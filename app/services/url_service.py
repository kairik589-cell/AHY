import string
import random

# Global in-memory dictionary
url_db = {}

def shorten_url(original_url: str) -> str:
    # Generate a random 6-character ID
    short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_db[short_id] = original_url
    return short_id

def get_original_url(short_id: str):
    return url_db.get(short_id)
