from collections import Counter
from datetime import datetime, timedelta


# ==============================
# RATE LIMIT DETECTOR
# ==============================

def detect_bruteforce_attempts(logs):
    print("\n===== Rate Limit Detector =====")

    attempts = Counter()

    for log in logs:
        username = log["username"]
        attempts[username] += 1

    limit = 5

    for username, count in attempts.items():

        print(f"User: {username}")
        print(f"Login Attempts: {count}")

        if count > limit:
            print("Status: ALERT - Too many login attempts")
        else:
            print("Status: Normal")

        print()


# ==============================
# LOCAL LAB LOGIN SIMULATION
# ==============================

def simulate_login_attempts():

    print("===== Password Attack Awareness Lab =====")
    print("Local simulation only\n")

    logs = []

    username = "lab_user"

    # Simulated failed login attempts
    for i in range(8):

        logs.append({
            "username": username,
            "status": "FAILED",
            "time": datetime.now().strftime("%H:%M:%S")
        })

    print("===== Simulated Login Logs =====")

    for log in logs:
        print(
            f"Time: {log['time']} | "
            f"User: {log['username']} | "
            f"Status: {log['status']}"
        )

    detect_bruteforce_attempts(logs)


# ==============================
# MAIN PROGRAM
# ==============================

simulate_login_attempts()

print("Scan completed.")