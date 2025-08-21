import re
from datetime import datetime
import pytz

def process_log_entry(log_entry):
    """
    Extract email and timestamp, then convert timestamp to multiple timezones.
    """
    email_pattern = r'[\w\.-]+@[\w\.-]+'
    time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

    email = re.search(email_pattern, log_entry)
    timestamp = re.search(time_pattern, log_entry)

    if email and timestamp:
        utc_time = datetime.strptime(timestamp.group(), "%Y-%m-%d %H:%M:%S")
        utc_time = pytz.utc.localize(utc_time)

        local_time = utc_time.astimezone(pytz.timezone("Asia/Amman"))
        ny_time = utc_time.astimezone(pytz.timezone("America/New_York"))

        print(f"User: {email.group()}")
        print(f"UTC Time: {utc_time}")
        print(f"Amman Time: {local_time}")
        print(f"New York Time: {ny_time}")
    else:
        print("Invalid log entry format.")

# Test log entry
log = "User login: john.doe@example.com at 2025-08-17 12:30:00"
process_log_entry(log)
