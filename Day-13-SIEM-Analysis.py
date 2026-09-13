from collections import Counter


print("===== SIEM Log Analysis Tool =====")
print("Social Engineering Attack Detection")
print("Training / Awareness Use Only\n")


# Sample security logs for the lab
logs = [
    {"user": "alice", "event": "LOGIN_SUCCESS", "ip": "192.168.1.10"},
    {"user": "bob", "event": "LOGIN_SUCCESS", "ip": "192.168.1.11"},
    {"user": "alice", "event": "LOGIN_SUCCESS", "ip": "192.168.1.10"},
    {"user": "unknown", "event": "LOGIN_FAILED", "ip": "10.0.0.50"},
    {"user": "unknown", "event": "LOGIN_FAILED", "ip": "10.0.0.50"},
    {"user": "unknown", "event": "LOGIN_FAILED", "ip": "10.0.0.50"},
    {"user": "unknown", "event": "LOGIN_FAILED", "ip": "10.0.0.50"},
    {"user": "unknown", "event": "LOGIN_FAILED", "ip": "10.0.0.50"},
    {"user": "alice", "event": "PASSWORD_CHANGED", "ip": "192.168.1.10"},
]


print("===== Sample Logs =====")

for log in logs:
    print(
        f"User: {log['user']} | "
        f"Event: {log['event']} | "
        f"IP: {log['ip']}"
    )


# Count failed login attempts by IP address
failed_attempts = Counter()

for log in logs:
    if log["event"] == "LOGIN_FAILED":
        failed_attempts[log["ip"]] += 1


print("\n===== Anomaly Detection =====")

alerts = []

for ip, count in failed_attempts.items():

    # Flag an IP if it has more than 3 failed attempts
    if count > 3:
        alert = f"ALERT: {ip} has {count} failed login attempts."
        alerts.append(alert)
        print(alert)


if not alerts:
    print("No suspicious activity detected.")


print("\n===== SIEM Summary =====")
print("Total Logs:", len(logs))
print("Failed Login Attempts:", sum(failed_attempts.values()))
print("Alerts Generated:", len(alerts))

print("\nAnalysis completed.")