from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Union, Tuple

class DataStructureExample(BaseModel):
    """Model for data structure code examples."""
    name: str
    description: str
    code: str
    output: Optional[Any] = None
    explanation: Optional[str] = None
    operations: Optional[List[Dict[str, str]]] = None

class DataStructureResponse(BaseModel):
    """Model for data structure example responses."""
    description: str
    examples: List[DataStructureExample]