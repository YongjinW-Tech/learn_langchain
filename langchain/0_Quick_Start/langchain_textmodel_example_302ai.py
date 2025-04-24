import os
from langchain_openai.llms import OpenAI  # Import OpenAI for text-based models

# Set the 302AI API key and base URL
os.environ["OPENAI_API_KEY"] = os.getenv("AI302_API_KEY")  # Ensure the API key is set in the environment variables
os.environ["OPENAI_API_BASE"] = "https://api.302.ai/v1"  # Set the base URL for 302AI API

# --- Example 1: Call Text Model ---
# Uncomment the following code to call a text-based model from 302AI
print("Calling Text Model...")
llm = OpenAI(
    model="gpt-3.5-turbo",  # Replace with the appropriate 302AI text model
    temperature=0.8,  # Control the randomness of the output
    max_tokens=60,  # Limit the number of tokens in the response
)

# # Send a prompt to the text model
text_response = llm.invoke("Good Morning!")  # Ensure the input is a string
print("Text Model Response:", text_response)

"""
Tips1:
    - 302.AI 的 API 文档和 OpenAI 的 API 文档几乎完全一致，使用方法完全一致。
Tips2:
    - Textmodel 的 API 端点 OPENAI_API_BASE = "https://api.302.ai/v1"
    - Chatmodel 的 API 端点 OPENAI_API_BASE = "https://api.302.ai/v1/chat/completions"(优先使用) 或者 "https://api.302.ai/v1"
    - 如果端口不一致会导致404错误(Not Found)，这通常意味着请求的资源不存在
Tips3:
    - The method `BaseLLM.predict` was deprecated in langchain-core 0.1.7 and will be removed in 1.0. 
    - Use :meth:`~invoke` instead.
Tips4:
    - 注意 Textmodel 和 Chatmodel 的区别
    - Textmodel 传入字符串（即需要询问的问题）
    - Chatmodel 传入 List[Message]
    - 注意一下选择的模型是不是 Textmodel 如果输入的不是简单的 Textmodel 会导致一直卡顿而没有输出
    - 确保使用正确的模型和输入格式
"""