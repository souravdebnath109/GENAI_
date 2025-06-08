from langchain_google_genai import GoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Step 1: Explain input
prompt_explain = PromptTemplate(
    input_variables=["input"],
    template="Explain about {input}.",
)

# Step 2: Summarize explanation
prompt_summarize = PromptTemplate(
    input_variables=["input"],
    template="Summarize the following content:\n\n{input}",
)

# Step 3: Extract keywords from the summary
prompt_keywords = PromptTemplate(
    input_variables=["input"],
    template="Find and list the most relevant keywords from the following text:\n\n{input}",
)

# Model setup
model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key="gemini_api_key",  # ⚠️ Replace with your actual API key securely
)

# Output parser to convert model output into plain string
parser = StrOutputParser()

# Runnable chain
chain = RunnableSequence(
    prompt_explain | model | parser |         # Step 1: Explain
    prompt_summarize | model | parser |      # Step 2: Summarize
    prompt_keywords | model | parser      # Step 3: Extract keywords
)

# Run the chain
output = chain.invoke("US airforce and its navy")
print("🔍 Final Keywords Output:\n", output)
