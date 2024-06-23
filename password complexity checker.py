import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on length, presence of uppercase and lowercase letters,
    numbers, and special characters.
    """
    # Criteria
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Initial score
    score = 0
    feedback = []

    # Check length
    if len(password) >= min_length:
        score += 1
    else:
        feedback.append(f"Password should be at least {min_length} characters long.")
    
    # Check uppercase
    if has_upper:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check lowercase
    if has_lower:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check digit
    if has_digit:
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    # Check special character
    if has_special:
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Determine strength
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Feedback message
    if not feedback:
        feedback_message = "Your password is strong."
    else:
        feedback_message = "Your password is weak. " + " ".join(feedback)
    
    return strength, feedback_message

# Example usage
password = input("Enter your password: ")
strength, feedback_message = assess_password_strength(password)
print(f"Password Strength: {strength}")
print(feedback_message)
