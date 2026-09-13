import platform
import socket
import getpass
import os
from datetime import datetime


def collect_system_info():
    info = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Username": getpass.getuser(),
        "Computer Name": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Python Version": platform.python_version(),
        "Current Folder": os.getcwd()
    }

    return info


print("===== USB Drop Attack Awareness Simulation =====")
print("Benign local simulation only\n")

system_info = collect_system_info()

print("===== System Information =====")

for key, value in system_info.items():
    print(f"{key}: {value}")


# Save information to a local awareness log
with open("usb_simulation_log.txt", "w") as file:

    file.write("===== USB Drop Simulation Log =====\n")
    file.write("Awareness / Training Use Only\n\n")

    for key, value in system_info.items():
        file.write(f"{key}: {value}\n")


print("\nSystem information logged locally.")
print("Log file: usb_simulation_log.txt")
print("\nSimulation completed.")
