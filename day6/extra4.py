def analyze_log():
    """Read server.log, count HTTP status codes, and write a summary to report.txt."""
    status_counts = {200: 0, 404: 0, 500: 0}

    try:
        with open("server.log", "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split()

                # Expecting format: [IP] [STATUS] [URL]
                if len(parts) != 3:
                    print(f"⚠ Skipping malformed line {line_number}: {line.strip()}")
                    continue

                _, status_code_str, _ = parts

                try:
                    status_code = int(status_code_str)
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except ValueError:
                    print(f"⚠ Invalid status code on line {line_number}: {status_code_str}")

        # Write summary report
        with open("report.txt", "w", encoding="utf-8") as report:
            report.write(f"Successful (200): {status_counts[200]}\n")
            report.write(f"Not Found (404): {status_counts[404]}\n")
            report.write(f"Server Error (500): {status_counts[500]}\n")

        print("✅ Report generated successfully: report.txt")

    except FileNotFoundError:
        print("❌ server.log file not found.")
    except OSError as e:
        print(f"❌ File error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    analyze_log()
