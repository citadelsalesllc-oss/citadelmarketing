"""Rule-based, plain-language takeaways generated from the month-over-month deltas.

This is deliberately deterministic (no external LLM call) so the tool has no extra
API dependency or cost, and every client gets the same explainable logic.
"""

from typing import List

from .metrics import pct_change
from .models import GA4Report, MetaPeriod

GROWTH_THRESHOLD = 10  # +/- % change treated as a meaningful move vs. "held steady"


def _trend_word(change: float) -> str:
    if change >= GROWTH_THRESHOLD:
        return "grew"
    if change <= -GROWTH_THRESHOLD:
        return "dropped"
    return "held steady"


def generate_takeaways(
    ga4_report: GA4Report,
    meta_current: MetaPeriod,
    meta_previous: MetaPeriod,
) -> List[str]:
    takeaways: List[str] = []

    sessions_change = pct_change(ga4_report.current.sessions, ga4_report.previous.sessions)
    conv_change = pct_change(ga4_report.current.conversions, ga4_report.previous.conversions)
    cost_change = None
    if meta_previous.cost_per_result and meta_current.cost_per_result:
        cost_change = pct_change(meta_current.cost_per_result, meta_previous.cost_per_result)

    # 1. Traffic trend + top channel
    top_source = (
        ga4_report.source_medium[0]["source_medium"] if ga4_report.source_medium else "your top channel"
    )
    if sessions_change is None:
        takeaways.append(
            f"Website traffic came in this month with {top_source} driving the largest share of visits "
            f"(no prior-month traffic to compare against)."
        )
    else:
        trend = _trend_word(sessions_change)
        direction = "up" if sessions_change >= 0 else "down"
        takeaways.append(
            f"Website traffic {trend} {abs(sessions_change):.0f}% month-over-month ({direction} vs. last "
            f"month), with {top_source} driving the largest share of visits."
        )

    # 2. Conversions — what it means for the business, not just the number
    if conv_change is not None:
        if conv_change >= GROWTH_THRESHOLD:
            takeaways.append(
                f"Conversions increased {conv_change:.0f}% compared to last month — more visitors are "
                f"taking action (calls, form fills, quote requests), a sign your site and offers are "
                f"resonating with the people you're reaching."
            )
        elif conv_change <= -GROWTH_THRESHOLD:
            takeaways.append(
                f"Conversions fell {abs(conv_change):.0f}% compared to last month. Since this isn't just a "
                f"traffic problem, it's worth reviewing landing pages and calls-to-action for friction "
                f"before adjusting ad spend."
            )
        else:
            takeaways.append(
                "Conversions held roughly steady month-over-month, suggesting consistent performance from "
                "your website and offers."
            )
    elif ga4_report.current.conversions:
        takeaways.append(
            f"The site generated {ga4_report.current.conversions:.0f} conversions this month "
            f"(no prior-month figure to compare against)."
        )

    # 3. Ad efficiency — plain-language read on Meta spend
    if cost_change is not None:
        if cost_change <= -GROWTH_THRESHOLD:
            takeaways.append(
                f"Cost per result on Meta Ads improved by {abs(cost_change):.0f}%, meaning the same budget "
                f"is now producing more results — a good time to consider scaling spend while efficiency "
                f"is strong."
            )
        elif cost_change >= GROWTH_THRESHOLD:
            takeaways.append(
                f"Cost per result on Meta Ads rose {cost_change:.0f}% this month. Refreshing ad creative or "
                f"tightening audience targeting would help bring efficiency back in line before spend "
                f"increases further."
            )
        else:
            takeaways.append(
                "Meta Ads efficiency (cost per result) stayed consistent with last month, so the current "
                "targeting and creative are still performing reliably."
            )
    elif meta_current.spend:
        takeaways.append(
            f"Meta Ads spend was ${meta_current.spend:,.0f} this month, reaching {meta_current.reach:,} "
            f"people (no prior-month figure to compare against)."
        )

    return takeaways[:3]
