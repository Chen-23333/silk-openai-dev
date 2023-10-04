#-*- coding: UTF-8 -*-

import yaml
import json
import requests
import os
import subprocess

# 通过 subprocess 执行 shell 命令，获取 git 仓库的根目录
command = ['git', 'rev-parse', '--show-toplevel']
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, error = process.communicate()
git_root = output.decode().strip()

# 通过 curl 请求 openai 示例
config_path = os.path.join(git_root, "openai-api", "config.yaml")
config = {}
with open(config_path,"r") as f:
    config = yaml.safe_load(f)

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
