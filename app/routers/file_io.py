from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import tempfile
import shutil
from app.models.io_models import IOExampleResponse, IOExample, FileInfo
from app.utils.file_manager import get_temp_dir

router = APIRouter()
temp_dir = get_temp_dir()

@router.get("/file", response_model=IOExampleResponse)
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

    return IOExampleResponse(
        description="File I/O in Python",
        examples=[
            IOExample(
                operation="Write to a file",
                code="""
with open('sample.txt', 'w') as f:
    f.write('This is an example file.\\nIt has multiple lines.\\nPython file I/O is powerful and flexible.')
""",
                explanation="Opens a file in write mode and writes string content to it"
            ),
            IOExample(
                operation="Read entire file",
                code="""
with open('sample.txt', 'r') as f:
    content = f.read()
""",
                output=read_content
            ),
            IOExample(
                operation="Read file line by line",
                code="""
with open('sample.txt', 'r') as f:
    lines = f.readlines()
""",
                output=example_content.split("\n")
            ),
            IOExample(
                operation="Append to a file",
                code="""
with open('sample.txt', 'a') as f:
    f.write('\\nThis line was appended!')
"""
            ),
            IOExample(
                operation="Binary file I/O",
                code="""
# Writing binary data
with open('binary_file.bin', 'wb') as f:
    f.write(b'\\x00\\x01\\x02\\x03')

# Reading binary data
with open('binary_file.bin', 'rb') as f:
    binary_data = f.read()
"""
            ),
            IOExample(
                operation="Using context managers",
                code="""
# Context managers automatically close files when exiting the block
with open('file.txt', 'w') as f:
    f.write('Content')
# File is automatically closed here
""",
                explanation="Context managers (with statements) ensure files are properly closed"
            ),
            IOExample(
                operation="Using os module for file operations",
                code="""
import os

# Check if file exists
exists = os.path.exists('file.txt')

# Get file size
size = os.path.getsize('file.txt')

# Remove a file
os.remove('file.txt')

# Create a directory
os.makedirs('new_directory', exist_ok=True)
"""
            )
        ]
    )

@router.post("/upload", response_model=FileInfo)
async def upload_file(file: UploadFile = File(...)):
    """Upload a file and store it on the server."""
    try:
        # Save the uploaded file
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get file size
        file_size = os.path.getsize(file_path)

        return FileInfo(
            filename=file.filename,
            size_bytes=file_size,
            stored_at=file_path,
            content_type=file.content_type
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@router.get("/download/{filename}")
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