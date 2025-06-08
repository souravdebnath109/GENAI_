import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Initialize the model
model = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="gemini_api_key")

# Streamlit UI
st.title("🧠 RAT - Research Assistant Tool")

# User input
user_input = st.text_area("Enter your research question or topic:")

# Summarize button
if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter a topic to summarize.")
    else:
        # Define prompt template
        prompt_template = PromptTemplate.from_template(
            "Summarize the following research topic in simple terms:\n\n{topic}"
        )
        prompt = prompt_template.format(topic=user_input)

        # Invoke the model
        result = model.invoke(prompt)

        # Display the result
        st.subheader("🔍 Summary:")
        st.write(result)
