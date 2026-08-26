"""Shared data models, kept free of any API SDK imports so the PDF/insights
code doesn't require the Google or Meta libraries just to run."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class GA4Period:
    sessions: int = 0
    total_users: int = 0
    engaged_sessions: int = 0
    conversions: float = 0.0
    engagement_rate: float = 0.0


@dataclass
class GA4Report:
    current: GA4Period
    previous: GA4Period
    source_medium: List[dict] = field(default_factory=list)
    top_pages: List[dict] = field(default_factory=list)


@dataclass
class MetaPeriod:
    spend: float = 0.0
    reach: int = 0
    clicks: int = 0
    impressions: int = 0
    results: int = 0
    cost_per_result: Optional[float] = None
