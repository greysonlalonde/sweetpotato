"""Provides core functionality and utilities for components.
"""

from threading import Lock


class ThreadSafe(type):
    """Metaclass for making class a thread-safe singleton."""

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
