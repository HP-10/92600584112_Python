import re

text = "My phone number is 9876543210"

pattern = r"\d{10}"

match = re.search(pattern, text)

print("Text:", text)

if match:
    print("Pattern Matched")
    print("Phone Number:", match.group())
else:
    print("Pattern Not Matched")