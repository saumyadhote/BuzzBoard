# backend/models/notice.py

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# This is the data that comes IN to our API
class NoticeInput(BaseModel):
    raw_text: str                  # The notice text to analyze
    source: Optional[str] = None  # Where it came from (optional)

# This is the structured data that comes OUT after Claude analyzes it
class ParsedNotice(BaseModel):
    title: str                        # Short title of the notice
    summary: str                      # 1-2 sentence summary
    deadlines: List[str]              # Any dates/deadlines found
    category: str                     # e.g. "exam", "assignment", "event"
    priority: str                     # "high", "medium", or "low"
    action_required: bool             # Does the student need to DO something?
    
class NoticeDocument(ParsedNotice):
    raw_text: str                          # Keep the original text too
    source: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Auto timestamp