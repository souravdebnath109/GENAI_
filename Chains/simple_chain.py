from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

# ✅ Correct initialization
model = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="gemini_api_key")

# ✅ Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="Generate a response for the following input: {input_text}"
)

# ✅ Create the RunnableSequence (chain)
chain = prompt_template | model

# ✅ Run the chain
response = chain.invoke({"Tell me about USA and EUROPE which is better for Phd students?"})

# ✅ Print output
print("✅ Final Output:\n", response['text'] if isinstance(response, dict) and 'text' in response else response)