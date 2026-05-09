import csv
import io

from src.models import SalesRecord

REQUIRED_COLUMNS = {"date", "region", "product", "units_sold", "unit_price"}


class CSVValidationError(ValueError):
    pass


def parse_sales_csv(file_bytes: bytes) -> list[SalesRecord]:
    if not file_bytes:
        raise CSVValidationError("The uploaded file is empty.")

    try:
        decoded = file_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise CSVValidationError("The CSV file must use UTF-8 encoding.") from exc

    reader = csv.DictReader(io.StringIO(decoded))
    headers = set(reader.fieldnames or [])

    missing_columns = REQUIRED_COLUMNS - headers
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise CSVValidationError(f"Missing required columns: {missing}")

    records: list[SalesRecord] = []

    for line_number, row in enumerate(reader, start=2):
        try:
            units_sold = int(row["units_sold"])
        except (TypeError, ValueError) as exc:
            raise CSVValidationError(
                f"Invalid units_sold at line {line_number}: {row.get('units_sold')}"
            ) from exc

        try:
            unit_price = float(row["unit_price"])
        except (TypeError, ValueError) as exc:
            raise CSVValidationError(
                f"Invalid unit_price at line {line_number}: {row.get('unit_price')}"
            ) from exc

        records.append(
            SalesRecord(
                date=(row.get("date") or "").strip(),
                region=(row.get("region") or "").strip(),
                product=(row.get("product") or "").strip(),
                units_sold=units_sold,
                unit_price=unit_price,
            )
        )

    if not records:
        raise CSVValidationError("The uploaded CSV file does not contain any data rows.")

    return records
