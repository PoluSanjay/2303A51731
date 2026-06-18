import requests

# =====================================================================
# Central Assignment Configuration
# Replace these strings with your actual registered student credentials
# =====================================================================
REGISTRATION_DATA = {
    "email": "sanjaypolu3@gmail.com",
    "name": "Polu Sanjay",
    "rollNo": "2303A51731",
    "accessCode": "bDreAq",
    "clientId": "d9cbb699-6a27-44a5-8d59-8b1befa816da",     # <-- Put your real version of this string here
    "clientSecret": "tVJaaaRBSexCrRXeM"                     # <-- Put your real version of this string here
}

BASE_URL = 'http://4.224.186.213/evaluation-service'
_cached_token = None

def get_auth_token():
    """
    Fetches or returns a cached Authorization Token from the evaluation server.
    Caching the token ensures we don't spam the /auth endpoint on every log request.
    """
    global _cached_token
    if _cached_token:
        return _cached_token

    try:
        response = requests.post(f"{BASE_URL}/auth", json=REGISTRATION_DATA)
        response.raise_for_status()
        _cached_token = response.json().get("access_token")
        return _cached_token
    except requests.exceptions.RequestException as e:
        print(f"Authentication failed: {e}")
        raise e

def log_message(stack: str, level: str, package: str, message: str):
    """
    Centralized logging utility. Sends structured log footprints directly to 
    the AffordMed evaluation server endpoint.
    
    Allowed Fields (in lowercase):
    - stack: 'backend', 'frontend'
    - level: 'debug', 'info', 'warn', 'error', 'fatal'
    - package: 'cache', 'controller', 'cron_job', 'db', 'domain', 'handler', etc.
    """
    try:
        token = get_auth_token()
        payload = {
            "stack": stack.lower(),
            "level": level.lower(),
            "package": package.lower(),
            "message": message
        }
        headers = {"Authorization": f"Bearer {token}"}
        
        response = requests.post(f"{BASE_URL}/logs", json=payload, headers=headers)
        response.raise_for_status()
        print(f"[Remote Log Success] LogID: {response.json().get('logID')}")
    except requests.exceptions.RequestException as e:
        print(f"[Remote Log Failed]: {e}")