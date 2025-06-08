from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

# Step 1: Define the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=100
)
model = ChatHuggingFace(llm=llm)

# Step 2: Define a Pydantic model for structured output
class Person(BaseModel):
    name: str = Field(..., description="Name of a fictional person")
    age: int = Field(..., description="Age of the person")
    city: str = Field(..., description="City where the person lives")

# Step 3: Use PydanticOutputParser with the model
parser = PydanticOutputParser(pydantic_object=Person)

# Step 4: Create the prompt template
template = PromptTemplate(
    template="Generate name, age, and city of a fictional person. {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Step 5: Format the prompt
prompt_text = template.format()
print("📝 Prompt:\n", prompt_text)

# Step 6: Get the response from the model
response = model.invoke(prompt_text)
print("\n📨 Raw Response:\n", response.content)

# Step 7: Parse the structured output
try:
    parsed = parser.parse(response.content)
    print("\n✅ Parsed Output:\n", parsed)
except Exception as e:
    print("\n❌ Parsing Failed:\n", str(e))
