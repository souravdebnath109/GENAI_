from langchain.schema.runnable import RunnablePassthrough, RunnableLambda, RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Function to count words in the joke
def word_count_fn(joke_text: str) -> int:
    return len(joke_text.split())

# Prompt to generate a joke
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# Model and output parser
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    google_api_key="gemini_api_key"  # ⚠️ Replace with env var in production
)
parser = StrOutputParser()

# Joke generation chain: prompt → model → parser
joke_gen_chain = RunnableSequence(prompt, model, parser)

# Word count chain from joke output
word_count_chain = RunnableLambda(word_count_fn)

# Parallel chain: generate joke once, then reuse for both joke & word count
parallel_chain = RunnableParallel({
    "joke": joke_gen_chain,
    "word_count": RunnableSequence(joke_gen_chain, word_count_chain)
})

# Directly invoke the parallel chain (no need for another sequence)
result = parallel_chain.invoke({"topic": "AI"})

# Display output
print("✅ Final Output:")
print("Joke:", result["joke"])
print("Word Count:", result["word_count"])
