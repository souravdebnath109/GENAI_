from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

# Initialize models
model1 = GoogleGenerativeAI(
    model="Gemini 2.0 Flash-Lite",
    api_key="gemini_api_key",
    temperature=0.2,
    max_output_tokens=100
)

model2 = GoogleGenerativeAI(
    model="Gemini 2.0 Flash",
    api_key="gemini_api_key",
    temperature=0.2,
    max_output_tokens=100
)

# Prompt templates
prompt1 = PromptTemplate(
    template="generate quiz about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate notes about {topic}",
    input_variables=["topic"]
)

# Merge template needs quiz and notes
prompt3 = PromptTemplate(
    template="Merge the following quiz and notes:\n\nQuiz:\n{quiz}\n\nNotes:\n{notes}",
    input_variables=["quiz", "notes"]
)

# Parser
parser = StrOutputParser()

# Combine in parallel then merge
parallel_chain = (
    RunnableParallel({
        "quiz": prompt1 | model1,
        "notes": prompt2 | model2,
    })
    | prompt3
    | model1
    | parser
)

# Run
result = parallel_chain.invoke({"topic": "Python programming"})

print("✅ Final Output:\n", result)
