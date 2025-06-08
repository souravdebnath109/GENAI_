import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Sample documents
docs = [
    Document(page_content="LangChain helps with building LLM-based apps."),
    Document(page_content="FAISS is a library for efficient similarity search."),
    Document(page_content="You can use MMR to get diverse results."),
]

# Step 1: Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Create FAISS vector store
vectorstore = FAISS.from_documents(documents=docs, embedding=embedding_model)

# Step 3: Create retriever with MMR
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"lambda_mult": 0.5, "k": 3}
)

# Step 4: Run query
query = "What is LangChain?"
results = retriever.invoke(query)

# Step 5: Print results
for i, doc in enumerate(results):
    print(f"\n🔍 Result {i+1}:")
    print(doc.page_content)
