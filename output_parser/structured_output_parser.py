from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Step 1: Initialize the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    temperature=0.7,
    max_new_tokens=100
)
model = ChatHuggingFace(llm=llm)

# Step 2: Define the output structure
schema = [
    ResponseSchema(name="name", description="Name of a fictional person"),
    ResponseSchema(name="age", description="Age of the person"),
    ResponseSchema(name="city", description="City where the person lives"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

# Step 3: Create the prompt template with format instructions
template = PromptTemplate(
    template="Give me name, age, and city of a fictional person. {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Step 4: Format the prompt
prompt_text = template.format()
print("📝 Prompt:\n", prompt_text)

# Step 5: Get the response
response = model.invoke(prompt_text)
print("\n📨 Raw Response:\n", response.content)

# Step 6: Parse the structured output
try:
    parsed = parser.parse(response.content)
    print("\n✅ Parsed Output:\n", parsed)
except Exception as e:
    print("\n❌ Parsing Failed:\n", str(e))
