import hashlib
import uuid

def generate_hash(text: str, algorithm: str = "sha256") -> str:
    if algorithm == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(text.encode()).hexdigest()
    else:
        raise ValueError("Unsupported algorithm. Use 'sha256' or 'sha512'.")

def generate_uuid() -> str:
    return str(uuid.uuid4())

def format_text(text: str, action: str) -> str:
    if action == "uppercase":
        return text.upper()
    elif action == "lowercase":
        return text.lower()
    elif action == "slug":
        return text.lower().replace(" ", "-")
    else:
        raise ValueError("Unsupported action. Use 'uppercase', 'lowercase', or 'slug'.")
