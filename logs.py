import re

text = input()
pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\s+(\w+) \d+ --- \[(\w+)\] (?:\w+\.)*(\w+)\s+: (.+)'
logs = re.findall(pattern, text)
formatted_logs = []

for log in logs:
    level = log[0]
    string = log[1]
    resp_class = log[2]
    message = log[3]
    formatted_log = f"\"{level}\",\"{string}\",\"{resp_class}\",\"{message}\""
    formatted_logs.append(formatted_log)

for formatted_log in formatted_logs:
    print(formatted_log)