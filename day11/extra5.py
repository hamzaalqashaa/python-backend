from datetime import datetime
import re

def parse_log_timestamps(log):
    """
    Extracts timestamps in [DD/Mon/YYYY:HH:MM:SS +0000]
    Converts them to 'YYYY-MM-DD HH:MM:SS' in UTC
    """
    pattern = r'\[(\d{2})/([A-Za-z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) \+0000\]'
    months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }

    matches = re.findall(pattern, log)
    results = []

    for day, mon, year, hour, minute, second in matches:
        date_str = f"{year}-{months[mon]}-{day} {hour}:{minute}:{second}"
        # Convert to datetime to ensure proper format
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        results.append(dt.strftime("%Y-%m-%d %H:%M:%S"))

    return results

# Example
log_data = """
192.168.0.1 - - [17/Aug/2025:12:34:56 +0000] "GET /index.html HTTP/1.1" 200
192.168.0.2 - - [18/Aug/2025:14:20:10 +0000] "POST /login HTTP/1.1" 404
"""
print("Extracted Timestamps:", parse_log_timestamps(log_data))
