import re

def check_password(password):
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = length + has_upper + has_lower + has_number + has_special

    if score == 5:
        return "Strong password"
    elif score >= 3:
        return "Good password"
    else:
        return "Weak password"

print("Check how strong your password is:")
password = input("Enter password: ")
print("Password strength:", check_password(password))
