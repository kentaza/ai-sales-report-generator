from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from src.config import settings
from src.routes.reports import router as reports_router

app = FastAPI(title=settings.app_name)
templates = Jinja2Templates(directory="src/templates")

app.include_router(reports_router)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.app_name,
            "environment": settings.app_env,
        },
    )


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
