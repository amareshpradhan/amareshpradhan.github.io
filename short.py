import requests

url = "https://api.short.io/domains/"

import json
payload = json.dumps({"hideReferer":False,"httpsLinks":False,"hostname":"amare.sh","linkType":"random"})
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "pk_k7XhXQsqCbq8MqaW"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
