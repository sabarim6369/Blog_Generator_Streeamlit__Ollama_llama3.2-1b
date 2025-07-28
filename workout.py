import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
prompttemplate=PromptTemplate.from_template("Write a blog post for {topic}")
chain=prompttemplate | Ollama(model="llama3.2:1b")
st.set_page_config("Local Blog generator");
st.title("📝 Blog Post Generator using Ollama (llama3.2:1b)")
topic=st.text_input("Enter a blog topic",placeholder="e.g., climate change")
if st.button("Generate Blog Post"):
  if topic.strip() == "":
        st.warning("Please enter a topic.")
  else:
        with st.spinner("Generating..."):
            result = chain.invoke({"topic": topic})
            st.subheader("📰 Blog Post:")
            st.write(result)