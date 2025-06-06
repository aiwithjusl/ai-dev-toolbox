# devtoolbox/tasking/task_runner.py

import time
import threading
from typing import Callable, Any


class TaskRunner:
    def __init__(self):
        self.tasks = []

    def schedule_task(self, func: Callable, delay: float = 0.0, args: tuple = (), kwargs: dict = {}):
        """Schedule a task to run after a delay"""
        task = threading.Timer(delay, func, args=args, kwargs=kwargs)
        self.tasks.append(task)
        task.start()

    def run_periodic(self, func: Callable, interval: float, args: tuple = (), kwargs: dict = {}):
        """Run a task repeatedly at fixed intervals"""
        def wrapper():
            while True:
                func(*args, **kwargs)
                time.sleep(interval)

        thread = threading.Thread(target=wrapper, daemon=True)
        self.tasks.append(thread)
        thread.start()

    def wait_all(self):
        """Wait for all non-daemon tasks to finish"""
        for task in self.tasks:
            if isinstance(task, threading.Timer):
                task.join()
