import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from langchain_google_genai import ChatGoogleGenerativeAI

# ✅ Set API keys
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_key"
os.environ["GOOGLE_API_KEY"] = "gemini_api_key"

# ✅ Step 1: Create documents
docs = [
    Document(page_content="LangChain helps with building LLM-based apps."),
    Document(page_content="FAISS is a library for efficient similarity search."),
    Document(page_content="You can use MMR to get diverse results."),
    Document(page_content="llama is a model of facebook"),
    Document(page_content="gemini is a model of google"),
    Document(page_content="chatgpt is a model of openai"),
]

# ✅ Step 2: Embedding model from HuggingFace
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ✅ Step 3: Create vector store
vectorstore = FAISS.from_documents(docs, embedding=embedding_model)

# ✅ Step 4: Base retriever
base_retriever = vectorstore.as_retriever(search_kwargs={'k': 5})

# ✅ Step 5: Use Gemini as LLM for compression
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# ✅ Step 6: Define the compression pipeline
compressor = LLMChainExtractor.from_llm(llm)
compressor_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# ✅ Step 7: Run the query
query = "What is LangChain?"
results = compressor_retriever.invoke(query)

# ✅ Step 8: Print results
for i, doc in enumerate(results):
    print(f"\n📄 Rank {i+1}:")
    print(doc.page_content)
