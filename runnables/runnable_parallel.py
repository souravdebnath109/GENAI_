from langchain_core.runnables import RunnableParallel
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda, RunnableMap
from langchain_core.output_parsers import StrOutputParser
prompt1=PromptTemplate(
    input_variables=["input"],
    template=" \n generate a tweet  about {input}. \n ",
)
prompt2=PromptTemplate(
    input_variables=["input"],
    template=" \n generate a linkedin post about {input} \n",
)

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key="gemini_api_key",  # ⚠️ Replace with your actual API key securely
)

parser = StrOutputParser()
# Runnable chain
chain = RunnableParallel({
    "tweet": prompt1 | model | parser,
    "linkedin_post": prompt2 | model | parser,
})

# Run the chain
output = chain.invoke("us airforce")
print(" \n 🔍 Final Output: \n ", output)