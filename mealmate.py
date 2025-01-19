from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("Meal Mate")

# Input text box for user queries
input_txt = st.text_input("Please input your diet queries here...")

# Correct the ChatPromptTemplate usage and message formatting
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful diet AI assistant. Your name is Meal Mate. Your job is to provide personalized meal plans, guided cooking, and integrated grocery ordering plans."),
        ("user", "User query: {query}")
    ]
)

# Use the correct instantiation of Ollama
llm = Ollama(model="llama3.2")

# Initialize output parser
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Check if user provided input and display the response
if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)