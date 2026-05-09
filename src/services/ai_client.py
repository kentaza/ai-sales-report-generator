class AIClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def is_configured(self) -> bool:
        return bool(self.api_key.strip())

    def build_sales_summary_prompt(self, summary: dict[str, object]) -> str:
        return f"""
You are a business analyst writing for a manager.

Write a short executive sales summary using the metrics below.

Rules:
- Use 3 short paragraphs or 3 bullet-style sentences.
- Sentence 1: overall performance summary.
- Sentence 2: one strength.
- Sentence 3: one risk or area to monitor.
- Use simple professional language.
- Do not invent numbers, trends, or causes that are not present in the input.

Metrics:
- Total revenue: {summary['total_revenue']}
- Total units sold: {summary['total_units_sold']}
- Total rows: {summary['total_rows']}
- Top product by revenue: {summary['top_product']}
- Top region by revenue: {summary['top_region']}
- Average revenue per row: {summary['average_revenue_per_row']}
""".strip()

    def generate_sales_summary(self, summary: dict[str, object]) -> str:
        prompt = self.build_sales_summary_prompt(summary)
        top_product = summary["top_product"]
        top_region = summary["top_region"]
        total_revenue = summary["total_revenue"]
        total_units_sold = summary["total_units_sold"]

        # Keep the prompt visible in code so learners can see how metrics
        # become structured AI input, even before real API integration.
        if not self.is_configured():
            return (
                f"Sales generated total revenue of {total_revenue:.2f} from {total_units_sold} units sold. "
                f"{top_region} was the strongest region and {top_product} was the leading product. "
                "Monitor lower-performing areas and compare the next report for trend changes."
            )

        return (
            "OpenAI integration is not connected yet. "
            "Use the generated prompt below with your model client:\n\n"
            f"{prompt}"
        )

    def build_sales_summary_result(self, summary: dict[str, object]) -> dict[str, str]:
        return {
            "prompt": self.build_sales_summary_prompt(summary),
            "summary": self.generate_sales_summary(summary),
        }
