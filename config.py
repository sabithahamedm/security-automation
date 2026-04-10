import os
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    raise Exception("API key not set")


RETRY_COUNT = 3
INITIAL_DELAY = 1
ABUSE_THRESHOLD = 50
SUSPICIOUS_THRESHOLD = 10