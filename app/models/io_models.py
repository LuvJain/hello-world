from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class TextInput(BaseModel):
    """Model for text input data."""
    content: str

class ProcessedOutput(BaseModel):
    """Model for processed output data."""
    original: str
    processed: str
    operation: str

class FileInfo(BaseModel):
    """Model for file information."""
    filename: str
    size_bytes: int
    stored_at: str
    content_type: str

class IOExample(BaseModel):
    """Model for I/O code examples."""
    operation: str
    code: str
    output: Optional[Any] = None
    explanation: Optional[str] = None

class IOExampleResponse(BaseModel):
    """Model for I/O example responses."""
    description: str
    examples: List[IOExample]