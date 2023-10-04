#-*- coding: UTF-8 -*-

import yaml
import openai
import os
import subprocess

# 通过 subprocess 执行 shell 命令，获取 git 仓库的根目录
command = ['git', 'rev-parse', '--show-toplevel']
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, error = process.communicate()
git_root = output.decode().strip()

config_path = os.path.join(git_root, "openai-api", "config.yaml")
config = {}
with open(config_path,"r") as f:
    config = yaml.safe_load(f)

openai.api_key = config["sk"]
message = config["content"]

# 通过 python 库请求 openai 示例
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
)

print('\n')
print(completion.choices[0].message.content)
