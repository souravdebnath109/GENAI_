from langchain_core.tools import tool

# Define the tool-decorated function
@tool
def multiply(a: int, b: int) -> int:
    "Multiply 2 numbers"
    return a * b

# Call the tool using correct argument keys (as strings)
result = multiply.invoke({"a": 3, "b": 4})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())
