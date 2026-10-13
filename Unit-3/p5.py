from datetime import datetime

print("=== Date & Time Module ===")

now = datetime.now()

print("Current Date:", now.date())
print("Current Date (Formatted):", now.strftime("%d-%m-%Y"))
print("Current time:", now.time())
print("Current Time (Formatted):", now.strftime("%H:%M:%S"))
print("Current date and time:", now)
print("Current Date and Time (Formatted):", now.strftime("%d-%m-%Y %H:%M:%S"))
print("Current Year:", now.year)
print("Current Month:", now.month)
print("Current Day:", now.day)
print("Current Hour:", now.hour)
print("Current Minute:", now.minute)
print("Current Second:", now.second)