def validate_positive(func):
    """
    Decorator that ensures all arguments passed to the function
    are positive numbers. Raises ValueError otherwise.
    """
    def wrapper(*args, **kwargs):
        # Check positional arguments
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Invalid argument {arg}: must be a positive number")

        # Check keyword arguments
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"Invalid argument {key}={value}: must be a positive number")

        return func(*args, **kwargs)
    
    return wrapper


# Example usage
@validate_positive
def add(a, b):
    return a + b

@validate_positive
def area_of_rectangle(length, width):
    return length * width


# Test
print("Sum:", add(5, 10))                  # ✅ works
print("Area:", area_of_rectangle(4, 6))    # ✅ works

# This will raise ValueError
#print(add(-3, 5))      
#print(area_of_rectangle(length=7, width=0))
