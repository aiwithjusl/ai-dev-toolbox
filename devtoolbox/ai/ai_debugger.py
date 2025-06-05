# devtoolbox/ai/ai_debugger.py

import sys
import traceback
import inspect
from datetime import datetime
from collections import defaultdict

class AIDebugger:
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.log = defaultdict(list)

    def trace(self, label, data):
        timestamp = datetime.utcnow().isoformat()
        self.log[label].append((timestamp, data))
        if self.verbose:
            print(f"[TRACE] {label} @ {timestamp}: {data}")

    def log_error(self, exc_type, exc_value, tb):
        error_details = ''.join(traceback.format_exception(exc_type, exc_value, tb))
        if self.verbose:
            print(f"\n[ERROR] {exc_type.__name__}: {exc_value}")
            print("[TRACEBACK]")
            print(error_details)
        self.log["errors"].append((datetime.utcnow().isoformat(), error_details))

    def attach_global_hook(self):
        sys.excepthook = self.log_error

    def get_function_context(self, func):
        sig = inspect.signature(func)
        doc = inspect.getdoc(func)
        return {
            "name": func.__name__,
            "signature": str(sig),
            "doc": doc or "No docstring available."
        }

    def suggest_fix(self, error_message):
        """Very basic heuristic fix suggestions"""
        suggestions = {
            "KeyError": "Check if key exists in dictionary before accessing.",
            "IndexError": "Check list/array index bounds.",
            "TypeError": "Check data types of arguments and variables.",
            "ValueError": "Validate input values before passing.",
            "AttributeError": "Check if object has the attribute you're trying to access.",
        }
        for key, fix in suggestions.items():
            if key in error_message:
                return f"[SUGGESTION] Possible Fix: {fix}"
        return "[SUGGESTION] No suggestion available."

    def preview(self):
        return dict(self.log)
