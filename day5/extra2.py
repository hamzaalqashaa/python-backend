def create_student():
    """
    Create and print a student dictionary.
    """
    student = {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Science", "History"]
    }
    print("Student Dictionary:")
    print(student)


def word_frequency(text: str) -> dict:
    """
    Count frequency of each word in a given string.

    Args:
        text (str): Input text.

    Returns:
        dict: Dictionary with word frequencies.
    """
    words = text.split()
    return {word: words.count(word) for word in set(words)}


def squares_dict(n: int) -> dict:
    """
    Create a dictionary of squares from 1 to n using comprehension.

    Args:
        n (int): The maximum number.

    Returns:
        dict: Dictionary of squares.
    """
    return {i: i ** 2 for i in range(1, n + 1)}


if __name__ == "__main__":
    # Task 1: Create and print student dictionary
    create_student()

    # Task 2: Word Frequency Counter
    text = "hello world hello"
    frequencies = word_frequency(text)
    print("\nWord Frequencies:")
    print(frequencies)

    # Task 3: Dictionary Comprehension
    squares = squares_dict(5)
    print("\nDictionary of Squares:")
    print(squares)
