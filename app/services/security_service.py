from zxcvbn import zxcvbn

def check_password_strength(password: str) -> dict:
    result = zxcvbn(password)

    return {
        "score": result['score'], # 0-4
        "crack_time_display": result['crack_times_display']['offline_slow_hashing_1e4_per_second'],
        "guesses": result['guesses'],
        "feedback": {
            "warning": result['feedback']['warning'],
            "suggestions": result['feedback']['suggestions']
        }
    }
