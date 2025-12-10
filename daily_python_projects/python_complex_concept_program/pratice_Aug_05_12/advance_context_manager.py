import threading
import time
from typing import Any
from contextlib import contextmanager


# Program 2: Advanced Context Managers and Resource Management
# ============================================================

class ResourceManager:
    """Program 2: Advanced context managers with nested resources and cleanup"""
    def __init__(self):
        self.resources = []
        self.lock = threading.Lock

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

    def get_active_resource(self):
        with self.lock:
            return [r for r in self.resources if r['active']]

# Demo for Program 2
def demo_context_managers():
    rm = ResourceManager()

    print("\n=== Advanced Context Managers Demo ===")
    try:
        with rm.transaction_manager() as txn:
            with rm.managed_resource("Database Connection") as db:
                txn.add_operation("CREATE_TABLE", {"table":"users"})

                with rm.managed_resource("Cache Connection") as cache:
                    txn.add_operation("CACHE_WARM", {"keys": 100})

                    # Simulate some work
                    active = rm.get_active_resource()
                    print(f"Active resources: {len(active)}")

    except Exception as e:
        print(f"Transaction failed: {e}")

if __name__ == "__main__":
    # Run synchronous parts
    demo_context_managers()








