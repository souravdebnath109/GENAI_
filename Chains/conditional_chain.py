from langchain_google_genai import GoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint  # ✅ fixed import
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
import os


# Optional: set API keys as env variables
os.environ["GOOGLE_API_KEY"] = "gemini_api_key"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_key"

# ✅ Define prompt template
prompt = PromptTemplate(
    template="Classify the sentiment of the following feedback as '+' or '-':\n\n{feedback}",
    input_variables=["feedback"]
)

# ✅ GoogleGenerativeAI model (for sentiment classification)
model_google = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    max_output_tokens=100
)

# ✅ Output parser
parser = StrOutputParser()

# ✅ Sentiment classification chain
classifier_chain = prompt | model_google | parser

# ✅ Invoke sentiment classification
input_text = {"feedback": "It was a bad phone call, I am not happy with the service."}
classification_result = classifier_chain.invoke(input_text)

print("✅ Sentiment classification result:", classification_result)

# ✅ Conditional branching based on sentiment
sentiment = classification_result.strip()

if sentiment == "+":
    print("✅ Positive branch triggered. Proceeding with Hugging Face model...")

    # Hugging Face model usage
    hf_model = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="text-generation",
        temperature=0.7,
        max_new_tokens=100
    )

    # Use HF model to generate a response
    hf_result = hf_model.invoke("Provide a motivational message for positive feedback.")
    print("🎯 Hugging Face Output:", hf_result)

elif sentiment == "-":
    print("⚠️ Negative branch triggered. You can handle this differently.")
    # You could invoke a different model or logic here
else:
    print("❓ Unexpected sentiment result:", sentiment)


# Conditional Chain Example: Sentiment Classification and Response Generation
# This example demonstrates a conditional chain that classifies user feedback sentiment
# User Feedback
#    ↓
# PromptTemplate (wrap feedback)
#    ↓
# Gemini Model (sentiment classification)
#    ↓
# Output: '+' or '-'
#    ↓
# [ '+' ] → Use Hugging Face model to generate motivational message
# [ '-' ] → Custom handling (e.g., apology message, alert admin, etc.)
