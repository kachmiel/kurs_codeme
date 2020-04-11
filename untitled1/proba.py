import json

filename = 'hangman.json'
with open(filename, 'r') as f:
    data = json.load(f)

print(data)