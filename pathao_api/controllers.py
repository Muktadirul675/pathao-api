import requests
from functools import wraps

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token")  # â Only look in keyword args

        if not token:
            raise ValueError("Authorization token is required as a keyword argument (token=...)")

        return func(*args, **kwargs)
    return wrapper

def issue_access_token(url:str, args: dict):
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=args, headers=headers)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")

    try:
        data = response.json()  # Parse JSON response
    except ValueError:
        raise ValueError("Response is not valid JSON")

    return data

def issue_refresh_token(url: str, args: dict):
    try:
        response = requests.post(url, json=args)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

    try:
        data = response.json()  # Parse JSON response
    except ValueError:
        raise ValueError("Response is not valid JSON")

    return data

@token_required
def get_city_list(url: str, token: str):
    """
    Send a GET request with Authorization token.

    Args:
        url (str): API endpoint URL.
        token (str): Bearer access token.

    Returns:
        dict or list: Parsed JSON response.
    """
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

    try:
        return response.json()
    except ValueError:
        raise ValueError("Response is not valid JSON")
    
@token_required
def get_zone_list(url: str, token: str):
    """
    Send a GET request with Authorization token.

    Args:
        url (str): API endpoint URL.
        token (str): Bearer access token.

    Returns:
        dict or list: Parsed JSON response.
    """
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

    try:
        return response.json()
    except ValueError:
        raise ValueError("Response is not valid JSON")
    
@token_required
def get_area_list(url: str, token: str):
    """
    Send a GET request with Authorization token.

    Args:
        url (str): API endpoint URL.
        token (str): Bearer access token.

    Returns:
        dict or list: Parsed JSON response.
    """
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

    try:
        return response.json()
    except ValueError:
        raise ValueError("Response is not valid JSON")

@token_required
def get_price_plan(url:str, payload:dict, token:str):
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}") from e

    try:
        return response.json()
    except ValueError:
        raise ValueError("Response is not valid JSON")

@token_required
def get_stores_info(url:str, token:str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")

    try:
        data = response.json()  # Parse JSON response
    except ValueError:
        raise ValueError("Response is not valid JSON")

    return data

