"""
# 参考: https://dash.302.ai/apis/markets
# 参考: https://302ai.apifox.cn/api-147522039
# 302.AI 迁移API指南
# 完全对齐 OpenAI 官方 OpenAI Docs 和 OpenAI API Reference，使用方法完全一致。基于官方 Model Endpoint Compatibility
# 在需要使用OpenAI API的地方，将 api.openai.com 替换为 api.302.ai 即可
替换示例：
    官方 : https://api.openai.com/v1/chat/completions
    我们 : https://api.302.ai/v1/chat/completions
请注意：
    有些App或者网站的 API_Base 为: https://api.openai.com 或 https://api.openai.com/v1
    此时应该替换为: https://api.302.ai 或 https://api.302.ai/v1
代码中调用请注意：
    关于 API KEY 的填写，在Header的Authorization参数里，将管理后台-API KEYS里生成的 API KEY 填在Bearer后面，比如Bearer sk-xxxxxxx
"""

# Ensure the OpenAI SDK is installed before running this script
# Install it using: `pip3 install openai`

import os                   # Import the os module to interact with environment variables
from openai import OpenAI   # Import the OpenAI SDK to interact with the 302.ai API


# 302.ai API configuration
DEEPSEEK_API_URL = "https://api.302.ai/v1/chat/completions"  # Set the base URL for the 302.ai API
DEEPSEEK_API_KEY = os.getenv("AI302_API_KEY")        # Read API key from environment variables
# DEEPSEEK_API_KEY = "<DeepSeek API Key>"            # Replace with your API key, this way is not recommended 

# Create an OpenAI client instance with the API key and base URL
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_API_URL)

# Check if the API key is available; raise an error if not found
if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY not found. Please make sure it is set in the environment variables.")

# Example usage of the 302.ai API
# Send a chat completion request to the 302.ai API
response = client.chat.completions.create(
    model="gpt-4o",  # Specify the model to use (e.g., GPT-4o)
    messages=[
        {"role": "system", "content": "You are a helpful assistant"}, # System message to set the context
        {"role": "user", "content": "请给我的花店起个名，谢谢！"}, # User message to initiate the conversation
    ],
    stream=False  # Set to True if you want to receive streaming responses
)

# Print the content of the first message in the response
print(response.choices[0].message.content)