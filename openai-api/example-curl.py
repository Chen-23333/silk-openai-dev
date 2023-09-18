#-*- coding: UTF-8 -*-

import json
import requests

# 通过 curl 请求 openai 示例

config = {}
with open("config.json","r") as f:
    config = json.load(f)

sk = config["sk"]
message = config["content"]
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
