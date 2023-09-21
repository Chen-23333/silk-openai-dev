#-*- coding: UTF-8 -*-

import json
import openai

# 通过 python 库请求 openai 示例

config = {}
with open("config.json","r") as f:
    config = json.load(f)

openai.api_key = config["sk"]
message = config["content"]

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": message}
  ]
)

print('\n')
print(completion.choices[0].message.content)
