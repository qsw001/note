from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

llm = ChatOpenAI(
    model="doubao-seed-1-6-251015",
    openai_api_key=API_KEY,
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3"
)

for chunk in llm.stream("用一句话解释什么是 LangChain"):
    print(chunk.text, end="|", flush=True)
