class InvalidLengthError(Exception):
    """Raised when the username length is invalid (less than 5 or more than 15 characters)."""
    pass


class InvalidCharacterError(Exception):
    """Raised when the username contains non-alphanumeric characters."""
    pass


def validate_username(username: str):
    """
    Validate a username according to rules:
    - Length must be between 5 and 15 characters.
    - Must contain only alphanumeric characters.
    """
    if len(username) < 5 or len(username) > 15:
        raise InvalidLengthError("Username must be between 5 and 15 characters long.")
    if not username.isalnum():
        raise InvalidCharacterError("Username must contain only alphanumeric characters.")


def register_user():
    """Prompt for a username, validate it, and save it if valid."""
    try:
        username = input("Enter a username: ").strip()
        validate_username(username)

        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(username + "\n")

        print(f"✅ Username '{username}' registered successfully!")

    except InvalidLengthError as e:
        print(f"❌ Invalid Length: {e}")
    except InvalidCharacterError as e:
        print(f"❌ Invalid Characters: {e}")
    except OSError as e:
        print(f"❌ File error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        print("📌 Registration attempt completed.")


if __name__ == "__main__":
    register_user()
