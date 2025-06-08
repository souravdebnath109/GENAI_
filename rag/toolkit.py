from langchain_core.tools import Tool

def add(a: int, b: int) -> int:
    """add 2 no"""
    return a + b

def multiply(a: int, b: int) -> int:
    """multiply 2 no"""
    return a * b

add_tool = Tool(
    name="add",
    func=add,
    description="add 2 no"
)

multiply_tool = Tool(
    name="multiply",
    func=multiply,
    description="multiply 2 no"
)

class Mathtoolinput:
    def get_tools(self):
        return [add_tool, multiply_tool]

toolkit = Mathtoolinput()
tools = toolkit.get_tools()
for tool in tools:
    print(f"{tool.name} => {tool.description}")