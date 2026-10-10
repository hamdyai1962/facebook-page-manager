from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.config import settings
from app.routes.agent import router as agent_router
from app.routes.health import router as health_router
from app.routes.pages import router as pages_router

app = FastAPI(title=settings.app_name, version="0.1.0")

app.include_router(health_router)
app.include_router(agent_router)
app.include_router(pages_router)

frontend_dir = Path(__file__).resolve().parent.parent.parent / "frontend"
if frontend_dir.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")


@app.get("/")
async def root():
    return {"message": "Facebook Page Manager & Multimodal AI Agent is running.", "docs": "/docs"}
