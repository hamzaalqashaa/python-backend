import re
from datetime import datetime
import pytz

# ---------- Email Validation Function ----------
def validate_email(email):
    """
    Validate email using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# ---------- Timezone Display Function ----------
def display_current_times():
    """
    Show current time in different timezones.
    """
    utc_now = datetime.now(pytz.utc)
    zones = ["UTC", "Asia/Amman", "America/New_York", "Europe/London"]

    print("\nCurrent Times in Different Timezones:")
    for zone in zones:
        tz = pytz.timezone(zone)
        local_time = utc_now.astimezone(tz)
        print(f"{zone:<15}: {local_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

# ---------- Main Program ----------
if __name__ == "__main__":
    email = input("Enter your email: ").strip()

    if validate_email(email):
        print(f"\n✅ '{email}' is a valid email address.")
    else:
        print(f"\n❌ '{email}' is NOT a valid email address.")

    # Display timezones
    display_current_times()
