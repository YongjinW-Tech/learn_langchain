"""
# 参考：https://api-docs.deepseek.com/zh-cn/
# DeepSeek API 使用与 OpenAI 兼容的 API 格式，通过修改配置，
# 可以使用 OpenAI SDK 来访问 DeepSeek API，或使用与 OpenAI API 兼容的软件。
* 出于与 OpenAI 兼容考虑，您也可以将 base_url 设置为 https://api.deepseek.com/v1 来使用，但注意，此处 v1 与模型版本无关。
* deepseek-chat 模型已全面升级为 DeepSeek-V3，接口不变。 通过指定 model='deepseek-chat' 即可调用 DeepSeek-V3。
* deepseek-reasoner 是 DeepSeek 最新推出的推理模型 DeepSeek-R1。通过指定 model='deepseek-reasoner'，即可调用 DeepSeek-R1。
* 通过使用 `client.chat.completions.create` 方法，您可以与 DeepSeek API 进行交互。
"""

# Ensure the OpenAI SDK is installed before running this script
# Install it using: `pip3 install openai`

import os                   # Import the os module to interact with environment variables
from openai import OpenAI   # Import the OpenAI SDK to interact with the DeepSeek API


# DeepSeek API configuration
DEEPSEEK_API_URL = "https://api.deepseek.com"        # Replace with the actual DeepSeek API URL
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")     # Read API key from environment variables
# DEEPSEEK_API_KEY = "<DeepSeek API Key>"            # Replace with your API key, this way is not recommended 

# Create OpenAI client instance
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_API_URL)

# Check if the API key is available; raise an error if not found
if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY not found. Please make sure it is set in the environment variables.")

# Example usage of the DeepSeek API
# Send a chat completion request to the DeepSeek API
response = client.chat.completions.create(
    model="deepseek-chat",  # Specify the model to use (DeepSeek-V3 in this case)
    messages=[
        {"role": "system", "content": "You are a helpful assistant"}, # System message to set the context
        {"role": "user", "content": "Hello"}, # User message to initiate the conversation
    ],
    stream=False,  # Set to True if you want to receive streaming responses
    temperature=0.8,
    max_tokens=200
)

print(response)  # Print the entire response for debugging purposes

print("\nResponse choices:", response.choices)  # Print the choices in the response

# Print the content of the first message in the response
print(response.choices[0].message.content)

"""
DeepSeek 提供的模型可以通过以下方式查看:

print(client.models.list())

输出:

SyncPage[Model](
    data=[
        Model(id='deepseek-chat', created=None, object='model', owned_by='deepseek'), 
        Model(id='deepseek-reasoner', created=None, object='model', owned_by='deepseek')
        ], 
    object='list'
)

"""