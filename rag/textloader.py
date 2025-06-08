from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

# Initialize the model
model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key="gemini_api_key"
)

# Prompt template
prompt = PromptTemplate(
    template="Write a summary for the topic:\n\n{topic}",
    input_variables=["topic"]
)

# Output parser
parser = StrOutputParser()

# Load the text manually using UTF-8 encoding
try:
    with open("files/cricket.txt", "r", encoding="utf-8") as f:
        text = f.read()
except UnicodeDecodeError as e:
    print("Error reading file with UTF-8 encoding:", e)
    exit()

# Wrap text into a Document
docs = [Document(page_content=text)]

# Proceed if document is loaded
if not docs:
    print("No documents found.")
else:
    topic_text = docs[0].page_content

    # Chain the prompt, model, and parser
    chain = prompt | model | parser

    # Run the chain
    result = chain.invoke({"topic": topic_text})

    # Print the result
    print("Summary:\n", result)
