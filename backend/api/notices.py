# backend/api/notices.py

from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from backend.models.notice import NoticeInput, ParsedNotice, NoticeDocument
from backend.services.notice_parser import parse_notice
from backend.core.database import notices_collection

router = APIRouter(prefix="/notices", tags=["notices"])

@router.post("/parse", response_model=NoticeDocument)
async def parse_notice_endpoint(notice: NoticeInput):
    """
    Parse a notice with AI and save it to MongoDB.
    """
    try:
        # Step 1: Parse the notice with AI
        parsed = parse_notice(notice.raw_text)

        # Step 2: Build the full document to save
        document = NoticeDocument(
            **parsed.dict(),
            raw_text=notice.raw_text,
            source=notice.source,
            created_at=datetime.utcnow()
        )

        # Step 3: Save to MongoDB
        # .dict() converts Pydantic model to a Python dict MongoDB can store
        result = await notices_collection.insert_one(document.dict())

        # Step 4: Return the saved document
        return document

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/all", response_model=List[NoticeDocument])
async def get_all_notices():
    """
    Retrieve all stored notices from MongoDB.
    """
    try:
        # find({}) means "get everything" — no filter
        # to_list(100) means get up to 100 documents
        notices = await notices_collection.find({}).to_list(100)
        return notices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/priority/{level}", response_model=List[NoticeDocument])
async def get_notices_by_priority(level: str):
    """
    Retrieve notices filtered by priority level (high, medium, low).
    """
    try:
        notices = await notices_collection.find(
            {"priority": level}  # Filter by priority field
        ).to_list(100)
        return notices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))