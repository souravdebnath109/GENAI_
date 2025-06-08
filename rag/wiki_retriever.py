from langchain_community.retrievers import WikipediaRetriever

# Initialize Wikipedia retriever
retriever = WikipediaRetriever(top_k_results=2, lang='en')

# Define the query
query = "the geographical political history about India and Pakistan from the perspective of China"

# Get relevant documents
doc2 = retriever.invoke(query)

# Print the retrieved content
for i, doc in enumerate(doc2):
    print(f"\n🔍 Result {i+1}:")
    print(f"{doc.page_content}\n")
