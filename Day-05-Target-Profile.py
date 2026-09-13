import json


def create_target_profile():
    # Practice / Lab data only
    profile = {
        "username": "lab_user",
        "platform": "GitHub",
        "public_repositories": [
            "security-learning",
            "python-projects",
            "cybersecurity-lab"
        ],
        "skills": [
            "Python",
            "Cybersecurity",
            "Networking"
        ],
        "public_interests": [
            "Cybersecurity",
            "Programming",
            "Technology"
        ]
    }

    return profile


print("===== OSINT Target Profile =====")
print("Practice / Lab Data Only\n")

profile = create_target_profile()

print("===== Target Profile =====")
print(json.dumps(profile, indent=4))

# Save profile as JSON
with open("target_profile.json", "w") as file:
    json.dump(profile, file, indent=4)

print("\nTarget profile saved as: target_profile.json")
print("Profile generation completed.")