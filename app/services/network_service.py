import whois
from user_agents import parse
from typing import Dict, Any

def lookup_whois(domain: str) -> Dict[str, Any]:
    try:
        w = whois.whois(domain)
        # Serialize datetime objects and list to strings for JSON safety
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers,
            "status": w.status,
            "emails": w.emails,
            "org": w.org
        }
    except Exception as e:
        raise Exception(f"Whois lookup failed: {str(e)}")

def parse_user_agent(ua_string: str) -> Dict[str, str]:
    user_agent = parse(ua_string)
    return {
        "browser": f"{user_agent.browser.family} {user_agent.browser.version_string}",
        "os": f"{user_agent.os.family} {user_agent.os.version_string}",
        "device": f"{user_agent.device.family} ({user_agent.device.brand} {user_agent.device.model})",
        "is_mobile": user_agent.is_mobile,
        "is_tablet": user_agent.is_tablet,
        "is_bot": user_agent.is_bot
    }
