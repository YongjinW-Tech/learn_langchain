import os
from openai import OpenAI

DEEPSEEK_API_URL = "https://api.deepseek.com"        # Replace with the actual DeepSeek API URL
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")     # Read API key from environment variables


if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY not found. Please make sure it is set in the environment variables.")

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_API_URL)  # Use the environment variable for the API key
print(client.models.list())

"""
SyncPage[Model](
    data=[
        Model(id='deepseek-chat', created=None, object='model', owned_by='deepseek'), 
        Model(id='deepseek-reasoner', created=None, object='model', owned_by='deepseek')
        ], 
    object='list'
)

"""