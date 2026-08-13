import requests

req = requests.get("https://www.lipsum.com")

print(req.content)
