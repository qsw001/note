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

responses = llm.batch([
    "今天天气怎么样",
    "你心情怎么样",
    "夸夸我"
])

for response in responses:
    print(response.text)