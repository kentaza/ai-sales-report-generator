from fastapi.testclient import TestClient

from src.main import app
from src.services.csv_parser import CSVValidationError
from src.services.csv_parser import parse_sales_csv
from src.services.report_service import build_sales_summary

client = TestClient(app)

VALID_CSV = b"""date,region,product,units_sold,unit_price
2026-05-01,Bangkok,Product A,10,99
2026-05-01,Chiang Mai,Product B,4,149
2026-05-02,Bangkok,Product A,6,99
"""


def test_parse_sales_csv_returns_records() -> None:
    records = parse_sales_csv(VALID_CSV)

    assert len(records) == 3
    assert records[0].product == "Product A"
    assert records[1].units_sold == 4


def test_parse_sales_csv_rejects_missing_columns() -> None:
    invalid_csv = b"date,region,product,units_sold\n2026-05-01,Bangkok,Product A,10"

    try:
        parse_sales_csv(invalid_csv)
        assert False, "Expected CSVValidationError"
    except CSVValidationError as exc:
        assert "Missing required columns" in str(exc)


def test_build_sales_summary_returns_expected_metrics() -> None:
    records = parse_sales_csv(VALID_CSV)
    summary = build_sales_summary(records)

    assert summary["total_revenue"] == 2182.0
    assert summary["total_units_sold"] == 20
    assert summary["top_product"] == "Product A"
    assert summary["top_region"] == "Bangkok"
    assert summary["average_revenue_per_row"] == 727.33


def test_post_sales_report_returns_summary() -> None:
    response = client.post(
        "/reports/sales",
        files={"file": ("sales.csv", VALID_CSV, "text/csv")},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["rows"] == 3
    assert payload["summary"]["top_product"] == "Product A"
    assert "Bangkok" in payload["ai_summary"]


def test_post_sales_report_rejects_non_csv_file() -> None:
    response = client.post(
        "/reports/sales",
        files={"file": ("sales.txt", b"not,a,csv", "text/plain")},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Only CSV files are supported."
