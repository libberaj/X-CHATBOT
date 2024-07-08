from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = ""
os.environ["LANGCHAIN_API_KEY"] = ""

os.environ["LANGCHAIN_PROJECT"]= "Tutorial1"


os.environ["LANGCHAIN_TRACING_V2"]= "true"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the queries"),
        ("user","Question:{question}")
    ]
)

st.title("CHATBOT WITH OLLAMA")
input_text=st.text_input("search the topic you want")

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
