import requests

url = "http://xml.resource.org/public/rfc/txt/rfc793.txt"
response = requests.get(url)

for line in response:
    print(line)
