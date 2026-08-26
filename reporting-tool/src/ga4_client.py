"""Wrapper around the GA4 Data API (Google Analytics 4)."""

from datetime import date
from typing import List

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    OrderBy,
    RunReportRequest,
)
from google.oauth2 import service_account

from .models import GA4Period, GA4Report


class GA4Client:
    """Thin wrapper over the GA4 Data API using a service account key file."""

    def __init__(self, service_account_path: str):
        credentials = service_account.Credentials.from_service_account_file(
            service_account_path,
            scopes=["https://www.googleapis.com/auth/analytics.readonly"],
        )
        self._client = BetaAnalyticsDataClient(credentials=credentials)

    def get_report(
        self,
        property_id: str,
        current_start: date,
        current_end: date,
        previous_start: date,
        previous_end: date,
    ) -> GA4Report:
        current = self._get_period_totals(property_id, current_start, current_end)
        previous = self._get_period_totals(property_id, previous_start, previous_end)
        source_medium = self._get_source_medium(property_id, current_start, current_end)
        top_pages = self._get_top_pages(property_id, current_start, current_end)
        return GA4Report(
            current=current,
            previous=previous,
            source_medium=source_medium,
            top_pages=top_pages,
        )

    def _get_period_totals(self, property_id: str, start: date, end: date) -> GA4Period:
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
            metrics=[
                Metric(name="sessions"),
                Metric(name="totalUsers"),
                Metric(name="engagedSessions"),
                Metric(name="conversions"),
                Metric(name="engagementRate"),
            ],
        )
        response = self._client.run_report(request)
        if not response.rows:
            return GA4Period()
        row = response.rows[0]
        return GA4Period(
            sessions=int(float(row.metric_values[0].value)),
            total_users=int(float(row.metric_values[1].value)),
            engaged_sessions=int(float(row.metric_values[2].value)),
            conversions=float(row.metric_values[3].value),
            engagement_rate=float(row.metric_values[4].value),
        )

    def _get_source_medium(self, property_id: str, start: date, end: date, limit: int = 5) -> List[dict]:
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
            dimensions=[Dimension(name="sessionSourceMedium")],
            metrics=[Metric(name="sessions")],
            limit=limit,
            order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
        )
        response = self._client.run_report(request)
        return [
            {
                "source_medium": row.dimension_values[0].value,
                "sessions": int(float(row.metric_values[0].value)),
            }
            for row in response.rows
        ]

    def _get_top_pages(self, property_id: str, start: date, end: date, limit: int = 5) -> List[dict]:
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
            dimensions=[Dimension(name="pagePath")],
            metrics=[Metric(name="screenPageViews")],
            limit=limit,
            order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="screenPageViews"), desc=True)],
        )
        response = self._client.run_report(request)
        return [
            {
                "page_path": row.dimension_values[0].value,
                "views": int(float(row.metric_values[0].value)),
            }
            for row in response.rows
        ]
