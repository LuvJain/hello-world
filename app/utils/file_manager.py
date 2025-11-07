import os
import tempfile
import shutil

# Create and manage temporary directory for file operations
_temp_dir = None

def get_temp_dir():
    """Get or create a temporary directory for file operations."""
    global _temp_dir

    if _temp_dir is None:
        _temp_dir = os.path.join(tempfile.gettempdir(), "python_io_demo")
        os.makedirs(_temp_dir, exist_ok=True)

    return _temp_dir

def cleanup_temp_dir():
    """Clean up the temporary directory when shutting down."""
    global _temp_dir

    if _temp_dir and os.path.exists(_temp_dir):
        shutil.rmtree(_temp_dir)
        _temp_dir = None