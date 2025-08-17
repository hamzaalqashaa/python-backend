# ---------------------------
# Closures
# ---------------------------
def multiplier(factor):
    """Closure that remembers the factor and multiplies numbers by it."""
    def multiply_by(n):
        return n * factor
    return multiply_by

# Create closures
double = multiplier(2)
triple = multiplier(3)


# ---------------------------
# Custom Decorators
# ---------------------------

# A simple logging decorator
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

# A decorator to check positive numbers
def require_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive!")
        return func(x)
    return wrapper


# Example functions using decorators
@log_execution
@require_positive
def square(n):
    """Return the square of a positive number"""
    return n * n


# ---------------------------
# Context Managers
# ---------------------------
class FileManager:
    """Custom context manager for file handling"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"[OPEN] {self.filename}")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"[CLOSE] {self.filename}")
        # Suppress exceptions if handled
        return False


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    # Closures
    print("Double 5:", double(5))   # 10
    print("Triple 4:", triple(4))   # 12

    # Decorators
    print("Square 6:", square(6))
    # print(square(-3))  # Uncomment to see ValueError

    # Context Manager
    with FileManager("example.txt", "w") as f:
        f.write("Hello with custom context manager!\n")
