from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models import ChatHuggingFace
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Define response schema
response_schemas = [
    ResponseSchema(name="name", description="Name of a fictional person"),
    ResponseSchema(name="age", description="Age of the person"),
    ResponseSchema(name="city", description="City where the person lives"),
]

# Create parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Create prompt template
template = PromptTemplate(
    template="Give me name, age, and city of a fictional person. {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Use a working Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # ✅ REPLACE WITH A VALID HF MODEL
    temperature=0.7,
    task="text-generation",
    max_new_tokens=100,
)

# Create the chat model
model = ChatHuggingFace(llm=llm)

# Format prompt
prompt_text = template.format()
print("📝 Prompt:\n", prompt_text)

# Invoke model
response = model.invoke(prompt_text)
print("\n📨 Raw Response:\n", response)

# Try parsing
try:
    parsed = parser.parse(response.content)
    print("\n✅ Parsed Response:\n", parsed)
except Exception as e:
    print("\n❌ Could not parse response:\n", str(e))
