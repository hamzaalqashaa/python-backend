def multiplier_generator(base):
    """
    Closure that generates a custom multiplier function.
    If base = 0 → special case: returns the square of the number.
    """
    def multiplier(x):
        if base == 0:  # special case: square
            return x * x
        return base * x
    return multiplier


# Create specific multipliers
doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)  # special case

# Test
print("Doubler of 5:", doubler(5))   # 10
print("Tripler of 5:", tripler(5))   # 15
print("Squarer of 5:", squarer(5))   # 25
