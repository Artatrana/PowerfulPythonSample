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


# Program 2: Advanced Context Managers and Resource Management
# ============================================================

class ResourceManager:
    """Program 2: Advanced context managers with nested resources and cleanup"""

    def __init__(self):
        self.resources = []
        self.lock = threading.Lock()

    @contextmanager
    def managed_resource(self, resource_name: str, setup_time: float = 0.1):
        """Context manager that tracks resource lifecycle"""
        print(f"🔧 Setting up {resource_name}")
        time.sleep(setup_time)

        resource = {
            'name': resource_name,
            'created_at': time.time(),
            'active': True
        }

        with self.lock:
            self.resources.append(resource)

        try:
            yield resource
        except Exception as e:
            print(f"❌ Error in {resource_name}: {e}")
            raise
        finally:
            resource['active'] = False
            print(f"🧹 Cleaning up {resource_name}")

    @contextmanager
    def transaction_manager(self):
        """Nested context manager for transaction-like operations"""
        transaction_id = f"txn_{int(time.time() * 1000)}"
        operations = []

        print(f"🚀 Starting transaction {transaction_id}")

        class TransactionContext:
            def add_operation(self, op_name: str, data: Any = None):
                operations.append((op_name, data, time.time()))
                print(f"  ➕ Added operation: {op_name}")

        ctx = TransactionContext()

        try:
            yield ctx
            print(f"✅ Committing transaction {transaction_id} with {len(operations)} operations")
        except Exception as e:
            print(f"🔄 Rolling back transaction {transaction_id}: {e}")
            # Simulate rollback
            for op_name, _, _ in reversed(operations):
                print(f"  ↩️  Rolling back: {op_name}")
            raise

    def get_active_resources(self) -> List[Dict[str, Any]]:
        with self.lock:
            return [r for r in self.resources if r['active']]


# Demo for Program 2
def demo_context_managers():
    rm = ResourceManager()

    print("\n=== Advanced Context Managers Demo ===")

    try:
        with rm.transaction_manager() as txn:
            with rm.managed_resource("Database Connection") as db:
                txn.add_operation("CREATE_TABLE", {"table": "users"})

                with rm.managed_resource("Cache Connection") as cache:
                    txn.add_operation("CACHE_WARM", {"keys": 100})

                    # Simulate some work
                    active = rm.get_active_resources()
                    print(f"Active resources: {len(active)}")

    except Exception as e:
        print(f"Transaction failed: {e}")


# Program 3: Advanced Metaclass and Descriptor Protocol
# =====================================================

class ValidationDescriptor:
    """Program 3: Custom descriptor with validation logic"""

    def __init__(self, validator_func: Callable[[Any], bool], error_msg: str):
        self.validator = validator_func
        self.error_msg = error_msg
        self.data = weakref.WeakKeyDictionary()

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"{self.name}: {self.error_msg}")
        self.data[instance] = value


class ModelMetaclass(type):
    """Metaclass that adds validation and automatic property creation"""

    def __new__(mcs, name, bases, namespace, **kwargs):
        # Add automatic validation tracking
        namespace['_validation_rules'] = {}

        # Process validation decorators
        for key, value in list(namespace.items()):
            if hasattr(value, '_validation_rule'):
                rule = value._validation_rule
                namespace['_validation_rules'][key] = rule
                namespace[key] = ValidationDescriptor(rule['validator'], rule['message'])

        # Add common methods
        def validate_all(self):
            errors = []
            for field_name, _ in self._validation_rules.items():
                try:
                    getattr(self, field_name)  # Trigger validation
                except ValueError as e:
                    errors.append(str(e))
            return errors

        def to_dict(self):
            return {k: getattr(self, k) for k in self._validation_rules.keys()
                    if getattr(self, k) is not None}

        namespace['validate_all'] = validate_all
        namespace['to_dict'] = to_dict

        return super().__new__(mcs, name, bases, namespace)


def validate(validator_func: Callable[[Any], bool], message: str):
    """Decorator for adding validation rules"""

    def decorator(func):
        func._validation_rule = {'validator': validator_func, 'message': message}
        return func

    return decorator


class User(metaclass=ModelMetaclass):
    """Example model using metaclass and descriptors"""

    @validate(lambda x: isinstance(x, str) and len(x) >= 2, "Name must be string with 2+ chars")
    def name(self): pass

    @validate(lambda x: isinstance(x, int) and 0 <= x <= 150, "Age must be between 0-150")
    def age(self): pass

    @validate(lambda x: isinstance(x, str) and '@' in x, "Invalid email format")
    def email(self): pass


# Demo for Program 3
def demo_metaclass():
    print("\n=== Advanced Metaclass & Descriptors Demo ===")

    user = User()
    user.name = "Alice"
    user.age = 25
    user.email = "alice@example.com"

    print(f"Valid user: {user.to_dict()}")
    print(f"Validation errors: {user.validate_all()}")

    try:
        user.age = 200  # Should fail validation
    except ValueError as e:
        print(f"Validation caught: {e}")


# Program 4: Advanced Async Patterns with Concurrency Control
# ===========================================================

class AsyncTaskManager:
    """Program 4: Advanced async patterns with semaphores and task coordination"""

    def __init__(self, max_concurrent: int = 3):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.results = {}
        self.task_queue = asyncio.Queue()
        self.completed_tasks = 0

    async def rate_limited_task(self, task_id: str, work_func: Callable, *args):
        """Execute task with rate limiting using semaphore"""
        async with self.semaphore:
            start_time = time.time()
            print(f"🚀 Starting task {task_id}")

            try:
                # Simulate async work
                if asyncio.iscoroutinefunction(work_func):
                    result = await work_func(*args)
                else:
                    result = work_func(*args)

                execution_time = time.time() - start_time
                self.results[task_id] = {
                    'result': result,
                    'execution_time': execution_time,
                    'status': 'success'
                }
                print(f"✅ Completed task {task_id} in {execution_time:.2f}s")

            except Exception as e:
                self.results[task_id] = {
                    'error': str(e),
                    'status': 'error'
                }
                print(f"❌ Task {task_id} failed: {e}")

            finally:
                self.completed_tasks += 1

    async def batch_execute(self, tasks: List[Dict[str, Any]]):
        """Execute multiple tasks concurrently with progress tracking"""
        total_tasks = len(tasks)

        # Create all tasks
        async_tasks = []
        for task_config in tasks:
            task = asyncio.create_task(
                self.rate_limited_task(
                    task_config['id'],
                    task_config['func'],
                    *task_config.get('args', [])
                )
            )
            async_tasks.append(task)

        # Monitor progress
        progress_task = asyncio.create_task(self._progress_monitor(total_tasks))

        # Wait for all tasks to complete
        await asyncio.gather(*async_tasks, return_exceptions=True)
        progress_task.cancel()

        return self.results

    async def _progress_monitor(self, total_tasks: int):
        """Monitor and report progress"""
        while self.completed_tasks < total_tasks:
            progress = (self.completed_tasks / total_tasks) * 100
            print(f"📊 Progress: {progress:.1f}% ({self.completed_tasks}/{total_tasks})")
            await asyncio.sleep(1)


# Demo functions for async tasks
async def async_calculation(n: int) -> int:
    await asyncio.sleep(0.5)  # Simulate async work
    return n ** 2


def sync_calculation(n: int) -> int:
    time.sleep(0.3)  # Simulate work
    return n * 2


async def demo_async_patterns():
    print("\n=== Advanced Async Patterns Demo ===")

    manager = AsyncTaskManager(max_concurrent=2)

    # Create mixed async and sync tasks
    tasks = [
        {'id': 'async_1', 'func': async_calculation, 'args': [5]},
        {'id': 'sync_1', 'func': sync_calculation, 'args': [10]},
        {'id': 'async_2', 'func': async_calculation, 'args': [3]},
        {'id': 'sync_2', 'func': sync_calculation, 'args': [7]},
    ]

    results = await manager.batch_execute(tasks)

    print("\n📋 Final Results:")
    for task_id, result in results.items():
        if result['status'] == 'success':
            print(f"  {task_id}: {result['result']} (took {result['execution_time']:.2f}s)")
        else:
            print(f"  {task_id}: ERROR - {result['error']}")


# Main execution function
async def main():
    """Run all program demonstrations"""
    print("🐍 Advanced Python Concepts Demonstration")
    print("=" * 50)

    # Run synchronous demos
    demo_decorators()
    demo_context_managers()
    demo_metaclass()

    # Run async demo
    await demo_async_patterns()

    print("\n🎉 All demonstrations completed!")


if __name__ == "__main__":
    # Run synchronous parts
    demo_decorators()
    demo_context_managers()
    demo_metaclass()

    # Run async part
    print("\n" + "=" * 50)
    print("Running async demo...")
    asyncio.run(demo_async_patterns())