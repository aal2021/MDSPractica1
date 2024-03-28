import re

text = input()
pattern = r'\bE(?:[-\s])?[0-9]{4}[-\s]?[A-Z]{3}\b|\b[0-9]{4}[-\s]?[A-Z]{3}\b'
plates = re.findall(pattern, text)

for match in plates:
    print(match)