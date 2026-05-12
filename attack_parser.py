import json

log_file = "cowrie.json"

print("Parsing Honeypot Logs")

try: with open(log_file, "r") as file: for line in file: data = json.loads(line) print(data) except FileNotFoundError: print("Log file not found")
