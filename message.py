from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Initialize the model
model = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="gemini_api_key")

# Define messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me your questions:")
]

# Invoke the model
result = model.invoke(messages)

# Append AI response to messages
messages.append(AIMessage(content=result))

# Print all messages
for message in messages:
    print(f"{message.__class__.__name__}: {message.content}")
