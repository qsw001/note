from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tool import calc, explain_code, search_concept
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="doubao-seed-1-6-251015",
    openai_api_key=os.getenv("MY_API_KEY"),
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",
)

agent = create_agent(
    model=llm,
    tools=[calc, explain_code, search_concept],
    system_prompt="""
你是一个开发助手。
用户可能会：
- 让你计算
- 让你解释代码
- 让你解释概念

如果需要工具，请选择合适的工具。
"""
)