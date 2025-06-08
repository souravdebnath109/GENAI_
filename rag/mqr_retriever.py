import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI

# Step 0: Set API keys
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_key"   # Hugging Face
os.environ["GOOGLE_API_KEY"] = "gemini_api_key"             # Gemini (Google GenAI)

# Step 1: Create documents
docs = [
    Document(page_content="LangChain helps with building LLM-based apps."),
    Document(page_content="FAISS is a library for efficient similarity search."),
    Document(page_content="You can use MMR to get diverse results."),
    Document(page_content="llama is a model of facebook"),
    Document(page_content="gemini is a model of google"),
    Document(page_content="chatgpt is a model of openai"),
]

# Step 2: Define Hugging Face embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 3: Create FAISS vectorstore
vectorstore = FAISS.from_documents(docs, embedding=embedding_model)

# Step 4: Create retriever
similarity_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Step 5: Use Gemini (GoogleGenerativeAI) as the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Step 6: MultiQueryRetriever with Gemini
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=similarity_retriever,
    llm=llm
)

# Step 7: Ask query
query = "Which things help to build LLM-based apps?"

# Step 8: Retrieve
multiquery_results = multiquery_retriever.invoke(query)

# Step 9: Print results
for i, doc in enumerate(multiquery_results):
    print(f"\n🔍 Result {i+1}:")
    print(doc.page_content)
