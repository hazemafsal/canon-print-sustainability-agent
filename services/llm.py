import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    API_KEY = st.secrets.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=API_KEY,
    temperature=0
)