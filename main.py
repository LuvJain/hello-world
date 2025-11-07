from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import io
import sys
import tempfile
import shutil

app = FastAPI(
    title="Python I/O Basics",
    description="A FastAPI application demonstrating Python input/output operations",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create temporary data directory
temp_dir = os.path.join(tempfile.gettempdir(), "python_io_demo")
os.makedirs(temp_dir, exist_ok=True)

# Models
class TextInput(BaseModel):
    content: str

class ProcessedOutput(BaseModel):
    original: str
    processed: str
    operation: str

@app.get("/")
async def root():
    """Root endpoint that returns basic information about the API."""
    return {
        "message": "Welcome to Python I/O Basics API",
        "description": "This API demonstrates various input/output operations in Python",
        "endpoints": [
            {"path": "/", "description": "This help message"},
            {"path": "/docs", "description": "Interactive API documentation"},
            {"path": "/io/console", "description": "Examples of console I/O"},
            {"path": "/io/file", "description": "Examples of file I/O"},
            {"path": "/io/string", "description": "Examples of string I/O"},
            {"path": "/io/upload", "description": "Upload a file"},
            {"path": "/io/download/{filename}", "description": "Download a file"},
        ]
    }

# Console I/O examples
@app.get("/io/console")
async def console_io_examples():
    """Demonstrates console I/O operations in Python."""
    # Capture stdout
    original_stdout = sys.stdout
    captured_stdout = io.StringIO()
    sys.stdout = captured_stdout

    # Print to stdout (this will be captured)
    print("Hello from Python!")
    print("This is a demonstration of console output.")

    # Restore stdout
    sys.stdout = original_stdout

    # Get the captured output
    output = captured_stdout.getvalue()

    return {
        "description": "Console I/O in Python",
        "examples": [
            {
                "operation": "Print to console (stdout)",
                "code": 'print("Hello from Python!")',
                "output": output
            },
            {
                "operation": "Read from console (stdin)",
                "code": 'name = input("Enter your name: ")',
                "explanation": "This would prompt the user for input in a console application"
            },
            {
                "operation": "Redirect stdout",
                "code": """
import sys
import io

# Redirect stdout to a StringIO object
original_stdout = sys.stdout
captured_stdout = io.StringIO()
sys.stdout = captured_stdout

# Print something
print("This will be captured!")

# Restore stdout
sys.stdout = original_stdout

# Get the captured output
output = captured_stdout.getvalue()
"""
            }
        ]
    }

# File I/O examples
@app.get("/io/file")
async def file_io_examples():
    """Demonstrates file I/O operations in Python."""
    # Example file content
    example_content = "This is an example file.\nIt has multiple lines.\nPython file I/O is powerful and flexible."

    # Create a sample file
    sample_file_path = os.path.join(temp_dir, "sample.txt")
    with open(sample_file_path, "w") as f:
        f.write(example_content)

    # Read the file back
    with open(sample_file_path, "r") as f:
        read_content = f.read()

    return {
        "description": "File I/O in Python",
        "examples": [
            {
                "operation": "Write to a file",
                "code": """
with open('sample.txt', 'w') as f:
    f.write('This is an example file.\\nIt has multiple lines.\\nPython file I/O is powerful and flexible.')
""",
                "explanation": "Opens a file in write mode and writes string content to it"
            },
            {
                "operation": "Read entire file",
                "code": """
with open('sample.txt', 'r') as f:
    content = f.read()
""",
                "output": read_content
            },
            {
                "operation": "Read file line by line",
                "code": """
with open('sample.txt', 'r') as f:
    lines = f.readlines()
""",
                "output": example_content.split("\n")
            },
            {
                "operation": "Append to a file",
                "code": """
with open('sample.txt', 'a') as f:
    f.write('\\nThis line was appended!')
"""
            },
            {
                "operation": "Binary file I/O",
                "code": """
# Writing binary data
with open('binary_file.bin', 'wb') as f:
    f.write(b'\\x00\\x01\\x02\\x03')

# Reading binary data
with open('binary_file.bin', 'rb') as f:
    binary_data = f.read()
"""
            }
        ]
    }

# String I/O examples
@app.get("/io/string")
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

    return {
        "description": "String I/O in Python",
        "examples": [
            {
                "operation": "StringIO - in-memory text stream",
                "code": """
import io

string_buffer = io.StringIO()
string_buffer.write("Hello, ")
string_buffer.write("world!")
string_buffer.seek(0)  # Move to the beginning of the buffer
content = string_buffer.read()
""",
                "output": string_content
            },
            {
                "operation": "BytesIO - in-memory binary stream",
                "code": """
import io

bytes_buffer = io.BytesIO()
bytes_buffer.write(b"Hello, ")
bytes_buffer.write(b"binary world!")
bytes_buffer.seek(0)  # Move to the beginning of the buffer
content = bytes_buffer.read()
""",
                "output": str(bytes_content)
            },
            {
                "operation": "Text processing with StringIO",
                "code": """
import io

# Create a StringIO object from a string
text = "Line 1\\nLine 2\\nLine 3"
buffer = io.StringIO(text)

# Read line by line
line1 = buffer.readline()  # "Line 1\\n"
line2 = buffer.readline()  # "Line 2\\n"
"""
            }
        ]
    }

# File upload endpoint
@app.post("/io/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload a file and store it on the server."""
    try:
        # Save the uploaded file
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get file size
        file_size = os.path.getsize(file_path)

        return {
            "filename": file.filename,
            "size_bytes": file_size,
            "stored_at": file_path,
            "content_type": file.content_type,
            "explanation": "This endpoint demonstrates how to handle file uploads in FastAPI, which is a common I/O operation in web applications."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

# File download endpoint
@app.get("/io/download/{filename}")
async def download_file(filename: str):
    """Download a file that was previously uploaded."""
    file_path = os.path.join(temp_dir, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found")

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )

# Text processing endpoint
@app.post("/io/process")
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)