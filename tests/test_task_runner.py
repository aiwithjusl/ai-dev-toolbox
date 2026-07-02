# tests/test_task_runner.py

import unittest
import time
import threading
from devtoolbox.tasking.task_runner import TaskRunner


class TestTaskRunner(unittest.TestCase):
    def setUp(self):
        self.runner = TaskRunner()
        self.log = []

    def test_schedule_task(self):
        def sample_task():
            self.log.append("task_run")

        task = self.runner.schedule_task(sample_task, delay=0.2)
        task.join()

        self.assertIsInstance(task, threading.Timer)
        self.assertIn("task_run", self.log)

    def test_schedule_task_with_args_and_kwargs(self):
        def sample_task(name, punctuation="!"):
            self.log.append(f"Hello, {name}{punctuation}")

        task = self.runner.schedule_task(
            sample_task,
            delay=0.2,
            args=("Justin",),
            kwargs={"punctuation": "."},
        )
        task.join()

        self.assertIn("Hello, Justin.", self.log)

    def test_run_periodic(self):
        def periodic_task():
            self.log.append("tick")

        thread = self.runner.run_periodic(periodic_task, interval=0.2)
        time.sleep(0.7)

        self.assertIsInstance(thread, threading.Thread)
        self.assertTrue(thread.daemon)
        self.assertGreaterEqual(self.log.count("tick"), 2)

    def test_wait_all(self):
        def sample_task():
            self.log.append("done")

        self.runner.schedule_task(sample_task, delay=0.2)
        self.runner.wait_all()

        self.assertIn("done", self.log)


if __name__ == "__main__":
    unittest.main()
