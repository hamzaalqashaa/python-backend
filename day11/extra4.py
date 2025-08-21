from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):
    """
    Converts time from one timezone to another.
    Input: time string "YYYY-MM-DD HH:MM:SS"
    """
    fmt = "%Y-%m-%d %H:%M:%S"
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    # Parse input time
    naive_time = datetime.strptime(time_str, fmt)

    # Localize and convert
    localized_time = from_zone.localize(naive_time)
    converted_time = localized_time.astimezone(to_zone)

    return converted_time.strftime(fmt)

# Example
print(convert_timezone("2025-08-17 14:30:00", "US/Eastern", "UTC"))
