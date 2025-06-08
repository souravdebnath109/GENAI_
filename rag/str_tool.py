from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

# Define the input schema
class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")

# Define the function
def multiply_func(a: int, b: int) -> int:
    return a * b

# Create the structured tool
multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply 2 numbers",
    args_schema=MultiplyInput
)

# Invoke the tool
result = multiply_tool.invoke({'a': 3, 'b': 4})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)