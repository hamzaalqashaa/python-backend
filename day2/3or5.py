def numbers_not_divisible_by_3_or_5(start: int = 1, end: int = 50) -> list:
    return [num for num in range(start, end + 1) if num % 3 != 0 and num % 5 != 0]


if __name__ == "__main__":
    result = numbers_not_divisible_by_3_or_5()
    print("Numbers from 1 to 50 that are not divisible by 3 or 5:")
    print(result)
