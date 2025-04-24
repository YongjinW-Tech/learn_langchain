"""
# PromptTemplate 使用

`PromptTemplate` 是 LangChain 中用于定义和格式化提示模板的核心类。
它支持动态变量替换、类型约束和部分变量预填充等功能。

通过多个示例，展示如何使用 `PromptTemplate` 创建和管理提示模板。

Ref: https://python.langchain.com/api_reference/core/prompts.html
Ref: https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html
"""

from langchain_core.prompts import PromptTemplate

# ============================
# 示例 1: 使用 from_template 快速创建模板
# ============================
"""
from_template 是创建 PromptTemplate 的推荐方式。
它会自动从模板字符串中提取变量名称而无需刻意指定，并生成一个 PromptTemplate 对象。
适用于简单的模板场景。
"""
prompt = PromptTemplate.from_template("Hello {name}, are you ready to {activity}?")
formatted_prompt = prompt.format(name="Alice", activity="start your journey")

print("Example 1: Using from_template")
print(prompt)  # 输出模板的详细信息
print(formatted_prompt)  # 输出格式化后的字符串
# 预期输出:
# input_variables=['activity', 'name'] input_types={} partial_variables={} template='Hello {name}, are you ready to {activity}?'
# Hello Alice, are you ready to start your journey?

# ============================
# 示例 2: 使用初始化方法创建模板
# ============================
"""
通过初始化方法创建模板时，可以显式指定 input_variables 和模板字符串。
适用于需要更复杂配置的场景。
"""
prompt = PromptTemplate(
    input_variables=["subject", "action"], 
    template="The {subject} will {action}."
)
formatted_prompt = prompt.format(subject="sun", action="rise")

print("\nExample 2: Using initializer")
print(prompt)  # 输出模板的详细信息
print(formatted_prompt)  # 输出格式化后的字符串
# 预期输出input_variables=['action', 'subject'] input_types={} partial_variables={} template='The {subject} will {action}.'
# The sun will rise.

# ============================
# 其他示例 1: 使用初始化方法创建模板，但是显式使用 input_types 和 partial_variables
# ============================
"""
通过 input_types 指定变量类型，通过 partial_variables 提前填充部分变量。
适用于需要类型约束和默认值的场景。
"""
prompt = PromptTemplate(
    input_variables=["subject", "action"], 
    input_types={"subject": str, "action": str},  # 指定变量类型
    partial_variables={"subject": "moon"},  # 提前填充部分变量
    template="The {subject} will {action}."
)
formatted_prompt = prompt.format(action="shine")

print("\nOther Example  1: Using input_types and partial_variables")
print(prompt)  # 输出模板的详细信息
print(formatted_prompt)  # 输出格式化后的字符串
# 预期输出:
# input_variables=['action'] input_types={'subject': <class 'str'>, 'action': <class 'str'>} partial_variables={'subject': 'moon'} template='The {subject} will {action}.'
# The moon will shine.

# ============================
# 其他示例 2: 动态调整 partial_variables 和 input_types
# ============================
"""
创建 PromptTemplate 对象后，可以动态调整 partial_variables 和 input_types。
适用于需要在运行时修改模板行为的场景。
如果使用 from_template 是创建 PromptTemplate 对象，可以通过这种方式进一步修改相关属性
"""
prompt.partial_variables["subject"] = "star"  # 修改 partial_variables 中的 subject
prompt.input_types["action"] = str  # 修改 input_types 中的 action 类型

formatted_prompt_dynamic = prompt.format(action="twinkle")
print("\nOther Example 2: Dynamic adjustment of partial_variables and input_types")
print(formatted_prompt_dynamic)  # 输出动态调整后的结果
# 预期输出:
# The star will twinkle.

# 再次动态调整 partial_variables
prompt.partial_variables["subject"] = "planet"
formatted_prompt_dynamic_2 = prompt.format(action="orbit")
print(formatted_prompt_dynamic_2)  # 输出动态调整后的结果
# 预期输出:
# The planet will orbit.

# ============================
# 示例 3: 使用 from_examples 创建模板
# ============================
"""
from_examples 方法通过提供示例、前缀和后缀，动态生成一个 PromptTemplate。
适用于需要提供上下文示例的场景，例如教 AI 如何回答问题。
"""
examples = [
    "Q: What is the capital of France?\nA: The capital of France is Paris.",
    "Q: What is 2 + 2?\nA: 2 + 2 equals 4.",
    "Q: Who wrote '1984'?\nA: '1984' was written by George Orwell."
]

prefix = "Here are some examples of questions and answers:"
suffix = "Now, please answer the following question: {question}"

prompt = PromptTemplate.from_examples(
    examples=examples,
    suffix=suffix,  # 这里是后缀：示例列表后的附加内容，通常用于设置上下文或背景
    input_variables=["question"],
    example_separator="\n\n", # 示例之间的分隔符，默认为两个换行符 \n\n
    prefix=prefix   # 这里是前缀：示例列表前的附加内容，通常用于设置上下文或背景
)

formatted_prompt = prompt.format(question="What is the largest planet in our solar system?")
print("\nExample 3: Using from_examples")
print(prompt)  # 输出模板的详细信息
print(formatted_prompt)  # 输出格式化后的字符串
# 预期输出:
# Here are some examples of questions and answers:
#
# Q: What is the capital of France?
# A: The capital of France is Paris.
#
# Q: What is 2 + 2?
# A: 2 + 2 equals 4.
#
# Q: Who wrote '1984'?
# A: '1984' was written by George Orwell.
#
# Now, please answer the following question: What is the largest planet in our solar system?