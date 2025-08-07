def remove_duplicates(words: list) -> set:
    """
    Remove duplicate words using a set.

    Args:
        words (list): A list of words (strings).

    Returns:
        set: A set of unique words.
    """
    return set(words)


def count_word_frequency(words: list) -> dict:
    """
    Count the frequency of each word in a list using a dictionary.

    Args:
        words (list): A list of words (strings).

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    word_count = {}
    for word in words:
        word = word.lower()  # make case-insensitive
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


if __name__ == "__main__":
    # Example input
    text = "apple banana Apple orange banana apple grape"
    words_list = text.split()

    # Remove duplicates using set
    unique_words = remove_duplicates(words_list)
    print("Unique words:", unique_words)

    # Count word frequency
    frequency = count_word_frequency(words_list)
    print("Word frequency:")
    for word, count in frequency.items():
        print(f"{word}: {count}")
