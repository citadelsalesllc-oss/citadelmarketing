"""Wrapper around the Meta Marketing API (Meta Ads Manager insights)."""

from datetime import date

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

from .models import MetaPeriod


class MetaClient:
    """Thin wrapper over the Meta Marketing API insights endpoint."""

    def __init__(self, access_token: str, app_id: str = "", app_secret: str = ""):
        FacebookAdsApi.init(app_id or None, app_secret or None, access_token)

    def get_period(
        self,
        ad_account_id: str,
        start: date,
        end: date,
        result_action_type: str = "lead",
    ) -> MetaPeriod:
        account = AdAccount(ad_account_id)
        insights = account.get_insights(
            fields=[
                "spend",
                "reach",
                "clicks",
                "impressions",
                "actions",
                "cost_per_action_type",
            ],
            params={
                "time_range": {"since": start.isoformat(), "until": end.isoformat()},
                "level": "account",
            },
        )
        if not insights:
            return MetaPeriod()

        row = insights[0]
        spend = float(row.get("spend", 0) or 0)
        reach = int(float(row.get("reach", 0) or 0))
        clicks = int(float(row.get("clicks", 0) or 0))
        impressions = int(float(row.get("impressions", 0) or 0))

        results = 0
        for action in row.get("actions", []) or []:
            if action.get("action_type") == result_action_type:
                results = int(float(action.get("value", 0)))
                break

        cost_per_result = None
        for cpa in row.get("cost_per_action_type", []) or []:
            if cpa.get("action_type") == result_action_type:
                cost_per_result = float(cpa.get("value", 0))
                break
        if cost_per_result is None and results:
            cost_per_result = spend / results

        return MetaPeriod(
            spend=spend,
            reach=reach,
            clicks=clicks,
            impressions=impressions,
            results=results,
            cost_per_result=cost_per_result,
        )
