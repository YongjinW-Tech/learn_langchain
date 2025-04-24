"""
# 302.ai API 快速入门示例
# 这个示例展示了如何使用 Python 和 requests 库调用 302.ai 的 API。
# 你需要安装 requests 库，可以使用以下命令安装：
# pip install requests
# 请确保你已经在 https://302.ai 上注册并获取了 API 密钥。
# 你可以在 https://302.ai/docs/api-reference/ 中找到 API 文档。
# 下面的代码示例展示了如何发送一个简单的请求到 302.ai 的聊天 API。
# 你可以根据需要修改请求的参数和内容。
"""

# 下面代码实例是参考“302.AI API文档”提供的Python示例代码，关于相关参数请参考:https://302ai.apifox.cn/api-147522039
import requests
import json

url = "https://api.302.ai/v1/chat/completions"

payload = json.dumps({
   "model": "gpt-4o", # 替换为你想使用的模型
   "temperature": 0.7,
   "max_tokens": 200,
   "messages": [
      {
         "role": "user",
         "content": "请给我的花店起个名，谢谢！"
      }
   ]
})

headers = {
   'Accept': 'application/json',
   'Authorization': 'Bearer sk-itnBECGXmqAzem1QrSFYa9mcd87nYrycxh268DvQpsnBkU4o', # 替换为你的 API 密钥
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# 提取并打印 AI 的回复内容
if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
else:
    print(f"请求失败: {response.status_code}, {response.text}")