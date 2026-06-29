# tests/test_debug.py

import unittest
from devtoolbox.ai.ai_debugger import AIDebugger


class TestAIDebugger(unittest.TestCase):
    def test_trace_stores_label_and_data(self):
        debugger = AIDebugger(verbose=False)

        debugger.trace("sample", {"status": "ok"})
        log = debugger.preview()

        self.assertIn("sample", log)
        self.assertEqual(log["sample"][0][1], {"status": "ok"})

    def test_suggest_fix_for_key_error(self):
        debugger = AIDebugger(verbose=False)

        suggestion = debugger.suggest_fix("KeyError: missing key")

        self.assertIn("Possible Fix", suggestion)
        self.assertIn("dictionary", suggestion)

    def test_suggest_fix_for_unknown_error(self):
        debugger = AIDebugger(verbose=False)

        suggestion = debugger.suggest_fix("CustomError: something unusual happened")

        self.assertEqual(
            suggestion,
            "[SUGGESTION] No suggestion available."
        )

    def test_get_function_context_returns_metadata(self):
        debugger = AIDebugger(verbose=False)

        def sample_function(name: str, count: int = 1):
            """Example function for debugger inspection."""
            return name * count

        context = debugger.get_function_context(sample_function)

        self.assertEqual(context["name"], "sample_function")
        self.assertIn("name: str", context["signature"])
        self.assertIn("count: int = 1", context["signature"])
        self.assertEqual(
            context["doc"],
            "Example function for debugger inspection."
        )

    def test_log_error_stores_traceback_details(self):
        debugger = AIDebugger(verbose=False)

        try:
            raise ValueError("Invalid test value")
        except ValueError as error:
            debugger.log_error(type(error), error, error.__traceback__)

        log = debugger.preview()

        self.assertIn("errors", log)
        self.assertIn("ValueError", log["errors"][0][1])
        self.assertIn("Invalid test value", log["errors"][0][1])


if __name__ == "__main__":
    unittest.main()
