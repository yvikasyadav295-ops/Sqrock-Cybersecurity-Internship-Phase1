import re


def extract_emails(text):
    # Email address identify karne ke liye regex pattern
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    emails = re.findall(pattern, text)

    return emails


# Practice / Lab data
sample_text = """
Contact our lab team:
admin@example.com
support@example.com
security@example.com

For training purposes only.
"""


print("===== Email Harvesting Tool =====")
print("Practice/Lab Data Only\n")

emails = extract_emails(sample_text)

print("===== Emails Found =====")

if emails:
    for email in emails:
        print(email)
else:
    print("No email addresses found.")

print("\nTotal Emails Found:", len(emails))
print("\nScan completed.")