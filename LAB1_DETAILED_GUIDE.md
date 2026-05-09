# Lab 1: AI Sales Report Generator

Detailed beginner-friendly lab guide based on the starter template in `0.lab-starter-template`.

## Lab Goal

Build a small web application that lets a user upload a sales CSV file and receive:

- a sales summary
- basic business metrics
- AI-generated insights in plain language

This is the first lab because the input and output are clear, the logic is easy to explain, and it helps learners practice the full workflow:

- copy starter template
- implement a small feature
- run locally
- commit to GitHub

## Learning Objectives

By the end of this lab, the learner should be able to:

- understand a simple AI app architecture
- create a small FastAPI service
- accept and parse CSV uploads
- compute summary metrics from tabular data
- call an AI service to generate a readable report
- document the system in GitHub
- run the app using Docker Compose

## Recommended Time

- Instructor walkthrough: 2 to 3 hours
- Hands-on lab: 3 to 5 hours
- Homework or extension: 1 to 2 hours

## Target User

This lab is for a beginner who:

- comes from infrastructure, DevOps, or cloud work
- understands files, APIs, logs, and containers
- has limited software development experience

## Lab Story

The user uploads a monthly sales file. The system reads the data, computes the totals, finds the top products or regions, and asks the AI model to generate a short executive summary for a manager.

## Expected Input

CSV file with columns like:

```csv
date,region,product,units_sold,unit_price
2026-05-01,Bangkok,Product A,10,99
2026-05-01,Chiang Mai,Product B,4,149
2026-05-02,Bangkok,Product A,6,99
```

## Expected Output

- total revenue
- total units sold
- top product
- top region
- AI summary such as:

`Revenue was strongest in Bangkok, Product A was the main driver, and overall sales suggest stable demand with room to improve underperforming regions.`

## MVP Scope

The first version should include only these features:

1. Upload a CSV file
2. Parse the CSV safely
3. Compute a few summary metrics
4. Send the metrics to an AI prompt
5. Return a plain report page or JSON response

## Out Of Scope For MVP

Do not add these in the first pass:

- login or authentication
- database writes
- chart libraries
- background jobs
- multiple file upload
- PDF export

Keep the first version small and easy to finish.

## Architecture

## High-Level Flow

1. User opens the app
2. User uploads a CSV file
3. FastAPI receives the file
4. A parser converts CSV rows into Python objects
5. A service calculates summary metrics
6. An AI prompt is built from those metrics
7. The app returns a report to the user

## Components

- `UI layer`
  A simple HTML form or minimal frontend page for file upload

- `API layer`
  FastAPI endpoint for file upload and report generation

- `Parser layer`
  Reads CSV and validates required columns

- `Metrics service`
  Computes totals and top performers

- `AI service`
  Sends summarized data to the model and gets a human-readable explanation

## Suggested Project Structure

Use the starter template and expand `src/` like this:

```text
src/
|-- main.py
|-- config.py
|-- models.py
|-- routes/
|   `-- reports.py
|-- services/
|   |-- ai_client.py
|   |-- csv_parser.py
|   `-- report_service.py
`-- templates/
    `-- index.html
```

## Suggested API Design

- `GET /`
  Show upload form

- `GET /health`
  Health check

- `POST /reports/sales`
  Accept CSV upload and return generated report

## Data Contract

### Required CSV Columns

- `date`
- `region`
- `product`
- `units_sold`
- `unit_price`

### Derived Fields

- `revenue = units_sold * unit_price`

## Metrics To Calculate

For MVP, calculate:

- total revenue
- total units sold
- total number of rows
- top product by revenue
- top region by revenue
- average revenue per row

## AI Prompt Design

The AI does not need the raw CSV. It only needs the computed summary.

### Prompt Input Example

- total revenue: 1881
- total units sold: 20
- top product: Product A
- top region: Bangkok
- average revenue per row: 627

### Prompt Goal

Ask the model to:

- summarize the sales performance
- mention the strongest area
- mention one possible concern
- keep the answer short and professional

### Example Prompt

```text
You are a business analyst.
Write a short sales summary for a manager based on the following metrics.
Use simple professional language.
Mention the strongest signal and one area to monitor.

Metrics:
- Total revenue: 1881
- Total units sold: 20
- Top product: Product A
- Top region: Bangkok
- Average revenue per row: 627
```

## Step-By-Step Build Plan

## Phase 1: Create The Repo

1. Copy `0.lab-starter-template` into a new folder named `1.AI Sales Report Generator`
2. Initialize a Git repository if needed
3. Create a GitHub repository named `ai-sales-report-generator`
4. Push the starter code

## Phase 2: Update Docs

Update:

- `README.md`
- `docs/architecture.md`
- `.env.example`

Replace generic starter content with this lab-specific objective.

## Phase 3: Add CSV Parsing

Create `src/services/csv_parser.py` with responsibilities:

- decode uploaded file
- read CSV rows
- validate required headers
- convert rows into structured dictionaries

Important validation checks:

- file is not empty
- all required columns exist
- `units_sold` is numeric
- `unit_price` is numeric

## Phase 4: Add Report Logic

Create `src/services/report_service.py` with logic to:

- calculate revenue per row
- sum total revenue
- sum total units
- group by product
- group by region
- return a summary dictionary

## Phase 5: Add Upload Endpoint

Create `src/routes/reports.py` and add:

- `POST /reports/sales`

This endpoint should:

1. receive the uploaded file
2. call `csv_parser.py`
3. call `report_service.py`
4. optionally call `ai_client.py`
5. return report output

## Phase 6: Add Basic UI

Create `src/templates/index.html`:

- upload form
- submit button
- result area

Keep the UI plain. This is a backend-first lab.

## Phase 7: Connect AI

Update `src/services/ai_client.py` so it can:

- check whether API key exists
- accept a summary payload
- return generated text

For the first pass, it is okay to:

- return a mock summary if no key is configured
- add the real AI integration in the second pass

## Phase 8: Test And Verify

Add tests for:

- health endpoint
- CSV validation
- summary calculation

Manual checks:

- upload valid CSV
- upload CSV with missing headers
- upload CSV with invalid number format

## Phase 9: Docker And GitHub

Verify:

- app runs with `docker compose up --build`
- CI runs on push and pull request
- repo contains setup steps for the learner

## Implementation Milestones

## Milestone 1

The app starts and shows `GET /health`.

Definition:

- local run works
- Docker build works

## Milestone 2

CSV upload is accepted and parsed.

Definition:

- invalid file returns a clear error
- valid file is parsed into rows

## Milestone 3

Sales summary metrics are returned.

Definition:

- totals are correct
- top product and region are correct

## Milestone 4

AI summary is attached to the report.

Definition:

- app returns both numeric metrics and a human summary

## Milestone 5

Project is documented and pushed to GitHub.

Definition:

- `README.md` complete
- `docs/architecture.md` updated
- repo pushed

## Suggested Tasks For Students

### Task 1

Create the repo from the starter template.

### Task 2

Add the new report endpoint.

### Task 3

Implement CSV parsing.

### Task 4

Implement metrics calculation.

### Task 5

Connect the metrics to AI prompt generation.

### Task 6

Add tests and run the app in Docker.

## Codex Prompts For This Lab

Use these prompts during the lab.

### Setup Prompt

`Help me turn this starter template into Lab 1: AI Sales Report Generator. Keep it beginner-friendly and explain each file you add.`

### CSV Parser Prompt

`Create a simple csv_parser.py for FastAPI that validates required headers: date, region, product, units_sold, unit_price. Keep the code easy to read for a beginner from infrastructure background.`

### Metrics Prompt

`Write a report_service.py that calculates total revenue, total units sold, top product by revenue, top region by revenue, and average revenue per row from parsed CSV rows.`

### Route Prompt

`Add a POST /reports/sales endpoint to this FastAPI project. It should accept a CSV upload, parse the rows, calculate summary metrics, and return JSON.`

### AI Prompt

`Help me build a prompt for OpenAI that turns sales summary metrics into a short executive summary with one strength and one risk to monitor.`

### Test Prompt

`Write beginner-friendly pytest tests for CSV validation and sales summary calculation in this project.`

### Refactor Prompt

`Review this project structure and suggest small refactors that improve readability without making it too advanced for a beginner.`

## Instructor Notes

Focus on these teaching points:

- separate parsing from business logic
- keep endpoints thin
- explain why health checks matter
- explain why `.env.example` is useful
- show how Git commits should follow milestones

## Suggested Commit Plan

1. `chore: initialize lab 1 from starter template`
2. `feat: add csv parser for sales uploads`
3. `feat: add sales report metrics service`
4. `feat: add report endpoint and upload flow`
5. `feat: add ai sales summary generation`
6. `test: add health and report tests`
7. `docs: update readme and architecture notes`

## Grading Rubric

### Basic Pass

- app runs
- CSV upload works
- summary metrics are correct

### Good

- AI summary works
- error handling is clear
- repo documentation is complete

### Strong

- tests exist
- Docker setup works
- code is separated cleanly into parser, service, and route layers

## Stretch Goals

After the learner finishes MVP, add one or two of these:

- export report to markdown file
- add top 3 products instead of top 1
- compare current file to previous month
- show a simple HTML table for the parsed data
- add a mock chart section

## Common Beginner Mistakes

- mixing CSV parsing and business logic in one route
- sending raw CSV directly to AI instead of summarized data
- skipping input validation
- trying to build charts before the metrics work
- making the app too complex too early

## Definition Of Done

The lab is complete when:

- the learner can upload a CSV file
- the app returns correct sales metrics
- the app returns an AI-generated summary or safe mock summary
- the project runs locally
- the repo includes docs and Docker support
- the code is pushed to GitHub
