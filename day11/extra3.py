from datetime import datetime, timedelta

def time_until_birthday(birthdate_str):
    """
    Calculates time until next birthday.
    Input format: YYYY-MM-DD
    """
    today = datetime.now()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

    # Set next birthday to this year
    next_birthday = birthdate.replace(year=today.year)

    # If birthday already passed this year, move to next year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    time_diff = next_birthday - today
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return days, hours, minutes

# Example
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
days, hours, minutes = time_until_birthday(birthdate_input)
print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes")
