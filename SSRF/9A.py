import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = ["example.com"]

url = input("Enter URL: ")
parsed = urlparse(url)

if parsed.hostname not in ALLOWED_DOMAINS:
    raise Exception("Invalid domain")

response = requests.get(url)
print(response.text)
