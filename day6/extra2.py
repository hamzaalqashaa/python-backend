def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.
    
    Formula: F = (C × 9/5) + 32
    """
    return (celsius * 9 / 5) + 32


def process_temperatures(input_file: str, output_file: str):
    """
    Read temperatures from a file, convert to Fahrenheit, and write formatted results.

    Args:
        input_file (str): Path to the Celsius temperatures file.
        output_file (str): Path to write Fahrenheit conversions.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        with open(output_file, "w", encoding="utf-8") as outfile:
            for line in lines:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                try:
                    celsius = float(line)
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    outfile.write(f"{celsius:.2f}C = {fahrenheit:.2f}F\n")
                except ValueError:
                    outfile.write(f"Invalid temperature: '{line}'\n")

        print(f"Conversion completed. Results saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    input_path = "extra2.txt"
    output_path = "extra2_fahrenheit.txt"
    process_temperatures(input_path, output_path)
