# model

## model是什么？ 

model = 一个可调用的聊天模型接口（chat model interface），可以来自 OpenAI / Anthropic / Gemini / Bedrock / Azure / HuggingFace 等。

model除了可以生成文字外，还可以干以下四件事
- Tool calling(工具调用): 模型可以调用工具，如api等，并返回相应的结果
- structured output(结构化输出): 模型输出可以被限定为schema（Pydantic/TypedDict/JSON Schema）
- multimodality(多模态): 模型输出的可以不只是文字，还有图片，视频等
- reasoning(推理): 模型还具有推理能力

对于新手，我应该优先掌握的是**工具调用**

## model的基本用法

1. 在agent里使用: 通过将llm传入create_agent来使用
``` 
# 先创建llm，再创建agent
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)
```

2. 单独使用: 单独使用则不需要agent

## model的三种调用方式

1. invoke(): 调用的意思，输入为一个字符串或者一组messages，输出为一个AIMessage
2. stream(): 流式输出，边生成边输出，适合前端展示
3. batch(): 一次回答多条问题

## 模型参数

文档列了一组“跨 provider 常见参数”： 

- model：模型名
- api_key：密钥（常用环境变量读）
- temperature：随机性/发散程度（越高越“飘”）
- max_tokens：回复最长 tokens
- timeout：超时时间
- max_retries：失败重试次数
