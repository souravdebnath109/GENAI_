import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =======================
# STEP 1: Configure Gemini
# =======================
os.environ["GOOGLE_API_KEY"] = "gemini_api_key"  # Replace with your own key

# Initialize Gemini model using LangChain wrapper
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# =======================
# STEP 2: Define Prompts
# =======================
# Prompt 1: Detailed report
template1 = PromptTemplate.from_template("Write a detailed report on {topic}.")

# Prompt 2: Summary of that report
template2 = PromptTemplate.from_template("Summarize the topic:\n{report}\n\nin 5 lines.")

# =======================
# STEP 3: Define Output Parser
# =======================
parser = StrOutputParser()

# =======================
# STEP 4: Create Chains
# =======================
# First chain: topic → detailed report
chain1 = template1 | llm | parser

# Second chain: report → summary
chain2 = template2 | llm | parser

# =======================
# STEP 5: Run the Chains
# =======================
topic_input = {"topic": "KUET"}

# Step 1: Get detailed report
detailed_report = chain1.invoke(topic_input)
print("🔍 Detailed Report on KUET:\n")
print(detailed_report)

# Step 2: Get summary
summary = chain2.invoke({"report": detailed_report})
print("\n📝 5-line Summary of KUET:\n")
print(summary)
