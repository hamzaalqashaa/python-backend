import math
import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_std_dev(numbers):
    return statistics.stdev(numbers)

def square_roots(numbers):
    return [math.sqrt(n) for n in numbers if n >= 0]
