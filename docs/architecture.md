# Architecture Note

## Objective

This lab lets a user upload a sales CSV file and generate a compact sales report with both numeric metrics and an AI-written executive summary. The design keeps the first version small so a beginner can understand the full end-to-end flow.

## Users

- Primary user: business user or analyst who wants a quick summary from sales data
- Secondary user: learner from infrastructure or DevOps who wants to understand how AI features fit into an application

## Main Flow

1. User opens the upload page.
2. User uploads a CSV file.
3. FastAPI validates and parses the CSV data.
4. The report service computes summary metrics.
5. The AI client turns those metrics into a short business summary.
6. The API returns the report as JSON and the page displays the result.

## Components

- `UI layer`: minimal HTML form for uploading a CSV file
- `API layer`: FastAPI routes for home page, health check, and report generation
- `Parser layer`: validates the file and converts CSV rows into structured records
- `Report service`: computes totals and top performers
- `AI client`: returns a mock summary or uses a real model later

## Data Flow

1. Input enters through the upload form.
2. The `/reports/sales` endpoint reads the uploaded file into memory.
3. The CSV parser checks required headers and numeric values.
4. The report service calculates revenue and summary metrics.
5. The AI client receives only the computed metrics, not the full raw file.
6. The response returns `summary`, `ai_summary`, and `rows`.

## Operations Notes

- Keep `OPENAI_API_KEY` in `.env`.
- Use the mock AI summary path when no API key is available.
- Keep the route thin and move logic into services.
- Keep `/health` available for containers and probes.

## Future Improvements

- add markdown or PDF export
- store uploaded reports in SQLite
- add charts for revenue by region and product
- compare reports between months
