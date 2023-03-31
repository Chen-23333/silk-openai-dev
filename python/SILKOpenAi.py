#-*- coding: UTF-8 -*-

import json
import requests

config = {}
with open("config.txt","r") as f:
    config = json.loads(f.read())

sk = config["sk"]
message = input("message: ")
url = config["url_host"] + "/v1/chat/completions"

post_data = {
  	"model": "gpt-3.5-turbo",
  	"messages": [{"role": "user", "content": message}]
}
headers = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer " + sk
}

response = requests.post(url, headers = headers, data = json.dumps(post_data))
responseDict = json.loads(response.content)
print('\n')
print(responseDict["choices"][0]["message"]["content"])
