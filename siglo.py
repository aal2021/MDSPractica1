import re

text = input()
pattern = r"\b\d{4}\b"
years = re.findall(pattern, text)

for match in years:
    print(f"{match}")