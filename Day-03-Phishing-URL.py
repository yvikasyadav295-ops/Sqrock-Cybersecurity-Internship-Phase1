from urllib.parse import urlparse


def check_phishing_url(url):
    score = 0
    warnings = []

    parsed = urlparse(url)

    # 1. HTTPS check
    if parsed.scheme != "https":
        score += 1
        warnings.append("URL does not use HTTPS")

    # 2. IP address instead of domain name
    hostname = parsed.hostname

    if hostname:
        parts = hostname.split(".")

        if len(parts) == 4 and all(part.isdigit() for part in parts):
            score += 2
            warnings.append("URL uses an IP address instead of a domain")

    # 3. Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "password",
        "account",
        "update",
        "secure",
        "bank"
    ]

    url_lower = url.lower()

    found_words = []

    for word in suspicious_words:
        if word in url_lower:
            found_words.append(word)

    if found_words:
        score += 1
        warnings.append(
            "Suspicious keywords found: " + ", ".join(found_words)
        )

    # 4. Very long URL
    if len(url) > 100:
        score += 1
        warnings.append("URL is unusually long")

    # 5. @ symbol
    if "@" in url:
        score += 2
        warnings.append("URL contains @ symbol")

    # Result
    if score >= 4:
        risk = "HIGH RISK"
    elif score >= 2:
        risk = "SUSPICIOUS"
    else:
        risk = "LOW RISK"

    print("\n===== Phishing URL Detector =====")
    print("URL:", url)
    print("Risk Score:", score)
    print("Risk Level:", risk)

    print("\n===== Findings =====")

    if warnings:
        for warning in warnings:
            print("- " + warning)
    else:
        print("- No obvious suspicious indicators found.")

    print("\nScan completed.")


# Practice URLs only
url = input("Enter a URL to check: ")

check_phishing_url(url)