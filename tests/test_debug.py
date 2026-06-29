# tests/test_debug.py

from devtoolbox.ai.ai_debugger import AIDebugger


def test_trace_stores_label_and_data():
    debugger = AIDebugger(verbose=False)

    debugger.trace("sample", {"status": "ok"})
    log = debugger.preview()

    assert "sample" in log
    assert log["sample"][0][1] == {"status": "ok"}


def test_suggest_fix_for_key_error():
    debugger = AIDebugger(verbose=False)

    suggestion = debugger.suggest_fix("KeyError: missing key")

    assert "Possible Fix" in suggestion
    assert "dictionary" in suggestion


def test_suggest_fix_for_unknown_error():
    debugger = AIDebugger(verbose=False)

    suggestion = debugger.suggest_fix("CustomError: something unusual happened")

    assert suggestion == "[SUGGESTION] No suggestion available."


def test_get_function_context_returns_metadata():
    debugger = AIDebugger(verbose=False)

    def sample_function(name: str, count: int = 1):
        """Example function for debugger inspection."""
        return name * count

    context = debugger.get_function_context(sample_function)

    assert context["name"] == "sample_function"
    assert "name: str" in context["signature"]
    assert "count: int = 1" in context["signature"]
    assert context["doc"] == "Example function for debugger inspection."


def test_log_error_stores_traceback_details():
    debugger = AIDebugger(verbose=False)

    try:
        raise ValueError("Invalid test value")
    except ValueError as error:
        debugger.log_error(type(error), error, error.__traceback__)

    log = debugger.preview()

    assert "errors" in log
    assert "ValueError" in log["errors"][0][1]
    assert "Invalid test value" in log["errors"][0][1]
