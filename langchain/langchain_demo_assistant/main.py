from agent import agent

while True:
    user_input = input(">>> ")
    if user_input == "exit":
        break

    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}
    )

    print(result["messages"][-1].content)