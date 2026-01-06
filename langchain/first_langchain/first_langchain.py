from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

# 工具函数
@tool
def get_weather(city: str) -> str:
    """模拟获取天气"""
    return f"{city} 今天是晴天"

# 初始化豆包 LLM（使用 OpenAI 兼容接口）
llm = ChatOpenAI(
    model="doubao-seed-1-6-251015",  # 使用豆包的模型名
    openai_api_key=API_KEY,  # 或从环境变量读取
    # 下面这个地址是豆包的 OpenAI 兼容 endpoint
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3"
)

# 创建 Agent
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)

# 运行 Agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "什么是 SF 的天气？"}]}
)

# 输出结果
final_msg = result["messages"][-1].content
print(final_msg)
