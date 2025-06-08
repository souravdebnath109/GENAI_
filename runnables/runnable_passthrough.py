from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Step 1: Define a passthrough
passthrough = RunnablePassthrough()
print(passthrough.invoke("ai"))  # Just testing passthrough

# Step 2: Define prompts
prompt1 = PromptTemplate.from_template("Hello {name}")
prompt2 = PromptTemplate.from_template("Explain in 3 sentences about {name}")

# Step 3: Set up the model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key="gemini_api_key"  # ⚠️ Use env vars for safety
)

parser = StrOutputParser()

# Step 4: Define sequences
greeting_chain = RunnableSequence(passthrough, prompt1, model, parser)
explanation_chain = RunnableSequence(prompt2, model, parser)

# Step 5: Parallel execution of two chains
parallel_chain = RunnableParallel({\
    
    "greeting": greeting_chain,
    "explanation": explanation_chain
})

# Option A: Just run parallel chain
output = parallel_chain.invoke({"name": "AI"})

# Option B (if you want to extend it into a final sequence):
# final_chain = RunnableSequence(parallel_chain, another_runnable_step)
# For now, skip final_chain because only one step was causing the ValueError.

print("✅ Final Output:\n", output)
