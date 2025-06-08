from langchain.tools import BaseTool
from pydantic import BaseModel, Field

# Define the input schema
class MultiplyInput(BaseModel):
    a: int = Field(..., description="first number to multiply")
    b: int = Field(..., description="second number to multiply")

# Define the tool
class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply 2 numbers"
    args_schema: type = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

# Instantiate the tool
multiply_tool = MultiplyTool()

# Invoke the tool 
result = multiply_tool.invoke({'a': 3, 'b': 4})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args_schema.schema())
