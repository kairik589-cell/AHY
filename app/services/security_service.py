# Simplified security service (No heavy zxcvbn)
import re

def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 chars).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    crack_time = "Instant"
    if score == 4:
        crack_time = "Years"
    elif score == 3:
        crack_time = "Days"

    return {
        "score": score, # 0-4
        "crack_time_display": crack_time,
        "guesses": 0,
        "feedback": {
            "warning": "Weak password" if score < 3 else "",
            "suggestions": feedback
        }
    }
