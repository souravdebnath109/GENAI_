from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Initialize the model (Replace with your actual API key securely in production)
model = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="gemini_api_key"
)

# Chat history list
chathistory = []

# Prompt template
prompttemplate = PromptTemplate.from_template(
    "You are a helpful research assistant. Answer the following question:\n\n{topic}"
)

# Chat loop
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        break

    if not user_input:
        print("Please enter a valid question.")
        continue

    # Add user message to history
    chathistory.append({"role": "user", "content": user_input})
    
    # Format prompt and get model response
    prompt = prompttemplate.format(topic=user_input)
    result = model.invoke(prompt)
    
    # Print and save AI response
    print("AI:", result)
    chathistory.append({"role": "assistant", "content": result})

# Save chat history to a file
with open("chathistory.txt", "w", encoding="utf-8") as f:
    for entry in chathistory:
        f.write(f"{entry['role']}: {entry['content']}\n")

# Print chat history
print("\nChat History:")
for entry in chathistory:
    print(f"{entry['role']}: {entry['content']}")
