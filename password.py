def check_password(password):
    if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
        return "Password is valid."
    else:
        return "Password is invalid."

password = input("Enter your password: ")

print(check_password(password))
