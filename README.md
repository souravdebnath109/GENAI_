# 🧠 GenAI-Powered Research Assistant & Tool Suite

This project is a comprehensive Generative AI-powered Research Assistant, built using **LangChain**, **Streamlit**, and integrated with custom tools and APIs. It demonstrates a solid understanding of LLM-based applications, tool development, document parsing, chain workflows, and retrieval-augmented question answering (QA) systems.

---

## 🚀 Features

### 🌐 Research Assistant with LangChain Agent

- Uses LLM Agents to make intelligent decisions and invoke the right tools for answering user queries.
- Streamlit UI for easy interaction.

### 🧑‍💻 Chatbot

- Human-like chat experience powered by **LLMs**
- Context-aware and supports tool use (like weather, search, currency)

### 🧰 Custom Tools Implemented

| Tool | Description |
|------|-------------|
| `get_weather_data` | Gets real-time weather info using OpenWeatherMap API |
| `youtube_transcript_qa` | Extracts YouTube transcripts & answers questions from them |
| `currency_converter_tool` | Converts currency using real-time exchange rate APIs |

---

## 🔗 Chains Implemented

| Chain Type        | Usage                                    |
|-------------------|-------------------------------------------|
| `SimpleChain`     | Basic input-output model                 |
| `SequentialChain` | Passes output of one chain to another    |
| `ParallelChain`   | Runs multiple chains in parallel         |
| `ConditionalChain`| Executes branches based on input conditions |

---

## 🧩 Output Parsers Explored

- `ChainOutputParser`
- `PydanticOutputParser`
- `StructuredOutputParser`
- `StringOutputParser`
- `JsonOutputParser`

These were used to structure and validate outputs returned by LLMs.

---

## 🔍 Retriever Types Used

| Retriever             | Description                              |
|-----------------------|------------------------------------------|
| `ContextRetriever`    | Fetches context chunks                   |
| `MMR Retriever`       | Maximal Marginal Relevance retriever     |
| `MultiQuery Retriever`| Asks multiple rephrased questions        |
| `VectorStoreRetriever`| Retrieves relevant chunks from vector DB |
| `WikipediaRetriever`  | Gets relevant info from Wikipedia live   |

---

## 📂 Loaders Explored

| Loader            | Purpose                            |
|-------------------|-------------------------------------|
| `WebBaseLoader`   | Loads content from webpages         |
| `PyPDFLoader`     | Parses PDFs                         |
| `PyPDFLazyLoader` | Lazy loading of large PDF documents |

---

## ✂️ Text Splitters Implemented

- `LengthBasedTextSplitter`
- `RecursiveCharacterTextSplitter`

These were used to break large documents into manageable chunks for better retrieval and token handling.

---

## 🔧 Runnables Used

| Runnable             | Role                            |
|----------------------|----------------------------------|
| `RunnableLambda`     | Apply functions to data          |
| `RunnablePassThrough`| No-op runnable                   |
| `RunnableBranch`     | Condition-based routing          |
| `RunnableParallel`   | Run multiple paths concurrently  |
| `PDF Readers`        | Custom logic for reading PDFs    |

---

## 🧾 Prompt Engineering

- `PromptTemplate`: Used to structure dynamic prompts.
- `PromptGenerator`: Created complex prompts for tools and agents.
- Custom ReAct-style templates for agent thought & action cycles.

---

## 📺 Demos

- Streamlit App for Chatbot + Tool Agent
- LLM Assistant answering questions about YouTube videos
- Currency conversion tool
- Live weather info tool using location
- Retrieval-based QA from uploaded PDFs and web articles

---

## 📚 Tech Stack

- `LangChain`
- `Streamlit`
- `OpenAI / Gemini`
- `OpenWeatherMap API`
- `YouTube Transcript API`
- `ExchangeRate API`
- `PDF Parsing Libraries`
- `FAISS / ChromaDB` (for vector storage)

---

## 💡 What I Learned

This project gave me hands-on experience with:

- Building LLM agents that use tools to reason and act
- Chain of thought prompting and output parsing
- Document retrieval using vector DBs and web APIs
- Integrating various Runnables and building modular pipelines
- Constructing real-world AI assistants using GenAI concepts

---

## 🔗 How to Run

1. Clone the repository:
```bash
git clone https://github.com/souravdebnath109/GENAI_.git
cd GENAI_
## ## 🧠 GenAI Learning Hub & Research Assistant Suite

This folder serves as both a learning hub and a tool suite for exploring and applying Generative AI concepts. It contains independently built projects and scripts based on what I've learned about GenAI—including a fully functional LLM-powered Research Assistant using LangChain, Streamlit, and various custom tools. Key concepts include tool integration, document parsing, prompt workflows, and retrieval-augmented QA systems.


## ## 🚀 Features

### 🌐 Research Assistant with LangChain Agent

- Uses LLM Agents to make intelligent decisions and invoke the right tools for answering user queries.
- Streamlit UI for easy interaction.

## ### 🧑‍💻 Chatbot

- Human-like chat experience powered by **LLMs**.
- Context-aware and supports tool use (like weather, search, currency).
## ### 🧰 Custom Tools Implemented

| Tool | Description |
|------|-------------|
| `get_weather_data` | Gets real-time weather info using OpenWeatherMap API 
| `youtube_transcript_qa` | Extracts YouTube transcripts & answers questions from them 
| `currency_converter_tool` | Converts currency using real-time exchange rate APIs 
## 🔗 Chains Implemented
| Chain Type | Usage |
|------------|-------|
| `SimpleChain` | Basic input-output model |
| `SequentialChain` | Passes output of one chain to another 
| `ParallelChain` | Runs multiple chains in parallel 
| `ConditionalChain` | Executes branches based on input conditions 
## ## 🧩 Output Parsers Explored

- `ChainOutputParser`
- `PydanticOutputParser`
- `StructuredOutputParser`
- `StringOutputParser`
- `JsonOutputParser`

These were used to structure and validate outputs returned by LLMs.


## ## 🔍 Retriever Types Used

| Retriever | Description |
|-----------|-------------|
| `ContextRetriever` | Fetches context chunks |
| `MMR Retriever` | Maximal Marginal Relevance retriever |
| `MultiQuery Retriever` | Asks multiple rephrased questions |
| `VectorStoreRetriever` | Retrieves relevant chunks from vector DB |
| `WikipediaRetriever` | Gets relevant info from Wikipedia live |

##   📂 Loaders Explored

| Loader | Purpose |
|--------|---------|
| `WebBaseLoader` | Loads content from webpages |
| `PyPDFLoader` | Parses PDFs |
| `PyPDFLazyLoader` | Lazy loading of large PDF documents |
## ✂️ Text Splitters Implemented

- `LengthBasedTextSplitter`
- `RecursiveCharacterTextSplitter`

These were used to break large documents into manageable chunks for better retrieval and token handling.

## 🔧 Runnables Used

| Runnable | Role |
|----------|------|
| `RunnableLambda` | Apply functions to data |
| `RunnablePassThrough` | No-op runnable |
| `RunnableBranch` | Condition-based routing |
| `RunnableParallel` | Run multiple paths concurrently |
| `PDF Readers` | Custom logic for reading PDFs |
##  🧾 Prompt Engineering

 - `PromptTemplate`: Used to structure dynamic prompts.
- `PromptGenerator`: Created complex prompts for tools and agents.
- Custom ReAct-style templates for agent thought & action cycles.
## 📺 Demos

- Streamlit App for Chatbot + Tool Agent
- LLM Assistant answering questions about YouTube videos
- Currency conversion tool
- Live weather info tool using location
- Retrieval-based QA from uploaded PDFs and web articles


##   📚 Tech Stack

- `LangChain`
- `Streamlit`
- `OpenAI / Gemini`
- `OpenWeatherMap API`
- `YouTube Transcript API`
- `ExchangeRate API`
- `PDF Parsing Libraries`
- `FAISS / ChromaDB` (for vector storage)
## 💡 What I Learned

This project gave me hands-on experience with:
- Building LLM agents that use tools to reason and act.
- Chain of thought prompting and output parsing.
- Document retrieval using vector DBs and web APIs.
- Integrating various Runnables and building modular pipelines.
- Constructing real-world AI assistants using GenAI concepts.

## 🔗 How to Run
1. Clone the repository
```bash
git clone https://github.com/souravdebnath109/GENAI_.git
## 🤝 Credits

Inspired by YouTube course on GenAI + LangChain
playlist link:
https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0

APIs: OpenWeatherMap, ExchangeRate.host, YouTube Transcript

LangChain documentation & community tools
## 📬 Contact
https://www.linkedin.com/in/sourav-debnath-b4a80a313/

https://github.com/souravdebnath109


## 📌 License


Let me know if you'd like help customizing:


Just paste your repo link or structure, and I’ll guide you further!
## Screenshots

![Screenshot 2025-06-08 172310](https://github.com/user-attachments/assets/5f565ada-6380-46b7-98af-4b64b2d8af54)
![Screenshot 2025-06-08 172623](https://github.com/user-attachments/assets/ee347d68-1bc0-4ffc-b086-e53214eba274)
![Screenshot 2025-06-08 172710](https://github.com/user-attachments/assets/067c069d-dda9-4a36-9769-143bbb3ae52d)
![Screenshot 2025-06-08 172837](https://github.com/user-attachments/assets/f9d7d3be-d6b9-475c-9512-41eba5a5dc75)
![Screenshot 2025-06-08 173417](https://github.com/user-attachments/assets/ccdee331-24d0-4508-9dcd-8c779e7eaca5)
![Screenshot 2025-06-08 173531](https://github.com/user-attachments/assets/ce5d0c1f-e570-420c-89ed-0961fe6f4910)
![Screenshot 2025-06-08 173725](https://github.com/user-attachments/assets/3bac8992-67c8-4aa5-bc7c-b0e2d6fed155)
![Screenshot 2025-06-08 173811](https://github.com/user-attachments/assets/10297dff-693f-4e22-af36-90187989c42f)
![Screenshot 2025-06-08 173911](https://github.com/user-attachments/assets/8f7903e1-bd7d-4de9-9f30-42458c40337f)
![Screenshot 2025-06-08 174220](https://github.com/user-attachments/assets/ba031562-d851-4bca-a2dd-15d2f863ac66)
![Screenshot 2025-06-08 175236](https://github.com/user-attachments/assets/02356b3e-fee6-4f2f-a7e4-55b9fb08e408)
![Screenshot 2025-06-08 175402](https://github.com/user-attachments/assets/a98ae418-f365-4051-b4f8-35e2bd1af3fd)
![Screenshot 2025-06-08 175450](https://github.com/user-attachments/assets/bc7a5a81-9577-45ad-a1ae-36fbdd9c85c6)
![Screenshot 2025-06-08 175534](https://github.com/user-attachments/assets/32a47733-ac7c-42c6-ab49-4cb2eb2b1726)
![Screenshot 2025-06-08 230014](https://github.com/user-attachments/assets/af5b6cc5-1669-41fc-bedc-932fb222ccf3)
![Screenshot 2025-06-08 230024](https://github.com/user-attachments/assets/9cde9632-0baa-488f-a575-36f47268a823)
![Screenshot 2025-06-08 230646](https://github.com/user-attachments/assets/14656cd3-00d0-4009-a92f-852bdc75dd1a)
![Screenshot 2025-06-08 230803](https://github.com/user-attachments/assets/01bd8c2a-98aa-4935-a786-f994c130eacb)
![Screenshot 2025-06-08 230854](https://github.com/user-attachments/assets/3c47d6ca-15f3-40c0-a8ab-5fd7447b7ef1)
![Screenshot 2025-06-08 231003](https://github.com/user-attachments/assets/c903f279-87de-4bf4-af57-48bc1f543d3e)
![Screenshot 2025-06-08 231118](https://github.com/user-attachments/assets/6f14268c-a4dc-49ce-9097-101ab16ee423)
![Screenshot 2025-06-08 231232](https://github.com/user-attachments/assets/27cff1d9-50e7-4ef2-b48f-618d1c967dc0)
![Screenshot 2025-06-08 232750](https://github.com/user-attachments/assets/9263e4d6-7562-41f7-b447-aa07ee7da047)
![Screenshot 2025-06-08 234231](https://github.com/user-attachments/assets/9c2da1f2-afa1-4a7a-bb8e-a24d32683e0d)
![Screenshot 2025-06-08 234409](https://github.com/user-attachments/assets/34ac5259-4bb3-469a-90d9-2de689d49a1f)
![Screenshot 2025-06-08 234550](https://github.com/user-attachments/assets/abb99a4c-e938-4543-a4de-0b56142cffa4)
![Screenshot 2025-06-08 234638](https://github.com/user-attachments/assets/26bb3910-8f13-40cc-a868-3172c88a87d9)
![Screenshot 2025-06-08 235154](https://github.com/user-attachments/assets/9de50d71-c1b3-4992-9de3-db5ee55a4f0e)
![Screenshot 2025-06-09 000359](https://github.com/user-attachments/assets/1f09b843-9ce2-42f6-a9ab-25dddcc6d0cf)
![Screenshot 2025-06-09 000012](https://github.com/user-attachments/assets/74e935f8-3468-44fd-a622-d97825f96805)
![Screenshot 2025-06-09 000123](https://github.com/user-attachments/assets/bb7d13fe-f5ed-4e36-8530-19c7beb7fcbe)
![Screenshot 2025-06-09 000819](https://github.com/user-attachments/assets/66886354-6409-47e9-8064-a88c2ed42fae)
![Screenshot 2025-06-09 001047](https://github.com/user-attachments/assets/c856b59a-cc6b-4bba-b122-bc629d01e2f4)
![Screenshot 2025-06-09 001355](https://github.com/user-attachments/assets/c090d476-472c-4329-a61c-6f5bd05b914a)
![Screenshot 2025-06-09 001355](https://github.com/user-attachments/assets/7858ee1c-b85b-41b7-b28f-316d2fb07c3d)
![Screenshot 2025-06-09 001443](https://github.com/user-attachments/assets/92e5b1c7-c670-477b-9fcd-3cd8ec7d7156)






