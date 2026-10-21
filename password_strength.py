import string

password = input("Enter a password to check: ")

checks = {
    "At least 8 characters": len(password) >= 8,
    "Contains an uppercase letter": any(c.isupper() for c in password),
    "Contains a lowercase letter": any(c.islower() for c in password),
    "Contains a digit": any(c.isdigit() for c in password),
    "Contains a special character": any(c in string.punctuation for c in password),
}

score = sum(checks.values())
for description, passed in checks.items():
    print(f"[{'OK' if passed else 'NO'}] {description}")

if score <= 2:
    label = "Weak"
elif score <= 4:
    label = "Moderate"
else:
    label = "Strong"

print(f"Password strength: {label} ({score}/5 checks passed)")
