# devtoolbox/tasking/task_runner.py

import time
import threading
from typing import Callable, Any, Optional


class TaskRunner:
    def __init__(self):
        self.tasks = []

    def schedule_task(
        self,
        func: Callable,
        delay: float = 0.0,
        args: Optional[tuple] = None,
        kwargs: Optional[dict] = None,
    ):
        """Schedule a task to run after a delay."""
        args = () if args is None else args
        kwargs = {} if kwargs is None else kwargs

        task = threading.Timer(delay, func, args=args, kwargs=kwargs)
        self.tasks.append(task)
        task.start()
        return task

    def run_periodic(
        self,
        func: Callable,
        interval: float,
        args: Optional[tuple] = None,
        kwargs: Optional[dict] = None,
    ):
        """Run a task repeatedly at fixed intervals."""
        args = () if args is None else args
        kwargs = {} if kwargs is None else kwargs

        def wrapper():
            while True:
                func(*args, **kwargs)
                time.sleep(interval)

        thread = threading.Thread(target=wrapper, daemon=True)
        self.tasks.append(thread)
        thread.start()
        return thread

    def wait_all(self):
        """Wait for all non-daemon tasks to finish."""
        for task in self.tasks:
            if isinstance(task, threading.Timer):
                task.join()
