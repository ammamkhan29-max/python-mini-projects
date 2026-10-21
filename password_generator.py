import secrets
import string

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Password length (minimum 8): "))
    if length < 8:
        print("Choose a length of at least 8 characters.")
    else:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        print("Generated password:", password)
        print("Store it securely; do not share it.")
except ValueError:
    print("Please enter a valid whole number.")
