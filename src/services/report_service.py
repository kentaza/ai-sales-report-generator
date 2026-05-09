from src.models import SalesRecord


def build_sales_summary(records: list[SalesRecord]) -> dict[str, object]:
    if not records:
        raise ValueError("At least one sales record is required.")

    total_revenue = 0.0
    total_units_sold = 0
    revenue_by_product: dict[str, float] = {}
    revenue_by_region: dict[str, float] = {}

    for record in records:
        revenue = record.units_sold * record.unit_price
        total_revenue += revenue
        total_units_sold += record.units_sold
        revenue_by_product[record.product] = revenue_by_product.get(record.product, 0.0) + revenue
        revenue_by_region[record.region] = revenue_by_region.get(record.region, 0.0) + revenue

    top_product = max(revenue_by_product, key=revenue_by_product.get)
    top_region = max(revenue_by_region, key=revenue_by_region.get)
    average_revenue_per_row = total_revenue / len(records)

    return {
        "total_revenue": round(total_revenue, 2),
        "total_units_sold": total_units_sold,
        "total_rows": len(records),
        "top_product": top_product,
        "top_region": top_region,
        "average_revenue_per_row": round(average_revenue_per_row, 2),
    }
