import logging


def block_ip(ip):
    logging.info(f"Blocking IP:{ip}")

def mark_safe(ip):
    logging.info(f"Safe IP: {ip}")

def flag_suspicious(ip):
    logging.warning(f"Suspicious IP: {ip}")