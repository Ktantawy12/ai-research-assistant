import streamlit as st

from src.graph.graph import graph
from src.vectordb.chroma_db import load_vector_store


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Research AI Assistant",
    page_icon="🤖",
    layout="wide",
)


# =====================================================
# VECTOR DATABASE STATS
# =====================================================

vector_store = load_vector_store()

db = vector_store.get()

num_chunks = len(db["documents"])

sources = {
    metadata["source"]
    for metadata in db["metadatas"]
}

num_documents = len(sources)


# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 Research AI Assistant")

    st.divider()

    st.write(f"📄 Documents: {num_documents}")
    st.write("🧠 Model: GPT-4.1")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
    ):

        st.session_state.messages = []
        st.session_state.welcome_shown = False

        st.rerun()


# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
<h1 style="text-align:center; font-size:52px;">
 Research AI Assistant
</h1>

<h4 style="text-align:center; color:#CBD5E1;">
Research Retrieval-Augmented Generation Assistant
</h4>
""",
    unsafe_allow_html=True,
)


# =====================================================
# WELCOME MESSAGE
# =====================================================

if not st.session_state.welcome_shown:

    with st.chat_message("assistant"):

        st.markdown(
            """
## 👋 Welcome!

Ask me anything about your uploaded documents.
"""
        )

    st.session_state.welcome_shown = True


# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =====================================================
# CHAT INPUT
# =====================================================

question = st.chat_input(
    "Ask a question..."
)


# =====================================================
# GENERATE RESPONSE
# =====================================================

if question:

    # -------------------------------
    # Save & display user message
    # -------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -------------------------------
    # Assistant response
    # -------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Searching documents and generating answer..."):

            result = graph.invoke(
                {
                    "question": question,
                    "answer": "",
                    "documents": [],
                }
            )

            answer = result["answer"]
            documents = result["documents"]

        with st.container(border=True):

            st.markdown(answer)

        with st.expander("📚 Sources Used"):

            for doc in documents:

                source = doc.metadata.get("source", "Unknown")
                source = source.replace("\\", "/").split("/")[-1]

                page = doc.metadata.get("page", 0) + 1

                st.markdown(f"**📄 {source}**")
                st.caption(f"Page {page}")

                preview = doc.page_content[:250]

                st.write(preview + "...")

                st.divider()

    # -------------------------------
    # Save assistant message
    # -------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "documents": documents,
        }
    )