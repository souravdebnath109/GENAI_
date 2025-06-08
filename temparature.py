from langchain_google_genai import GoogleGenerativeAI

# Initialize the model with a higher temperature for more creative outputs
model = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="gemini_api_key",
    temperature=1.5
)

# Invoke the model
result = model.invoke("Write a 5-line poem on cricket")

# Output the result
print("AI Response:\n", result)
