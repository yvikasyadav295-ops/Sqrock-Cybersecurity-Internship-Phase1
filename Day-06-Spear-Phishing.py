def create_awareness_email(name, department, topic):

    email = f"""
===== SPEAR PHISHING AWARENESS EMAIL =====

To: {name}
Department: {department}
Subject: Security Awareness - {topic}

Hello {name},

This is a cybersecurity awareness training example.

A suspicious message may try to create urgency or
ask you to provide sensitive information.

For example, an attacker might pretend to be from
an internal department and ask you to verify an account.

RED FLAGS TO WATCH FOR:
- Unexpected requests
- Urgent language
- Unknown or unverified sender
- Requests for passwords or OTPs
- Suspicious links or attachments

SAFETY ACTIONS:
1. Do not share passwords or OTPs.
2. Do not click suspicious links.
3. Verify the request through an official channel.
4. Report suspicious messages to the security team.

This email is for cybersecurity awareness training only.

Regards,
Cybersecurity Awareness Team
"""

    return email


print("===== Spear Phishing Awareness Generator =====")
print("Lab / Training Use Only\n")

name = input("Enter practice recipient name: ")
department = input("Enter practice department: ")
topic = input("Enter awareness topic: ")

result = create_awareness_email(name, department, topic)

print(result)

print("Awareness email generated successfully.")