class AIClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def is_configured(self) -> bool:
        return bool(self.api_key.strip())

    def generate_sales_summary(self, summary: dict[str, object]) -> str:
        top_product = summary["top_product"]
        top_region = summary["top_region"]
        total_revenue = summary["total_revenue"]
        total_units_sold = summary["total_units_sold"]

        if not self.is_configured():
            return (
                f"Sales generated total revenue of {total_revenue:.2f} from {total_units_sold} units sold. "
                f"{top_region} was the strongest region and {top_product} was the leading product. "
                "Monitor lower-performing areas and compare the next report for trend changes."
            )

        return (
            f"Sales generated total revenue of {total_revenue:.2f} from {total_units_sold} units sold. "
            f"{top_region} led performance and {top_product} drove the most revenue. "
            "This is a placeholder for real OpenAI integration when an API call is added."
        )
