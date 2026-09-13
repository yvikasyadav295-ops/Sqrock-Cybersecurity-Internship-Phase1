import socket
import json
import urllib.request


# ==============================
# DNS LOOKUP
# ==============================

def dns_lookup(domain):
    try:
        url = f"https://dns.google/resolve?name={domain}&type=A"

        response = urllib.request.urlopen(url, timeout=10)
        data = json.loads(response.read().decode())

        for answer in data.get("Answer", []):
            if answer.get("type") == 1:
                return answer.get("data")

        return None

    except Exception:
        return None


# ==============================
# WHOIS LOOKUP
# ==============================

def whois_lookup(domain):
    try:
        # WHOIS server for .com domains
        whois_server = "whois.verisign-grs.com"

        sock = socket.create_connection(
            (whois_server, 43),
            timeout=10
        )

        sock.sendall((domain + "\r\n").encode())

        data = b""

        while True:
            part = sock.recv(4096)

            if not part:
                break

            data += part

        sock.close()

        text = data.decode(errors="ignore")

        useful_lines = []

        for line in text.splitlines():

            lower = line.lower()

            if (
                lower.startswith("registrar:")
                or lower.startswith("creation date:")
                or lower.startswith("registry expiry date:")
                or lower.startswith("updated date:")
            ):
                useful_lines.append(line.strip())

        if useful_lines:
            return "\n".join(useful_lines)

        return "WHOIS information unavailable"

    except Exception as e:
        return f"WHOIS lookup failed: {e}"


# ==============================
# IP GEOLOCATION
# ==============================

def geolocation_lookup(ip):
    try:
        url = f"https://ipwho.is/{ip}"

        response = urllib.request.urlopen(
            url,
            timeout=10
        )

        data = json.loads(response.read().decode())

        if data.get("success"):

            country = data.get("country", "Unknown")
            region = data.get("region", "Unknown")
            city = data.get("city", "Unknown")

            connection = data.get("connection", {})
            isp = connection.get("isp", "Unknown")

            return (
                f"Country : {country}\n"
                f"Region  : {region}\n"
                f"City    : {city}\n"
                f"ISP     : {isp}"
            )

        return "Geolocation information unavailable"

    except Exception as e:
        return f"Geolocation lookup failed: {e}"


# ==============================
# MAIN OSINT SCANNER
# ==============================

def osint_scan(domain):

    print("\n===== OSINT Scanner =====")
    print(f"Target Domain : {domain}")

    # --------------------------
    # DNS Lookup
    # --------------------------

    ip = dns_lookup(domain)

    if ip:
        print(f"IP Address    : {ip}")
        dns_status = "Completed"
    else:
        print("IP Address    : Unable to retrieve")
        dns_status = "Failed"

    # --------------------------
    # WHOIS
    # --------------------------

    print("\n===== WHOIS Information =====")

    whois = whois_lookup(domain)

    print(whois)

    # --------------------------
    # IP Geolocation
    # --------------------------

    print("\n===== IP Geolocation =====")

    if ip:

        location = geolocation_lookup(ip)

        print(location)

    else:

        location = "Geolocation unavailable because IP was not found."

        print(location)

    # --------------------------
    # Final Report
    # --------------------------

    print("\n===== OSINT Report =====")

    print(f"Domain        : {domain}")
    print(f"DNS Lookup    : {dns_status}")

    if ip:
        print(f"IP Address    : {ip}")
    else:
        print("IP Address    : Not found")

    if (
        "failed" in whois.lower()
        or "unavailable" in whois.lower()
    ):
        whois_status = "Failed"
    else:
        whois_status = "Collected"

    print(f"WHOIS         : {whois_status}")

    if (
        "failed" in location.lower()
        or "unavailable" in location.lower()
    ):
        geo_status = "Failed"
    else:
        geo_status = "Collected"

    print(f"Geolocation   : {geo_status}")

    print("\nScan completed.")


# ==============================
# PRACTICE DOMAIN
# ==============================

osint_scan("example.com")
