from langchain.schema.runnable import RunnablePassthrough, RunnableLambda, RunnableParallel, RunnableSequence, RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Prompt for detailed report
prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"]
)

# Prompt for summary
prompt2 = PromptTemplate(
    template="Write a summary on {topic}.",
    input_variables=["topic"]
)

# Model and output parser
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key="gemini_api_key"
)
parser = StrOutputParser()

# Step 1: Generate report
report_generation_chain = RunnableSequence(prompt1, model, parser)

# Step 2: Generate summary
summary_chain = RunnableSequence(prompt2, model, parser)

# Step 3: Branch logic — if the report has more than 500 words, replace with summary
branch_chain = RunnableBranch(
    (lambda text: len(text.split()) > 500, summary_chain),
    RunnablePassthrough()
)

# Step 4: Chain: generate → check → maybe summarize
final_chain = RunnableSequence(report_generation_chain, branch_chain)

# Step 5: Run and print
result = final_chain.invoke({'topic': 'IELTS exam'})

print("✅ Final Output:\n")
print(result)
