# devtoolbox/core/debug.py

def debug_log(message: str, level: str = "INFO"):
    """
    Simple logger to print debug messages with levels.
    Example:
        debug_log("Loading model...", level="INFO")
    """
    levels = {"INFO": "[ℹ️]", "WARNING": "[⚠️]", "ERROR": "[❌]"}
    prefix = levels.get(level.upper(), "[ℹ️]")
    print(f"{prefix} {message}")
