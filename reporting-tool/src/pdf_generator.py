"""Builds the single-page client PDF report using ReportLab (pure Python, no
system-level dependencies like Cairo/Pango, so it installs cleanly everywhere).
"""

import os
from datetime import date
from typing import List, Optional

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from .metrics import pct_change
from .models import GA4Report, MetaPeriod

PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 0.45 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

LIGHT_GRAY = HexColor("#F4F5F7")
MID_GRAY = HexColor("#6B7280")
DARK_TEXT = HexColor("#1A1A2E")
GREEN = HexColor("#1B8A5A")
RED = HexColor("#C0392B")


def _safe_color(hex_value: str, fallback: str) -> HexColor:
    try:
        return HexColor(hex_value)
    except Exception:
        return HexColor(fallback)


def _fmt_change(current: float, previous: float, lower_is_better: bool = False) -> str:
    change = pct_change(current, previous)
    if change is None:
        return '<font color="#6B7280">n/a</font>'
    good = (change <= 0) if lower_is_better else (change >= 0)
    color = "#1B8A5A" if good else "#C0392B"
    arrow = "▲" if change >= 0 else "▼"
    return f'<font color="{color}">{arrow} {abs(change):.0f}%</font>'


def _kpi_cell(label: str, value: str, change_html: str, styles) -> List:
    return [
        Paragraph(label, styles["kpi_label"]),
        Paragraph(value, styles["kpi_value"]),
        Paragraph(f"vs. last month: {change_html}", styles["kpi_change"]),
    ]


def _build_styles(primary_color: HexColor):
    return {
        "client_name": ParagraphStyle(
            "client_name", fontName="Helvetica-Bold", fontSize=18, textColor=DARK_TEXT, leading=21
        ),
        "report_title": ParagraphStyle(
            "report_title", fontName="Helvetica", fontSize=10.5, textColor=MID_GRAY, leading=13
        ),
        "period": ParagraphStyle(
            "period", fontName="Helvetica", fontSize=9.5, textColor=MID_GRAY, alignment=2, leading=12
        ),
        "section_header": ParagraphStyle(
            "section_header",
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=primary_color,
            spaceBefore=2,
            spaceAfter=4,
        ),
        "kpi_label": ParagraphStyle(
            "kpi_label", fontName="Helvetica", fontSize=8, textColor=MID_GRAY, leading=10
        ),
        "kpi_value": ParagraphStyle(
            "kpi_value", fontName="Helvetica-Bold", fontSize=15, textColor=DARK_TEXT, leading=18, spaceBefore=1
        ),
        "kpi_change": ParagraphStyle(
            "kpi_change", fontName="Helvetica", fontSize=8, textColor=MID_GRAY, leading=10, spaceBefore=1
        ),
        "table_header": ParagraphStyle(
            "table_header", fontName="Helvetica-Bold", fontSize=8.5, textColor=colors.white, leading=11
        ),
        "table_cell": ParagraphStyle(
            "table_cell", fontName="Helvetica", fontSize=8.5, textColor=DARK_TEXT, leading=11
        ),
        "takeaway": ParagraphStyle(
            "takeaway",
            fontName="Helvetica",
            fontSize=9.5,
            textColor=DARK_TEXT,
            leading=13,
            spaceBefore=4,
            bulletIndent=0,
            leftIndent=14,
        ),
        "footer": ParagraphStyle(
            "footer", fontName="Helvetica", fontSize=7.5, textColor=MID_GRAY, leading=9
        ),
    }


def _header(client_config: dict, period_start: date, period_end: date, styles, primary_color):
    logo_path = client_config.get("brand", {}).get("logo_path")
    logo_cell = ""
    if logo_path and os.path.exists(logo_path):
        img = Image(logo_path)
        max_h = 0.55 * inch
        ratio = img.imageWidth / img.imageHeight if img.imageHeight else 1
        img.drawHeight = max_h
        img.drawWidth = max_h * ratio
        logo_cell = img

    name_block = [
        Paragraph(client_config["client_name"], styles["client_name"]),
        Paragraph("Monthly Performance Report", styles["report_title"]),
    ]
    period_text = Paragraph(
        f"{period_start.strftime('%b %d, %Y')} &ndash; {period_end.strftime('%b %d, %Y')}",
        styles["period"],
    )

    header_table = Table(
        [[logo_cell, name_block, period_text]],
        colWidths=[0.9 * inch, CONTENT_WIDTH - 0.9 * inch - 2.0 * inch, 2.0 * inch],
    )
    header_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (2, 0), (2, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    divider = Table([[""]], colWidths=[CONTENT_WIDTH], rowHeights=[3])
    divider.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), primary_color)]))

    return [header_table, Spacer(1, 6), divider, Spacer(1, 10)]


def _kpi_grid(ga4_report: GA4Report, meta_current: MetaPeriod, meta_previous: MetaPeriod, styles):
    c, p = ga4_report.current, ga4_report.previous
    cells = [
        _kpi_cell("Website Sessions", f"{c.sessions:,}", _fmt_change(c.sessions, p.sessions), styles),
        _kpi_cell("Website Users", f"{c.total_users:,}", _fmt_change(c.total_users, p.total_users), styles),
        _kpi_cell(
            "Conversions", f"{c.conversions:,.0f}", _fmt_change(c.conversions, p.conversions), styles
        ),
        _kpi_cell(
            "Engagement Rate",
            f"{c.engagement_rate * 100:.1f}%",
            _fmt_change(c.engagement_rate, p.engagement_rate),
            styles,
        ),
        _kpi_cell(
            "Meta Ad Spend",
            f"${meta_current.spend:,.0f}",
            _fmt_change(meta_current.spend, meta_previous.spend, lower_is_better=True),
            styles,
        ),
        _kpi_cell(
            "Meta Reach", f"{meta_current.reach:,}", _fmt_change(meta_current.reach, meta_previous.reach), styles
        ),
        _kpi_cell(
            "Meta Clicks",
            f"{meta_current.clicks:,}",
            _fmt_change(meta_current.clicks, meta_previous.clicks),
            styles,
        ),
        _kpi_cell(
            "Cost per Result",
            f"${meta_current.cost_per_result:,.2f}" if meta_current.cost_per_result else "n/a",
            (
                _fmt_change(meta_current.cost_per_result, meta_previous.cost_per_result, lower_is_better=True)
                if meta_current.cost_per_result and meta_previous.cost_per_result
                else '<font color="#6B7280">n/a</font>'
            ),
            styles,
        ),
    ]

    col_w = CONTENT_WIDTH / 4
    rows = [cells[0:4], cells[4:8]]
    grid = Table(rows, colWidths=[col_w] * 4, rowHeights=[0.72 * inch, 0.72 * inch])
    grid.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GRAY),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.white),
                ("INNERGRID", (0, 0), (-1, -1), 3, colors.white),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return grid


def _breakdown_tables(ga4_report: GA4Report, primary_color, styles):
    total_sessions = sum(row["sessions"] for row in ga4_report.source_medium) or 1

    src_header = [Paragraph("Source / Medium", styles["table_header"]), Paragraph("Sessions", styles["table_header"])]
    src_rows = [src_header]
    for row in ga4_report.source_medium[:5]:
        pct = row["sessions"] / total_sessions * 100
        src_rows.append(
            [
                Paragraph(row["source_medium"], styles["table_cell"]),
                Paragraph(f"{row['sessions']:,} ({pct:.0f}%)", styles["table_cell"]),
            ]
        )
    src_table = Table(src_rows, colWidths=[1.55 * inch, 1.15 * inch], repeatRows=1)

    pages_header = [Paragraph("Top Pages", styles["table_header"]), Paragraph("Views", styles["table_header"])]
    pages_rows = [pages_header]
    for row in ga4_report.top_pages[:5]:
        pages_rows.append(
            [
                Paragraph(row["page_path"], styles["table_cell"]),
                Paragraph(f"{row['views']:,}", styles["table_cell"]),
            ]
        )
    pages_table = Table(pages_rows, colWidths=[1.9 * inch, 0.8 * inch], repeatRows=1)

    for t in (src_table, pages_table):
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), primary_color),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.white),
                ]
            )
        )

    wrapper = Table(
        [[src_table, pages_table]],
        colWidths=[CONTENT_WIDTH / 2, CONTENT_WIDTH / 2],
    )
    wrapper.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 10),
            ]
        )
    )
    return wrapper


def _takeaways_block(takeaways: List[str], primary_color, styles):
    flow = [Paragraph("What This Means For Your Business", styles["section_header"])]
    for t in takeaways:
        flow.append(Paragraph(f"&bull;&nbsp;&nbsp;{t}", styles["takeaway"]))
    return flow


def generate_pdf_report(
    output_path: str,
    client_config: dict,
    period_start: date,
    period_end: date,
    prev_start: date,
    prev_end: date,
    ga4_report: GA4Report,
    meta_current: MetaPeriod,
    meta_previous: MetaPeriod,
    takeaways: List[str],
) -> None:
    brand = client_config.get("brand", {})
    primary_color = _safe_color(brand.get("primary_color", "#0B5FFF"), "#0B5FFF")

    styles = _build_styles(primary_color)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title=f"{client_config['client_name']} Monthly Performance Report",
    )

    story = []
    story += _header(client_config, period_start, period_end, styles, primary_color)

    story.append(Paragraph("Key Metrics", styles["section_header"]))
    story.append(_kpi_grid(ga4_report, meta_current, meta_previous, styles))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Website Performance Detail", styles["section_header"]))
    story.append(_breakdown_tables(ga4_report, primary_color, styles))
    story.append(Spacer(1, 12))

    story += _takeaways_block(takeaways, primary_color, styles)
    story.append(Spacer(1, 10))

    footer_text = (
        f"Prepared by Citadel Sales &amp; Marketing &middot; Generated {date.today().strftime('%B %d, %Y')} "
        f"&middot; Previous period compared: {prev_start.strftime('%b %d')}&ndash;{prev_end.strftime('%b %d, %Y')}"
    )
    story.append(Paragraph(footer_text, styles["footer"]))

    doc.build(story)
