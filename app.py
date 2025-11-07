from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import console_io, file_io, string_io
from app.utils.file_manager import cleanup_temp_dir
import atexit

# Create FastAPI application
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

# Register cleanup function
atexit.register(cleanup_temp_dir)

# Root endpoint
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
            {"path": "/io/process", "description": "Process text input"},
        ]
    }

# Include routers
app.include_router(console_io.router, prefix="/io", tags=["Console I/O"])
app.include_router(file_io.router, prefix="/io", tags=["File I/O"])
app.include_router(string_io.router, prefix="/io", tags=["String I/O"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)