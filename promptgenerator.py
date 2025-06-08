from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Define chat prompt template
chat_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful assistant."),
    HumanMessagePromptTemplate.from_template(
        "Please summarize the topic '{topic}' related to the domain '{domain}' in a {style} style and {length} length."
    )
])

# Initialize the model
model = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="gemini_api_key")

# Format the prompt with actual variables
prompt = chat_template.format_messages(
    domain="cricket",
    topic="world cup",
    style="simple",
    length="short"
)

# Invoke the model
result = model.invoke(prompt)

# Output the result
print("AI:", result)
