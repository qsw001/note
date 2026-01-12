from langchain.tools import tool

@tool
def calc(expression: str) -> str:
    """用于计算数学表达式：例如1+2=3"""
    try:
        result = eval(expression)
        return f"计算的结果是{result}"
    except Exception as e:
        return f"计算错误: {e}"
    
@tool
def explain_code(code: str) -> str:
    """
    解释一小段代码
    """
    return f"这段代码的作用是：\n{code}\n\n（示例解释，你可以后续换成更详细的）"


@tool
def search_concept(concept: str) -> str:
    """
    解释一个编程/计算机概念
    """
    return f"{concept} 是一个常见的计算机概念，用于……（示例）"
