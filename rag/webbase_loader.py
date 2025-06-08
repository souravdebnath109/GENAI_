import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load the webpage
url = "https://www.kuet.ac.bd/"
loader = WebBaseLoader(url)
docs = loader.load()
print(f"✅ Pages loaded: {len(docs)}")

# Initialize the model
model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key="gemini_api_key",
    temperature=0.7,
)

# Prompt
prompt = PromptTemplate(
    template="Answer the question: {question}\n\nContext:\n{text}",
    input_variables=["question", "text"],
)

# Output parser (just plain text output for now)
parser = StrOutputParser()

# Chain: prompt → model → parse
chain = prompt | model | parser

# Run the chain
response = chain.invoke({
    "question": "In which year was the university established?",
    "text": docs[0].page_content
})

print("\n📄 Response:\n", response)
