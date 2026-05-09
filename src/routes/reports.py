from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import Request
from fastapi import UploadFile
from fastapi.templating import Jinja2Templates

from src.config import settings
from src.services.ai_client import AIClient
from src.services.csv_parser import CSVValidationError
from src.services.csv_parser import parse_sales_csv
from src.services.report_service import build_sales_summary

router = APIRouter(prefix="/reports", tags=["reports"])
templates = Jinja2Templates(directory="src/templates")


async def _build_report_response(file: UploadFile) -> dict[str, object]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    file_bytes = await file.read()

    try:
        records = parse_sales_csv(file_bytes)
    except CSVValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    summary = build_sales_summary(records)
    ai_result = AIClient(settings.openai_api_key).build_sales_summary_result(summary)

    return {
        "summary": summary,
        "ai_summary": ai_result["summary"],
        "ai_prompt": ai_result["prompt"],
        "rows": len(records),
    }


@router.post("/sales")
async def create_sales_report(file: UploadFile = File(...)) -> dict[str, object]:
    return await _build_report_response(file)


@router.post("/sales/view")
async def create_sales_report_view(
    request: Request,
    file: UploadFile = File(...),
):
    response_payload = await _build_report_response(file)
    return templates.TemplateResponse(
        request=request,
        name="report_result.html",
        context=response_payload,
        status_code=200,
    )
