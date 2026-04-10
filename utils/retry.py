import time
import logging

def retry(func, retries, delay, *args):
    for attempt in range(retries):
        try:
            return func(*args)


        except Exception as e:
            logging.warning(f"Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
            delay *= 2

    return None