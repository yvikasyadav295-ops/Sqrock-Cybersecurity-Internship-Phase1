print("===== Fake Profile Detection Tool =====")
print("Awareness / Training Use Only\n")


def calculate_risk(profile):
    score = 0
    reasons = []

    # Very new account
    if profile["account_age_days"] < 30:
        score += 2
        reasons.append("Very new account")

    # Very few followers
    if profile["followers"] < 20:
        score += 2
        reasons.append("Very few followers")

    # Following many more accounts than followers
    if profile["following"] > profile["followers"] * 5:
        score += 2
        reasons.append("Following many more accounts than followers")

    # Very low profile activity
    if profile["posts"] < 3:
        score += 1
        reasons.append("Very low post activity")

    # No profile picture
    if not profile["profile_picture"]:
        score += 2
        reasons.append("No profile picture")

    return score, reasons


# Sample practice profile
profile = {
    "username": "lab_user",
    "account_age_days": 10,
    "followers": 8,
    "following": 150,
    "posts": 1,
    "profile_picture": False
}


print("===== Profile Details =====")
print("Username:", profile["username"])
print("Account Age:", profile["account_age_days"], "days")
print("Followers:", profile["followers"])
print("Following:", profile["following"])
print("Posts:", profile["posts"])
print("Profile Picture:", "Yes" if profile["profile_picture"] else "No")


score, reasons = calculate_risk(profile)

print("\n===== Detection Results =====")
print("Risk Score:", score)


if score >= 6:
    risk = "HIGH RISK"
elif score >= 3:
    risk = "SUSPICIOUS"
else:
    risk = "LOW RISK"


print("Risk Level:", risk)

print("\n===== Suspicious Indicators =====")

if reasons:
    for reason in reasons:
        print("-", reason)
else:
    print("No obvious suspicious indicators found.")


print("\nNote: This tool uses simple behavioral indicators.")
print("It does not confirm whether a real person is fake.")
print("\nDetection completed.")