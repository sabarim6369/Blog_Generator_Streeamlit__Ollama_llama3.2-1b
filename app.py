import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain.callbacks import tracing_v2_enabled    # Ensure LangSmith tracing is enabled

# Load environment variables from .env
load_dotenv()

# Make sure LangSmith environment variables are loaded
# Or set them manually as fallback
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "lsv2_pt_...")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "Blogapp")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")

# Setup Ollama model
llm = Ollama(model="llama3.2:1b")

# Define prompt template and chain
prompt_template = PromptTemplate.from_template("Write a blog post for {topic}")
chain = prompt_template | llm

# Streamlit UI
st.set_page_config(page_title="Local Blog Generator", layout="centered")
st.title("📝 Blog Post Generator using Ollama (llama3.2:1b)")

topic = st.text_input("Enter a blog topic", placeholder="e.g., climate change")

if st.button("Generate Blog Post"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            # LangSmith tracing enabled here
            with tracing_v2_enabled():
                result = chain.invoke({"topic": topic})
            st.subheader("📰 Blog Post:")
            st.write(result)
