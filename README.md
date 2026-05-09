# AI Sales Report Generator

Beginner-friendly AI lab for learners from infrastructure, operations, cloud, or DevOps backgrounds.

## Goal

Upload a sales CSV file and generate:

- total revenue
- total units sold
- top product by revenue
- top region by revenue
- AI-generated business summary

This lab practices the full delivery flow from file upload to business logic to AI output.

## Features

- simple web upload form
- CSV validation
- sales metrics calculation
- AI summary generation
- JSON API response
- Docker Compose support
- GitHub Actions test workflow

## Repository Layout

```text
.
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|-- docs/
|   `-- architecture.md
|-- src/
|   |-- routes/
|   |   `-- reports.py
|   |-- services/
|   |   |-- ai_client.py
|   |   |-- csv_parser.py
|   |   `-- report_service.py
|   |-- templates/
|   |   `-- index.html
|   |-- config.py
|   |-- main.py
|   `-- models.py
|-- tests/
|   |-- test_health.py
|   `-- test_sales_report.py
|-- .env.example
|-- docker-compose.yml
|-- requirements.txt
`-- sample-sales.csv
```

## Input CSV Format

Required columns:

- `date`
- `region`
- `product`
- `units_sold`
- `unit_price`

Example:

```csv
date,region,product,units_sold,unit_price
2026-05-01,Bangkok,Product A,10,99
2026-05-01,Chiang Mai,Product B,4,149
2026-05-02,Bangkok,Product A,6,99
```

## Local Run

### 1. Create virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Create environment file

```powershell
Copy-Item .env.example .env
```

If `OPENAI_API_KEY` is empty, the app will return a safe mock summary instead of calling a real model.

### 3. Start the app

```powershell
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- App: `http://localhost:8000`
- Health: `http://localhost:8000/health`

## Run With Docker Compose

```powershell
docker compose up --build
```

## API

### `GET /`

Shows the upload form.

### `GET /health`

Returns container-friendly health status.

### `POST /reports/sales`

Accepts a CSV file upload and returns:

- `summary`
- `ai_summary`
- `rows`

## Test

```powershell
pytest
```

## Suggested Learning Flow

1. Run the starter app
2. Upload `sample-sales.csv`
3. Inspect the JSON summary
4. Read `src/services/csv_parser.py`
5. Read `src/services/report_service.py`
6. Modify one metric and rerun tests

## Next Improvements

- export markdown report
- return top 3 products
- compare two months
- add charts
