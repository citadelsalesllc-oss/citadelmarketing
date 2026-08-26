"""Shared helpers for comparing current vs. previous period metrics."""

from typing import Optional


def pct_change(current: float, previous: float) -> Optional[float]:
    """Percent change from previous to current. None if previous is 0 (undefined)."""
    if not previous:
        return None
    return ((current - previous) / previous) * 100
