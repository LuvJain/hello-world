from fastapi import APIRouter
import sys
import io
from app.models.io_models import IOExampleResponse, IOExample

router = APIRouter()

@router.get("/console", response_model=IOExampleResponse)
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

    # Create response with examples
    return IOExampleResponse(
        description="Console I/O in Python",
        examples=[
            IOExample(
                operation="Print to console (stdout)",
                code='print("Hello from Python!")',
                output=output
            ),
            IOExample(
                operation="Read from console (stdin)",
                code='name = input("Enter your name: ")',
                explanation="This would prompt the user for input in a console application"
            ),
            IOExample(
                operation="Redirect stdout",
                code="""
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
            ),
            IOExample(
                operation="Error output (stderr)",
                code="""
import sys

# Print to stderr
sys.stderr.write("This is an error message\\n")

# Redirect stderr
import io
original_stderr = sys.stderr
captured_stderr = io.StringIO()
sys.stderr = captured_stderr

# Write to stderr
sys.stderr.write("This error is captured!\\n")

# Restore stderr
sys.stderr = original_stderr

# Get captured stderr output
error_output = captured_stderr.getvalue()
""",
                explanation="Python can write to and redirect standard error (stderr) as well as stdout"
            )
        ]
    )