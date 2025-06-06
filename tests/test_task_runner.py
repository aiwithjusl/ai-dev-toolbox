# tests/test_task_runner.py

import unittest
import time
from devtoolbox.tasking.task_runner import TaskRunner

class TestTaskRunner(unittest.TestCase):
    def setUp(self):
        self.runner = TaskRunner()
        self.log = []

    def test_schedule_task(self):
        def sample_task():
            self.log.append("task_run")

        self.runner.schedule_task(sample_task, delay=0.5)
        time.sleep(1)  # Wait for the task to complete
        self.assertIn("task_run", self.log)

    def test_run_periodic(self):
        def periodic_task():
            self.log.append("tick")

        self.runner.run_periodic(periodic_task, interval=0.3)
        time.sleep(1)  # Let it run a few times
        self.assertGreaterEqual(self.log.count("tick"), 2)

if __name__ == '__main__':
    unittest.main()
