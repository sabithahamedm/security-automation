from config import ABUSE_THRESHOLD,SUSPICIOUS_THRESHOLD

def classify_ip(data):
    abuse_score=data["data"]["abuseConfidenceScore"]


    if abuse_score > ABUSE_THRESHOLD:
        return "malicious"
    
    elif abuse_score>SUSPICIOUS_THRESHOLD:
        return "suspicious"
    
    else:
        return "safe"