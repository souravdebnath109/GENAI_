#aita similarity search er basis e

import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document   

# Step 1: Set Google API key
os.environ["GOOGLE_API_KEY"] = "gemini_api_key"  # Replace "xyz" with your actual key

# Step 2: Initialize embedding model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Step 3: Example documents
documents = [
    Document(page_content="Life is about learning, growing, and evolving.", metadata={"source": "philosophy"}),
    Document(page_content="The purpose of life is a central philosophical question.", metadata={"source": "ethics"}),
]

# Step 4: Create vector store
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# Step 5: Convert vector store into retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Step 6: Define query
query = "What is the meaning of life?"

# Step 7: Run retrieval
results = retriever.invoke(query)

# Step 8: Print results
for i, doc in enumerate(results):
    print(f"\n🔍 Result {i+1}:")
    print(doc.page_content)
