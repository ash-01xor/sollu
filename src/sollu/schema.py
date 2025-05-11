from typing import Optional
from pydantic import BaseModel , Field

class ErrorResponse(BaseModel):
    error: str = Field(...,description="Error message.")
    details: Optional[str] = Field(None,description="Additional error details.")