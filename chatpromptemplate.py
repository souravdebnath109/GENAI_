from langchain_core.prompts import ChatPromptTemplate

# Define chat prompt template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, expain about  {topic}?")
])

# Format the prompt with actual variables
prompt = chat_template.format_messages(domain="cricket", topic="bangladesh cricket team")

# Print the prompt messages
for message in prompt:
    print(f"{message.type}: {message.content}")
