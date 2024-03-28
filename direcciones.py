import re

text = input()
pattern = r'\b(C/|Calle)\s([A-ZÁÉÍÓÚÑÜ][a-zA-ZÁÉÍÓÚÑÜáéíóúñü]*),?\s+?(?:Nº|nº|N|n)?\s?(\d+),\s+?(\d{5})\b'
addresses = re.findall(pattern, text)
formatted_addresses = []

for address in addresses:
    street = address[1]
    number = address[2]
    postal_code = address[3]
    formatted_address = f"{postal_code}-{street}-{number}"
    formatted_addresses.append(formatted_address)

for formatted_address in formatted_addresses:
    print(formatted_address)