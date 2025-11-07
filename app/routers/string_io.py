from fastapi import APIRouter
from pydantic import BaseModel
import io
from app.models.io_models import IOExampleResponse, IOExample, TextInput, ProcessedOutput

router = APIRouter()

@router.get("/string", response_model=IOExampleResponse)
async def string_io_examples():
    """Demonstrates string I/O operations in Python."""
    # Example with StringIO
    string_buffer = io.StringIO()
    string_buffer.write("Hello, ")
    string_buffer.write("world!")
    string_buffer.seek(0)  # Move to the beginning of the buffer
    string_content = string_buffer.read()

    # Example with BytesIO
    bytes_buffer = io.BytesIO()
    bytes_buffer.write(b"Hello, ")
    bytes_buffer.write(b"binary world!")
    bytes_buffer.seek(0)  # Move to the beginning of the buffer
    bytes_content = bytes_buffer.read()

    return IOExampleResponse(
        description="String I/O in Python",
        examples=[
            IOExample(
                operation="StringIO - in-memory text stream",
                code="""
import io

string_buffer = io.StringIO()
string_buffer.write("Hello, ")
string_buffer.write("world!")
string_buffer.seek(0)  # Move to the beginning of the buffer
content = string_buffer.read()
""",
                output=string_content
            ),
            IOExample(
                operation="BytesIO - in-memory binary stream",
                code="""
import io

bytes_buffer = io.BytesIO()
bytes_buffer.write(b"Hello, ")
bytes_buffer.write(b"binary world!")
bytes_buffer.seek(0)  # Move to the beginning of the buffer
content = bytes_buffer.read()
""",
                output=str(bytes_content)
            ),
            IOExample(
                operation="Text processing with StringIO",
                code="""
import io

# Create a StringIO object from a string
text = "Line 1\\nLine 2\\nLine 3"
buffer = io.StringIO(text)

# Read line by line
line1 = buffer.readline()  # "Line 1\\n"
line2 = buffer.readline()  # "Line 2\\n"
"""
            ),
            IOExample(
                operation="Using StringIO as a file-like object",
                code="""
import io
import csv

# Create a StringIO object for writing CSV
output = io.StringIO()
csv_writer = csv.writer(output)
csv_writer.writerow(["Name", "Age", "City"])
csv_writer.writerow(["Alice", 30, "New York"])
csv_writer.writerow(["Bob", 25, "Chicago"])

# Get the CSV string
csv_string = output.getvalue()
""",
                explanation="StringIO objects can be used anywhere a file object is expected"
            )
        ]
    )

@router.post("/process", response_model=ProcessedOutput)
async def process_text(text_input: TextInput):
    """Process text input and return modified output."""
    original = text_input.content

    # Process the text (convert to uppercase)
    processed = original.upper()

    return ProcessedOutput(
        original=original,
        processed=processed,
        operation="Convert to uppercase"
    )