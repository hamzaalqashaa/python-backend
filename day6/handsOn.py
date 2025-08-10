def process_file(input_file: str, output_file: str):
    """
    Read a file, process its content, and write to another file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """
    try:
        # Step 1: Read the file
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Step 2: Process the content (example: convert to uppercase)
        processed_content = content.upper()

        # Step 3: Write processed content to another file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(processed_content)

        print(f"Processing complete. Output saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    input_filename = "input.txt"
    output_filename = "output.txt"

    process_file(input_filename, output_filename)
