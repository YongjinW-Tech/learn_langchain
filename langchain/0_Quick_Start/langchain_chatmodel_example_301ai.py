import os
from langchain_openai.llms import OpenAI  # Import OpenAI for text-based models
from langchain_openai.chat_models import ChatOpenAI  # Import ChatOpenAI for chat-based models
from langchain.schema import HumanMessage, SystemMessage  # Import message schema for chat models

# Set the 302AI API key and base URL
os.environ["OPENAI_API_KEY"] = os.getenv("AI302_API_KEY")  # Ensure the API key is set in the environment variables
os.environ["OPENAI_API_BASE"] = "https://api.302.ai/v1/chat/completions"  # Set the base URL for 302AI API
# Check if the API key is available; raise an error if not found

# --- Example 2: Call Chat Model ---
print("\nCalling Chat Model...")
chat = ChatOpenAI(
    model="gpt-4o",  # Replace with the appropriate 302AI chat model
    temperature=0.8,  # Control the randomness of the output
    max_tokens=60,  # Limit the number of tokens in the response
)

# Define the conversation messages
messages = [
    SystemMessage(content="You are a great smart assistant"),  # System message to set the assistant's behavior
    HumanMessage(content="What is the value of dividing 1 by 0?"),  # User message to initiate the conversation
]

# Send the messages to the chat model
chat_response = chat.invoke(messages)  # Ensure the input is a list of messages
print("Chat Model Response:\n", chat_response.content)

"""
Tips1:
    - Textmodel 的 API 端点 OPENAI_API_BASE = "https://api.302.ai/v1"
    - Chatmodel 的 API 端点 OPENAI_API_BASE = "https://api.302.ai/v1/chat/completions"(优先使用) 或者 "https://api.302.ai/v1"
Tips2:
    - 请注意调用的模型是不是 Chatmodel
    - Chatmodel 传入 List[Message]
Tips3:
    - The method `BaseLLM.predict` was deprecated in langchain-core 0.1.7 and will be removed in 1.0. 
    - Use :meth:`~invoke` instead.
"""