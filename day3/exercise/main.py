import stats_utils

def get_numbers():
    user_input = input("Enter numbers separated by commas: ")
    return [float(n.strip()) for n in user_input.split(',')]

def main():
    numbers = get_numbers()

    print("\n--- Statistics ---")
    print(f"Mean: {stats_utils.calculate_mean(numbers)}")
    print(f"Median: {stats_utils.calculate_median(numbers)}")
    print(f"Standard Deviation: {stats_utils.calculate_std_dev(numbers)}")

    print("\nSquare Roots:")
    roots = stats_utils.square_roots(numbers)
    for i, r in enumerate(roots):
        print(f"√{numbers[i]} = {r:.2f}")

if __name__ == "__main__":
    main()
