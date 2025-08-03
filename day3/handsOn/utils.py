def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci_series(n: int) -> list:
    if n <= 0:
        raise ValueError("Number of terms must be greater than 0.")
    series = [0, 1] if n > 1 else [0]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series


def numbers_not_divisible_by_3_or_5(start: int = 1, end: int = 50) -> list:
    return [num for num in range(start, end + 1) if num % 3 != 0 and num % 5 != 0]
