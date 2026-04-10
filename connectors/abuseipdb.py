import requests
import logging
from config import API_KEY


def fetch_ip_data(ip):
    url="https://api.abuseipdb.com/api/v2/check"

    headers = {
        "key" : API_KEY, "Accept": "application/json"
    }


    params = {
        "ipAddress": ip, "maxAgeInDays":90
    }


    response = requests.get(url, headers=headers, params=params, timeout=5)

    if response.status_code == 200:
        return response.json()
    
    else:
        raise Exception(f"API failed with status {response.status_code}")

