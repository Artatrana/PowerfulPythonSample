import time
from functools import wraps

# A decorator to track function call count and execution time
def log_execution_time_and_call_count(func):
    # Initialize call count dictionary to track call counts of each function
    call_count = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function name
        func_name = func.__name__

        # Initialize call count if if not present
        call_count[func_name] = call_count.get(func_name,0) + 1

        # Start timing the execution
        start_time = time.time()

        # Call the actual function
        result = func(*args, **kwargs)

        # End timing the execution
        end_time = time.time()

        # Calculate elapsed time
        execution_time = end_time - start_time

        # Log call count and execution time
        print(f"Function '{func_name}' called {call_count[func_name]} times.")
        print(f"Execution time for '{func_name}': {execution_time:.4f} seconds.")
        
        # Return the result of the function
        return result
    return wrapper

# Example usage
@log_execution_time_and_call_count
def compute_sum(n):
    #print("test")
    return sum(range(n))

@log_execution_time_and_call_count
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    compute_sum(1000000)
    compute_sum(2000000)
    factorial(10)
    factorial(15)