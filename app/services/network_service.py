from user_agents import parse
from typing import Dict, Any

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
