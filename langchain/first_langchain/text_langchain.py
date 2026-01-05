from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

# 1. 定义工具


@tool
def search_weather(location: str) -> str:
    """搜索指定地点的天气信息

    Args:
        location: 需要查询天气的城市名称，例如 "深圳"
    """
    print(f"tool 搜索天气信息：{location}")
    # 模拟天气查询API
    weather_data = {
        "深圳": "晴天，温度25°C，湿度60%",
        "广州": "多云，温度22°C，湿度70%"
    }
    return weather_data.get(location, f"{location}的天气信息暂时无法获取")


@tool
def calculate_distance(city1: str, city2: str) -> str:
    """计算两个城市之间的距离

    Args:
        city1: 第一个城市的名称
        city2: 第二个城市的名称
    """
    print(f"tool 计算距离：{city1}到{city2}")
    # 模拟距离计算API
    distances = {
        ("深圳", "广州"): "约500公里",
        ("广州", "深圳"): "约500公里"
    }
    return distances.get((city1, city2), f"{city1}到{city2}的距离信息暂时无法获取")


# 2. 创建模型
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
if API_KEY == "" or BASE_URL == "":
    raise ValueError("OPENAI_API_KEY or OPENAI_BASE_URL not set")

model = ChatOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    model_name="doubao-seed-1-6-251015"
)

# 3. 创建ReAct Agent
agent = create_agent(
    model=model,
    tools=[search_weather, calculate_distance],
    system_prompt="你是一个天气助手，可以帮助用户查询天气和计算距离。",
)

# 4. 使用Agent
result = agent.invoke({
    "messages": [HumanMessage(content="城市深圳和城市广州的天气怎么样？距离有多远？")]
})

# 5. 打印结果
print("agent 调用结果：")
print(result["messages"][-1].content)
