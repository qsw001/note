# message

## message的作用

message(没有s)是langchain上下文中的最小单位，

messages则是喂给ai的上下文(context)，也是返回结果的载体，它至少包含三个信息
- role: 谁说的，起什么作用(system,user,assistant,tool)
- content: 给模型看的东西(多模态)
- metadata(元数据): token,id等东西

例如：
```
{
  "role": "user",
  "content": "什么是 SF 的天气？"
}
```

message为一条聊天记录加附带的结构化信息,用message的作用是统一不同的api供应商的格式

## message的传入方式

### 直接传字符串
适合学习测试使用
   `model.invoke("Write a haiku about spring")`

### 传message对象列表

比较langchain的写法
```
[
  SystemMessage(...),
  HumanMessage(...),
  AIMessage(...)
]
```

### 传dict列表
openai chat风格
```
[
  {"role":"system","content":"..."},
  {"role":"user","content":"..."}
]
```

## message type

1. SystemMessage
2. HumanMessage
3. AIMessage:模型输出，注意这里的模型输出不知包括文字输出，还有tool_calls,usage_metadata(token用量),response_metadata（模型厂商返回的其它字段）
4. ToolMessage