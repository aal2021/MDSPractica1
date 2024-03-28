import re

text = input()
matches = re.findall(r'\b([a-z]\.[a-z]+\.\d{4}@alumnos\.urjc\.es|[a-z]+\.[a-z]+@urjc\.es)\b', text)
for match in matches:
    if re.match(r'\b[a-z]\.[a-z]+\.\d{4}@alumnos\.urjc\.es\b', match):
        match = re.match(r'\b([a-z])\.([a-z]+)\.(\d{4})@alumnos\.urjc\.es\b', match)
        initial = match.group(1)
        last_name = match.group(2)
        year = match.group(3)
        print(f"alumno {last_name} matriculado en {year}")
    elif re.match(r'\b[a-z]+\.[a-z]+@urjc\.es\b', match):
        match = re.match(r'\b([a-z]+)\.([a-z]+)@urjc\.es\b', match)
        first_name = match.group(1)
        last_name = match.group(2)
        print(f"profesor {first_name} apellido {last_name}")
