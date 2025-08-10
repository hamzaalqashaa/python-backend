def is_palindrome(word: str) -> bool:
    """
    Check if a word is a palindrome (case-insensitive).
    """
    cleaned_word = word.strip().lower()
    return cleaned_word == cleaned_word[::-1] if cleaned_word else False


def find_palindromes(input_file: str, output_file: str):
    """
    Read words from a file, find palindromes, and write them to another file in uppercase.

    Args:
        input_file (str): Path to input file containing words (one per line).
        output_file (str): Path to output file for palindromes.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            words = infile.readlines()

        palindromes = [word.strip().upper() for word in words if is_palindrome(word)]

        with open(output_file, "w", encoding="utf-8") as outfile:
            for p in palindromes:
                outfile.write(p + "\n")

        print(f"Palindromes successfully written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    input_path = "extra1.txt"
    output_path = "extra1_palindromes.txt"
    find_palindromes(input_path, output_path)
