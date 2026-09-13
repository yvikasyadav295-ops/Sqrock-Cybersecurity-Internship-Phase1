import re
import socket
import json
from urllib.parse import urlparse
from datetime import datetime


# ==============================
# 1. OSINT / DNS INFORMATION
# ==============================

def osint_scan(domain):
    print("\n===== OSINT Scanner =====")
    print("Domain:", domain)

    try:
        ip = socket.gethostbyname(domain)
        print("IP Address:", ip)
        dns_status = "Completed"
    except Exception:
        ip = "Unavailable"
        dns_status = "Failed"

    return {
        "domain": domain,
        "ip_address": ip,
        "dns_lookup": dns_status
    }


# ==============================
# 2. PHISHING URL SCORER
# ==============================

def phishing_url_check(url):
    print("\n===== Phishing URL Checker =====")

    score = 0
    reasons = []

    parsed = urlparse(url)

    # HTTPS check
    if parsed.scheme != "https":
        score += 1
        reasons.append("URL does not use HTTPS")

    # IP address check
    hostname = parsed.hostname or ""

    if re.fullmatch(r"\d+\.\d+\.\d+\.\d+", hostname):
        score += 2
        reasons.append("URL uses an IP address instead of a domain")

    # Suspicious words
    suspicious_words = [
        "login", "verify", "password",
        "account", "update", "secure", "bank"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append("Suspicious word found: " + word)

    # Long URL
    if len(url) > 100:
        score += 1
        reasons.append("URL is unusually long")

    # @ symbol
    if "@" in url:
        score += 2
        reasons.append("URL contains @ symbol")

    if score >= 4:
        risk = "HIGH RISK"
    elif score >= 2:
        risk = "SUSPICIOUS"
    else:
        risk = "LOW RISK"

    print("URL:", url)
    print("Risk Score:", score)
    print("Risk Level:", risk)

    if reasons:
        print("\nSuspicious Indicators:")
        for reason in reasons:
            print("-", reason)
    else:
        print("No obvious suspicious indicators found.")

    return {
        "url": url,
        "risk_score": score,
        "risk_level": risk,
        "indicators": reasons
    }


# ==============================
# 3. AWARENESS EMAIL TEMPLATE
# ==============================

def awareness_email():
    print("\n===== Awareness Email Template =====")

    recipient = input("Enter practice recipient name: ")
    topic = input("Enter security topic: ")

    email = f"""
Subject: Security Awareness - {topic}

Hello {recipient},

This is a cybersecurity awareness training example.

Please remember:
- Never share passwords or OTPs.
- Check links before clicking.
- Be careful with unexpected emails.
- Verify unusual requests through official channels.

This message is for training purposes only.
"""

    print(email)

    return {
        "recipient": recipient,
        "topic": topic,
        "purpose": "Security awareness training"
    }


# ==============================
# 4. INCIDENT RESPONSE
# ==============================

def incident_response():
    print("\n===== Incident Response Simulation =====")

    source_ip = "10.0.0.50"
    failed_attempts = 5

    print("Alert: Multiple Failed Login Attempts")
    print("Source IP:", source_ip)
    print("Failed Attempts:", failed_attempts)
    print("Severity: HIGH")

    actions = [
        "Alert received and analyzed",
        "Suspicious IP identified",
        "Source IP temporarily blocked (simulation)",
        "Affected account flagged for review",
        "Security team notified (simulation)"
    ]

    print("\nContainment Actions:")

    for action in actions:
        print("[ACTION]", action)

    return {
        "alert": "Multiple Failed Login Attempts",
        "source_ip": source_ip,
        "failed_attempts": failed_attempts,
        "severity": "HIGH",
        "actions": actions
    }


# ==============================
# MAIN FINAL PROJECT
# ==============================

print("==========================================")
print(" SOCIAL ENGINEERING ATTACK CHAIN SIMULATOR")
print("==========================================")
print("Training / Awareness Use Only")

print("\n1. OSINT Scanner")
print("2. Phishing URL Checker")
print("3. Awareness Email Template")
print("4. Incident Response Simulation")
print("5. Run Full Simulation")
print("6. Exit")

choice = input("\nEnter your choice: ")

results = {
    "project": "Social Engineering Attack Chain Simulator",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}


if choice == "1":

    domain = input("Enter practice domain: ")
    results["osint"] = osint_scan(domain)


elif choice == "2":

    url = input("Enter practice URL: ")
    results["phishing_url"] = phishing_url_check(url)


elif choice == "3":

    results["awareness_email"] = awareness_email()


elif choice == "4":

    results["incident_response"] = incident_response()


elif choice == "5":

    print("\n===== FULL SIMULATION =====")

    results["osint"] = osint_scan("example.com")

    results["phishing_url"] = phishing_url_check(
        "http://example.com/login?verify=password"
    )

    results["awareness_email"] = {
        "recipient": "Lab User",
        "topic": "Account Security",
        "purpose": "Security awareness training"
    }

    results["incident_response"] = incident_response()


elif choice == "6":

    print("Exiting program.")


else:

    print("Invalid choice.")


# Save final report

if choice in ["1", "2", "3", "4", "5"]:

    with open("final_project_report.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\n==========================================")
    print("Final report saved as:")
    print("final_project_report.json")
    print("==========================================")

    print("\nFinal Project Completed.")