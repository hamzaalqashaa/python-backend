def get_valid_input():
    """
    Repeatedly ask for a number using the walrus operator
    until the user enters a number greater than 10.
    """
    while (num := int(input("Enter a number greater than 10: "))) <= 10:
        print("That's not greater than 10. Try again.")
    print(f"Valid input received: {num}")


if __name__ == "__main__":
    get_valid_input()
