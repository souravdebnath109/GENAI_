import google.generativeai as genai
from langchain_core.prompts import PromptTemplate

# Replace with your Gemini API Key
GEMINI_API_KEY = "gemini_api_key"  # Replace this

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
llm = genai.GenerativeModel("gemini-2.0-flash")

def get_response(prompt):
    try:
        response = llm.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Prompt templates (LangChain-style, reused)
template1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="Summarize the topic {topic} in 5 lines.",
    input_variables=["topic"],
)

# Use template1
prompt1 = template1.format(topic="KUET")
result1 = get_response(prompt1)
print("Detailed Report on KUET:\n", result1)

# Use template2
prompt2 = template2.format(topic="KUET")
result2 = get_response(prompt2)
print("\n5-line Summary of KUET:\n", result2)
