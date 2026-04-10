import logging
from connectors.abuseipdb import fetch_ip_data
from utils.retry import retry
from Processing.decision import classify_ip
from Action.response import block_ip, mark_safe, flag_suspicious
from config import RETRY_COUNT, INITIAL_DELAY

logging.basicConfig(level=logging.INFO)

alerts = [
    {"ip": "8.8.8.8"},
    {"ip": "185.220.101.1"}
]

for alert in alerts:
    ip = alert["ip"]

    logging.info(f"Processing IP: {ip}")

    data = retry(fetch_ip_data, RETRY_COUNT, INITIAL_DELAY, ip)

    if data is None:
        logging.error(f"Failed to fetch data for {ip}")
        continue

    result = classify_ip(data)

    if result == "malicious":
        block_ip(ip)

    elif result == "suspicious":
        flag_suspicious(ip)

    else:
        mark_safe(ip)