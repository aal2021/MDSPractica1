import re

text = input()
pattern = r'\b(\d{4})-(\d{2})-(\d{2})\b'
result = re.sub(pattern, r'\3.\2.\1', text)
print(result)