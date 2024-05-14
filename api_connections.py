import json
import requests


with open("config.json") as f:
    config = json.load(f)

endpoint_url = config["endpoint_url"]
easy_token = config["easy_token"]




url = "https://api.easyinventory.com.br/v1/company?token=20fb7df2-80bd-4b7c-9779-fe9b27d6346a"

payload = {}
headers = {
  'Cookie': 'SRVGROUP=common'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
