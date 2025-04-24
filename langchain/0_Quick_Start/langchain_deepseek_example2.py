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
    ("system", "You are a knowledgeable assistant specializing in providing information about universities in China."),
    ("human", "Can you tell me about universities in Shenzhen?"),
    ("assistant", "Shenzhen is home to several well-known universities, including Shenzhen University (SZU), Southern University of Science and Technology (SUSTech), Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen), and Harbin Institute of Technology, Shenzhen (HIT-SZ). These institutions are known for their strong academic programs and research initiatives."),
    ("human", "Can you provide more details about Shenzhen University?"),
    ("assistant", "Shenzhen University, also known as SZU, was established in 1983. It is a comprehensive university located in Nanshan District, Shenzhen. The university is known for its strong programs in engineering, business, and computer science."),
    ("human", "There seems to be another university in Shenzhen called Shenzhen Technology University. Do you know about this school?"),
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


"""
消息角色的作用机制:
    - system: 用于设置助手的行为或角色。
        - system 消息是对话的起点，用于定义 AI 的行为和对话的规则。
        - 它不会直接出现在用户的对话中，但会影响 AI 的回答方式。
    - human: 用于表示用户的输入或问题。
        - human 消息是用户与 AI 之间的交互内容。
        - 它包含用户提出的问题或请求
        - AI 将根据这些消息生成响应。
    - assistant: 用于表示助手的回答或响应。
        - assistant 消息是 AI 对用户输入的回应，提供相关信息或解决方案。
        - AI 的响应以 assistant 消息的形式返回。
        - 在多轮对话中 assistant 消息可以作为上下文的一部分，影响后续的回答。
    - function: 用于表示函数调用的输入参数。
        - function 消息用于传递给 AI 的具体操作指令或数据。 
    ...
temperature:
    - temperature 是生成式语言模型（如 GPT 系列）中的一个重要参数，用于控制生成文本的随机性和多样性。
    - 它决定了模型在生成下一个 token（单词或字符）时，如何从可能的候选 token 中进行采样
    - temperature = 0 
        - 模型会选择概率最高的 token（最确定的答案）。
        - 输出是确定性的，即每次运行相同的输入都会生成完全相同的输出。
        - 适用于需要精确和一致答案的场景，例如数学计算、代码生成或事实性问答。
    - 0 < temperature < 1
        - 增加了一定的随机性，模型会偶尔选择次高概率的 token。
        - 输出内容可能会有轻微变化，适合需要一定创意但仍保持合理性的任务。
    - temperature = 1
        - 默认值，模型会根据概率分布进行采样，生成的内容较为多样。
        - 输出可能会有更多的创意，但也可能出现不太相关或不准确的内容。
    - temperature > 1
        - 极高的随机性，模型会倾向于选择低概率的 token。
        - 输出可能会变得不连贯或不合理，通常不推荐使用。
"""

"""
deepseek-chat 模型的返回结果示例:(ai_msg = llm.invoke(messages) )

content="Yes! **Shenzhen Technology University (SZTU)** is a relatively new public university in Shenzhen, officially established in **2018**. It focuses on **applied sciences, engineering, and technology**, with strong ties to local industries to promote innovation and practical skills.  \n\n### **Key Details:**  \n- **Location:** Pingshan District, Shenzhen (about 45 minutes from downtown).  \n- **Founding:** Started enrollment in 2017, officially approved as a university in 2018.  \n- **Type:** Public, applied technology-oriented university.  \n- **Programs:** Offers undergraduate and master's degrees in fields like:  \n  - **New Energy Vehicles**  \n  - **Intelligent Manufacturing**  \n  - **Robotics & AI**  \n  - **Optics & Photonics**  \n  - **Biomedical Engineering**  \n- **Language:** Some programs are taught in **English or German** (due to collaborations with German universities).  \n- **Industry Connections:** Strong partnerships with **Shenzhen’s tech companies** (e.g., BYD, DJI, Huawei) for internships and R&D.  \n\n### **Unique Features:**  \n✅ **German-style applied education** (collaborates with universities like **Aachen University of Applied Sciences**).  \n✅ **Modern campus** with advanced labs and maker spaces.  \n✅ **High employment rate** due to Shenzhen’s booming tech industry.  \n\n### **Comparison with Shenzhen University (SZU):**  \n- **SZU** is more **comprehensive** (arts, business, medicine, etc.).  \n- **SZTU** is **specialized in engineering & applied tech**, similar to Germany’s **FH (Fachhochschule)** model.  \n\nWould you like details on admissions, rankings, or specific programs?" 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {
                        'completion_tokens': 377, 
                        'prompt_tokens': 188, 
                        'total_tokens': 565, 
                        'completion_tokens_details': None, 
                        'prompt_tokens_details': {
                            'audio_tokens': None, 
                            'cached_tokens': 0
                            }, 
                        'prompt_cache_hit_tokens': 0, 
                        'prompt_cache_miss_tokens': 188
                        }, 
                    'model_name': 'deepseek-chat', 
                    'system_fingerprint': 'fp_3d5141a69a_prod0225', 
                    'id': '9577a84d-d3e5-4673-8f51-3e832c324969', 
                    'finish_reason': 'stop', 
                    'logprobs': None
                    } 
id='run-2fb6200a-6f57-4041-bcb5-1e7932fd15fb-0' 
usage_metadata={'input_tokens': 188, 
                'output_tokens': 377, 
                'total_tokens': 565, 
                'input_token_details': {'cache_read': 0}, 
                'output_token_details': {}
                }
"""