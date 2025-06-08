import os
from langchain_community.document_loaders import PDFMinerLoader  # More stable than PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace,HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS

from langchain.prompts import PromptTemplate

# ✅ Set Hugging Face token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_key"

# ✅ Load PDF using PDFMinerLoader for better reliability
loader = PDFMinerLoader("data/Skin_Cancer_Detection_Using_Combined_Decision_of_Deep_Learners.pdf")
pdf_path = loader.file_path
documents = loader.load()

# ✅ Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# ...existing code...

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding_model)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

query = "What are the main topics of the document?"
retrieved_docs = retriever.invoke(query)
retrieved_docs_text = "\n\n".join([doc.page_content for doc in retrieved_docs])

prompt_template = PromptTemplate(
    template="Answer the question based on the following context:\n\n{context}\n\nQuestion: {question}\nAnswer:",
    input_variables=["context", "question"]
)

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=256
)
model = ChatHuggingFace(llm=llm)

formatted_prompt = prompt_template.format(context=retrieved_docs_text, question=query)
answer = model.invoke(formatted_prompt)
print(os.path.basename(pdf_path), "loaded successfully.")

print("=======main topics of the document=======")
print("✅ Answer:", answer.content)
