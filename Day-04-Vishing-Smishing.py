def generate_awareness_script(company, role, pretext):
    print("\n===== VISHING & SMISHING AWARENESS SCRIPT =====")

    print("\n--- Vishing (Phone Call) ---")
    print(f"Caller Role : {role}")
    print(f"Company     : {company}")
    print(f"Pretext     : {pretext}")

    print("\nExample Awareness Scenario:")
    print(f"""
A caller claims to be from {company} IT Support
and says there is an issue with the employee account.

The employee should NOT share:
- Password
- OTP
- PIN
- Banking information
- Other sensitive information

The employee should verify the caller through an
official company contact method.
""")

    print("\n--- Smishing (SMS) ---")

    print(f"""
Example Awareness SMS:

"Your {company} account requires attention.
Please contact the official IT support team
using the company's verified contact details."

Do NOT click unknown links or share sensitive information.
""")

    print("\n===== RED FLAGS =====")
    print("1. Urgent or threatening language")
    print("2. Unknown caller or sender")
    print("3. Request for password or OTP")
    print("4. Suspicious links")
    print("5. Request for sensitive information")

    print("\n===== SAFETY TIPS =====")
    print("1. Do not share passwords or OTPs.")
    print("2. Verify the person's identity.")
    print("3. Use official contact information.")
    print("4. Do not click suspicious links.")
    print("5. Report suspicious calls or messages.")

    print("\nAwareness script generated successfully.")


# Lab / training input
print("===== Vishing & Smishing Awareness Tool =====")

company = input("Enter practice company name: ")
role = input("Enter caller role: ")
pretext = input("Enter example pretext: ")

generate_awareness_script(company, role, pretext)