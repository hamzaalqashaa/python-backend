import time

# ---------------------------
# Decorator to measure execution time
# ---------------------------
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"[TIMER] {func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper


# ---------------------------
# Context Manager for File Handling
# ---------------------------
class FileManager:
    """Custom context manager for safe file handling"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # don't suppress exceptions


# ---------------------------
# Example Function with Timing
# ---------------------------
@measure_time
def slow_function(n):
    """Simulate a slow task (sum of numbers)"""
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.001)  # simulate delay
    return total


# ---------------------------
# Usage
# ---------------------------
if __name__ == "__main__":
    result = slow_function(1000)  # decorated function

    # Write result to file using context manager
    with FileManager("results.txt", "w") as f:
        f.write(f"Final result: {result}\n")
        f.write("Execution complete.\n")
