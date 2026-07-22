import streamlit as st
import os

from src.graph.graph import graph
from src.vectordb.chroma_db import load_vector_store


st.write("OPENAI KEY FOUND:", bool(os.environ.get("OPENAI_API_KEY")))

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

load_vector_store()


if "messages" not in st.session_state:
    st.session_state.messages = []



with st.sidebar:

    st.title("📚 AI Research Assistant")

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.subheader("Capabilities")

    st.markdown(
        """
- 📄 Answer questions from uploaded documents
- 🔍 Search academic papers
- 🌟 Discover seminal papers
- 🤝 Find related research
- 🕸️ Explore citation networks
"""
    )


    st.markdown("---")

    st.caption("Version 1.0")



st.title("📚 AI Research Assistant")

st.caption(
    "Ask questions about your uploaded documents or explore academic research using OpenAlex."
)




for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



question = st.chat_input("Ask a question...")


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        try:

            state = {
                "question": question,
                "route": "",
                "answer": "",
                "documents": [],
            }

            result = graph.invoke(state)

            answer = result["answer"]

        except Exception as e:

            answer = f"❌ {e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)