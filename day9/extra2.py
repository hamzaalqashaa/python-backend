def call_counter(func):
    """
    Decorator that counts how many times a function is called.
    Stores the count as a function attribute: func.call_count
    """
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0  # initialize counter
    return wrapper


# Example usage
@call_counter
def greet(name):
    return f"Hello, {name}!"


# Test calls
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

# Access count directly
print("Final count:", greet.call_count)
