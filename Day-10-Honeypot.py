from datetime import datetime


print("===== Honeypot Link Tracker =====")
print("Baiting & Watering Hole Awareness Simulation")
print("Local Lab Use Only\n")


# Store simulated click events
click_logs = []


def log_click(user):
    event = {
        "user": user,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "SIMULATED CLICK"
    }

    click_logs.append(event)


# Simulate users clicking a suspicious training link
users = ["lab_user_1", "lab_user_2", "lab_user_3"]

for user in users:
    log_click(user)


print("===== Simulated Honeypot Clicks =====")

for event in click_logs:
    print("User   :", event["user"])
    print("Time   :", event["time"])
    print("Status :", event["status"])
    print("-" * 35)


# Save the results locally
with open("honeypot_click_log.txt", "w") as file:
    file.write("===== Honeypot Click Log =====\n")
    file.write("Awareness / Training Use Only\n\n")

    for event in click_logs:
        file.write(f"User   : {event['user']}\n")
        file.write(f"Time   : {event['time']}\n")
        file.write(f"Status : {event['status']}\n")
        file.write("-" * 35 + "\n")


print("\nTotal Simulated Clicks:", len(click_logs))
print("Log file: honeypot_click_log.txt")
print("\nSimulation completed.")
