from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel

from app.services.file_extractor import extract_text_from_file
from app.services.meta_client import MetaPageClient

router = APIRouter(prefix="/api/pages", tags=["pages"])


class PublishRequest(BaseModel):
    message: str
    link: str | None = None
    scheduled_time: str | None = None


@router.get("/health")
async def page_api_health():
    return {"status": "ready"}


@router.post("/publish")
async def publish_to_page(payload: PublishRequest):
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Message is required.")

    client = MetaPageClient()
    result = client.publish_post(payload.message, payload.link)
    return {"result": result}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    text = await extract_text_from_file(file)
    return {"filename": file.filename, "text": text}
