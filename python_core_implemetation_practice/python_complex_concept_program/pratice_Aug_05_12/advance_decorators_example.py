"""
Advanced Python Programs Collection
==================================
Each program demonstrates complex Python concepts in under 100 lines
"""

# Program 1: Advanced Decorators with Class-based and Function Composition
# =========================================================================

import functools
import time
import threading
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass, field
from contextlib import contextmanager
from collections import defaultdict, deque
import asyncio
import weakref


class AdvancedDecorators:
    """Program 1: Complex decorator patterns with caching, timing, and retry logic"""

    def __init__(self):
        self.cache = {}
        self.call_stats = defaultdict(int)

    def smart_cache(self, ttl: int = 300):
        """Decorator with TTL-based caching and statistics"""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Create cache key from args and kwargs
                key = str(args) + str(sorted(kwargs.items()))
                current_time = time.time()

                # Check cache validity
                if key in self.cache:
                    cached_time, result = self.cache[key]
                    if current_time - cached_time < ttl:
                        self.call_stats[f"{func.__name__}_cache_hit"] += 1
                        return result

                # Execute function and cache result
                result = func(*args, **kwargs)
                self.cache[key] = (current_time, result)
                self.call_stats[f"{func.__name__}_cache_miss"] += 1
                return result

            wrapper.clear_cache = lambda: self.cache.clear()
            wrapper.stats = lambda: dict(self.call_stats)
            return wrapper

        return decorator

    def retry_with_backoff(self, max_attempts: int = 3):
        """Decorator with exponential backoff retry logic"""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise e
                        wait_time = (2 ** attempt) * 0.1
                        time.sleep(wait_time)
                        print(f"Retry {attempt + 1} after {wait_time}s: {e}")

            return wrapper

        return decorator


# Demo for Program 1
def demo_decorators():
    decorators = AdvancedDecorators()

    @decorators.smart_cache(ttl=5)
    @decorators.retry_with_backoff(max_attempts=2)
    def expensive_calculation(n: int) -> int:
        if n < 0:
            raise ValueError("Negative number")
        time.sleep(0.1)  # Simulate expensive operation
        return n ** 2

    print("=== Advanced Decorators Demo ===")
    print(f"Result: {expensive_calculation(5)}")
    print(f"Cached: {expensive_calculation(5)}")
    print(f"Stats: {expensive_calculation.stats()}")


if __name__ == "__main__":
    # Run synchronous parts
    demo_decorators()
