## prompt和message的目的

- 你能用 system prompt 改模型行为，并验证“确实生效”
- 你能解释清楚：messages 是对话历史，不是参数
- 你能用多轮 messages复现“上下文保留/不保留”的差别
- 你能读懂并操作：HumanMessage / AIMessage / SystemMessage（或它们的字典等价物）

首先说说运行agent的代码

```
# 运行 Agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "什么是 SF 的天气？"}]}
)
```

其中的result是agent执行的结果，它是一个包含完整执行记录的字典

result["message"]是一个消息对象列表，一般回答在最后一项，所以我们用result["message"][-1]表示最后一个对象，再加上.content返回内容