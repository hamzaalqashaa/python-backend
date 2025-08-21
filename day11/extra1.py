import re

def validate_email(email):
    """
    Validates an email address:
    username@domain.extension
    Username: letters, numbers, dots, underscores, hyphens
    Domain: letters, numbers, hyphens
    Extension: 2–4 letters
    """
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))

# Example
emails = ["user@example.com", "bad-email@", "hello.world@site.org"]
for email in emails:
    print(f"{email} -> {validate_email(email)}")
