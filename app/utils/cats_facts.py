import requests

def fetch_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("fact", "Cats are mysterious creatures!")
    except requests.RequestException:
        return "Could not fetch cat fact at the moment. Try again later."
