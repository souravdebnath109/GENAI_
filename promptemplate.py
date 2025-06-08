import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Initialize the model
model = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="gemini_api_key")

# Streamlit UI
st.title("🧠 RAT - Research Assistant Tool")

# User inputs
paper_input = st.text_area("Enter your research question or topic:")
style_input = st.selectbox("Select the style or tone:", ["simple", "complex"])
length_input = st.selectbox("Select the length of the summary:", ["Short", "Medium", "Long"])

# Define prompt template
template = PromptTemplate.from_template(
    "You are a research assistant. Your task is to summarize the following research topic in {style} style and {length} length:\n\n{topic}"
)

# Summarize button
if st.button("Summarize"):
    if not paper_input.strip():
        st.warning("Please enter a topic to summarize.")
    else:
        # Format the prompt
        prompt = template.format(style=style_input, length=length_input, topic=paper_input)

        # Invoke the model
        result = model.invoke(prompt)

        # Display the result
        st.subheader("🔍 Summary:")
        st.write(result)
