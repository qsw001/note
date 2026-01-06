from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
import os

#读取环境变量
load_dotenv()
API_KEY = os.getenv("MY_API_KEY")

#定义运行函数
def run(user_text:str) :
    return agent.invoke({
        "messages":[
            {"role":"user","content":user_text},
            {"role":"system","content":"你是一个可爱阳光的小女孩"}
        ]
    })

#初始化豆包大预言模型(使用openai兼容)
llm = ChatOpenAI(
    model="doubao-seed-1-6-251015",
    openai_api_key=API_KEY,
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3"
)

#创建agent

agent = create_agent(
    model=llm
)

#调用函数，输出结果
result = run("解释一下api")
print(result["messages"][-1].content)


