PN = input("Enter your phone number:")
def phone_number(PN):
    if len(PN) == 10 and PN.isdigit():
        return "[REDACTED]"
    if PN.startswith("+84") and PN[1:].isdigit() and len(PN) == 12:
        return "[REDACTED]"
    return PN

print(phone_number(PN))