import json
from datetime import datetime


print("===== Social Engineering Incident Response =====")
print("Training / Awareness Use Only\n")


# Simulated security alert
alert = {
    "alert_type": "Multiple Failed Login Attempts",
    "source_ip": "10.0.0.50",
    "failed_attempts": 5,
    "severity": "HIGH",
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}


print("===== Security Alert =====")
print("Alert Type:", alert["alert_type"])
print("Source IP:", alert["source_ip"])
print("Failed Attempts:", alert["failed_attempts"])
print("Severity:", alert["severity"])
print("Time:", alert["time"])


# Simulated containment actions
print("\n===== Incident Response Actions =====")

actions = [
    "Alert received and analyzed",
    "Suspicious IP identified",
    "Source IP temporarily blocked (simulation)",
    "Affected account flagged for review",
    "Security team notified (simulation)"
]

for action in actions:
    print("[ACTION]", action)


# Create incident response report
report = {
    "incident": "Social Engineering / Brute-Force Alert",
    "status": "CONTAINMENT SIMULATED",
    "timestamp": alert["time"],
    "alert": alert,
    "actions_taken": actions,
    "recommendation": "Review account activity and investigate the source IP."
}


with open("incident_response_report.json", "w") as file:
    json.dump(report, file, indent=4)


print("\n===== Incident Response Summary =====")
print("Status: CONTAINMENT SIMULATED")
print("Actions Taken:", len(actions))
print("Report saved as: incident_response_report.json")

print("\nIncident response simulation completed.")