from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the Google Generative AI model
model = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="gemini_api_key")

# Create prompt templates
prompt_template1 = PromptTemplate(
    input_variables=["input_text"],
    template="Generate a detailed response for the following input: {input_text}"
)
prompt_template2 = PromptTemplate(
    input_variables=["detailed_response"],
    template="Generate a 5 line summary for the following input: {detailed_response}"
)
parser = StrOutputParser()

# Chain: detailed response -> summary
chain = (
    prompt_template1
    | model
    | parser
    | (lambda detailed_response: {"detailed_response": detailed_response})
    | prompt_template2
    | model
    | parser
)

result = chain.invoke({"input_text": "Tell me about USA and EUROPE which is better for Phd students?"})
print("✅ Final Output:\n", result)
