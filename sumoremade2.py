import streamlit as st
import os
from langchain_openai import AzureChatOpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.callbacks import get_openai_callback


# Chatbot Headings 
st.image('https://www.dogster.com/wp-content/uploads/2024/03/close-up-of-labrador-retriever_Chiemsee2016_Pixabay.jpg', caption='Happy boy')
st.title("AzureOpenAI (Happy Boy) Chatbot")
st.text("This chatbot is Agile 2: Scooter")


# API access credentials from streamlit secrets
os.environ["AZURE_OPENAI_API_KEY"] = st.secrets["AZURE_OPENAI_KEY"]
os.environ["AZURE_OPENAI_ENDPOINT"] = st.secrets["AZURE_OPENAI_ENDPOINT"]


def generate_response(input_text):
    model = AzureChatOpenAI(
        openai_api_version="2024-02-15-preview",
        azure_deployment=st.secrets["AZURE_OPENAI_35"],
    )
    message = HumanMessage(
        content=input_text
    )
   
    with get_openai_callback() as cb:
        st.info(model([message]).content) # chat model output
        st.info(cb) # callback output (like cost)

with st.form("my_form"):
    text = st.text_area("Enter text:")
    submitted = st.form_submit_button("Submit")
    generate_response(text)

