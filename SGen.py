import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

class Commaseparatedoutput(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(",")

# Set up Streamlit UI
st.set_page_config(page_title="Synonyms Generator")
st.header("📝 Synonyms Generator 🔄")

# Define the template for the chat prompt
template = "You are a helpful assistant. When the user provides any input, you should generate 5 words synonyms in a comma-separated list."
human_template = "{text}"

# Create the ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])

# Create the ChatOpenAI model
model = ChatOpenAI()

# Create the chain
chain = chat_prompt | model | Commaseparatedoutput()

# Text input for user query
input_text = st.text_input("Enter a word or phrase:", "")

# Button to trigger the synonym generation
if st.button("Generate Synonyms"):
    # Perform the conversation with the chatbot
    if input_text:
        # Get the chatbot response
        response = chain.invoke({"text": input_text})

        # Display the synonyms
        st.write("Synonyms:", ", ".join(response))
    else:
        st.write("Please enter a word or phrase.")
