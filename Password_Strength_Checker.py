import string

def check_password_strength(password):
    score = 0

    # Sets for checking characters
    lowercase = set(string.ascii_lowercase)
    uppercase = set(string.ascii_uppercase)
    digits = set(string.digits)
    special_chars = set(string.punctuation)

    # Convert password to set for faster checks
    password_set = set(password)

    # Check each condition
    if len(password) >= 8:
        score += 2
    if any(char in lowercase for char in password_set):
        score += 2
    if any(char in uppercase for char in password_set):
        score += 2
    if any(char in digits for char in password_set):
        score += 2
    if any(char in special_chars for char in password_set):
        score += 2

    # Display feedback
    print(f"Password Score: {score}/10")
    if score == 10:
        print("Strength: 🔐 Very Strong")
    elif score >= 8:
        print("Strength: 💪 Strong")
    elif score >= 6:
        print("Strength: 😐 Moderate")
    else:
        print("Strength: ⚠️ Weak - Consider using a stronger password!")

# Example usage
password_input = input("Enter your password: ")
check_password_strength(password_input)
