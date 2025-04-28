import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        if re.search(r"[a-z]", password):
            strength += 1
        else:
            feedback.append("Password should include at least one lowercase letter.")
    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*(), etc.).")

    # Determine strength level
    if strength == 5:
        return "Strong password!", feedback
    elif 3 <= strength < 5:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback


if __name__ == "__main__":
    while True:
        user_password = input("Enter a password to check its strength: ")
        result, suggestions = check_password_strength(user_password)
        print(result)
        if suggestions:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        if result == "Strong password!":
            break

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    result, suggestions = check_password_strength(user_password)
    print(result)
    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")