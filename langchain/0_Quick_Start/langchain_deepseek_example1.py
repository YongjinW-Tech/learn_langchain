"""
    Reference URL: https://python.langchain.com/api_reference/deepseek/index.html
    Additional notes or comments can be added here.
"""

# Setup: Install langchain-deepseek and set environment variable DEEPSEEK_API_KEY.
# pip install -U langchain-deepseek
# export DEEPSEEK_API_KEY="your-api-key"
import os
from langchain_deepseek import ChatDeepSeek

# os.environ["DEEPSEEK_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")  # If need, ensure the API key is set in the environment variables
# os.environ["DEEPSEEK_API_BASE"] = "https://api.deepseek.com/v1"  # If need, set the base URL for DeepSeek API

# Instantiate:
llm = ChatDeepSeek(
    model="deepseek-chat",  # Name of DeepSeek model to use, e.g. “deepseek-chat, deepseek-reasoner”.
    temperature=0,          # Sampling temperature.
    max_tokens=None,        # Max number of tokens to generate.
    timeout=None,           # Timeout for requests.
    max_retries=2,          # Max number of retries for failed requests.
    # api_key="...",        # DeepSeek API key. If not passed in will be read from env var DEEPSEEK_API_KEY.
    # api_base="...",       # Base URL for DeepSeek API. DEFAULT_API_BASE = "https://api.deepseek.com/v1"
    # other params...
)

# Invoke:
messages = [
    ("system", "You are a helpful translator. Please answer me some questions about mathematics"),
    ("human", "Please calculate the result of dividing 1 by 0!"),
]
# Call the model and get the response
ai_msg = llm.invoke(messages)

# Print the full AI message object
print("=== Full AI Message Object ===")
print(ai_msg)
print("=" * 40)  # Add a separator for clarity

# Print usage metadata (e.g., token usage, cost, etc.)
print("=== Usage Metadata ===")
print(ai_msg.usage_metadata)
print("=" * 40)

# Print response metadata (e.g., model details, request ID, etc.)
print("=== Response Metadata ===")
print(ai_msg.response_metadata)
print("=" * 40)

# Print the content of the AI response
print("=== AI Response Content ===")
print(ai_msg.content)
print("=" * 40)

# Stream the response in chunks and print each chunk
# - It will gradually return the generated content (usually by token or chunk), suitable 
# - for handling longer responses or scenarios that require real-time display of results.
print("=== Streaming Response ===")
for chunk in llm.stream(messages):
    print(chunk.text(), end="")
print("\n" + "=" * 40)  # Add a separator after streaming