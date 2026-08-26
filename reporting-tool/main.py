#!/usr/bin/env python3
"""CLI entry point: generate one client's monthly performance report PDF.

Usage:
    python main.py --client acme_dental --start 2026-07-01 --end 2026-07-31
"""

import argparse
import json
import os
from datetime import date, timedelta
from pathlib import Path

from dotenv import load_dotenv

from src.ga4_client import GA4Client
from src.insights import generate_takeaways
from src.meta_client import MetaClient
from src.pdf_generator import generate_pdf_report

BASE_DIR = Path(__file__).resolve().parent


def previous_period(start: date, end: date):
    """Same-length period immediately preceding [start, end]."""
    length_days = (end - start).days + 1
    prev_end = start - timedelta(days=1)
    prev_start = prev_end - timedelta(days=length_days - 1)
    return prev_start, prev_end


def load_client_config(name: str) -> dict:
    path = BASE_DIR / "config" / "clients" / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(
            f"No client config found at {path}.\n"
            f"Copy config/clients.example.json to config/clients/{name}.json "
            f"and fill in that client's details."
        )
    with open(path) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Generate a monthly performance report PDF for a client.")
    parser.add_argument("--client", required=True, help="Client config name (config/clients/<name>.json)")
    parser.add_argument("--start", required=True, help="Report period start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="Report period end date (YYYY-MM-DD)")
    parser.add_argument("--output", default=None, help="Output PDF path (default: output/<client>_<dates>.pdf)")
    args = parser.parse_args()

    load_dotenv(BASE_DIR / ".env")

    ga4_creds = os.environ.get("GA4_SERVICE_ACCOUNT_JSON")
    meta_token = os.environ.get("META_ACCESS_TOKEN")
    if not ga4_creds or not meta_token:
        raise SystemExit(
            "Missing credentials. Set GA4_SERVICE_ACCOUNT_JSON and META_ACCESS_TOKEN in your .env file.\n"
            "See README.md for step-by-step setup instructions."
        )
    if not os.path.exists(ga4_creds):
        raise SystemExit(f"GA4 service account key not found at: {ga4_creds}")

    client_config = load_client_config(args.client)

    start = date.fromisoformat(args.start)
    end = date.fromisoformat(args.end)
    if end < start:
        raise SystemExit("--end must be on or after --start")
    prev_start, prev_end = previous_period(start, end)

    client_name = client_config["client_name"]

    print(f"Fetching GA4 data for {client_name}...")
    ga4_client = GA4Client(ga4_creds)
    ga4_report = ga4_client.get_report(
        client_config["ga4_property_id"], start, end, prev_start, prev_end
    )

    print(f"Fetching Meta Ads data for {client_name}...")
    meta_client = MetaClient(
        meta_token,
        os.environ.get("META_APP_ID", ""),
        os.environ.get("META_APP_SECRET", ""),
    )
    result_action_type = client_config.get("meta_result_action_type", "lead")
    meta_current = meta_client.get_period(client_config["meta_ad_account_id"], start, end, result_action_type)
    meta_previous = meta_client.get_period(
        client_config["meta_ad_account_id"], prev_start, prev_end, result_action_type
    )

    takeaways = generate_takeaways(ga4_report, meta_current, meta_previous)

    output_path = args.output or str(
        BASE_DIR / "output" / f"{args.client}_{start.isoformat()}_to_{end.isoformat()}.pdf"
    )
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    print("Building PDF report...")
    generate_pdf_report(
        output_path=output_path,
        client_config=client_config,
        period_start=start,
        period_end=end,
        prev_start=prev_start,
        prev_end=prev_end,
        ga4_report=ga4_report,
        meta_current=meta_current,
        meta_previous=meta_previous,
        takeaways=takeaways,
    )
    print(f"Report saved to {output_path}")


if __name__ == "__main__":
    main()
