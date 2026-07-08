import streamlit as st

from src.rag.chain import ask
from src.vectordb.chroma_db import load_vector_store


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="💰",
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

    st.title("💰 AI Financial Advisor")

    st.success("🟢 System Ready")

    st.subheader("System Status")

    st.write("✅ OpenAI Connected")
    st.write("✅ ChromaDB Loaded")
    st.write("✅ Documents Indexed")

    st.divider()

    st.subheader("Statistics")

    st.write(f"📄 Documents: {num_documents}")
    st.write(f"🧠 Model: GPT-4.1")

    st.divider()

    st.info(
        """
This assistant answers questions using
Retrieval-Augmented Generation (RAG).

Responses are grounded in the indexed
financial documents.
"""
    )

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

st.markdown("""
<h1 style="
text-align:center;
font-size:52px;">
💰 AI Financial Advisor
</h1>

<h4 style="
text-align:center;
color:#CBD5E1;">
Enterprise Retrieval-Augmented Financial Assistant
</h4>
""", unsafe_allow_html=True)

# =====================================================
# WELCOME MESSAGE
# =====================================================

if not st.session_state.welcome_shown:

    with st.chat_message("assistant"):

        st.markdown(
            """
## 👋 Welcome!
Ask me anything to get started.
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
    "Ask a question about your financial documents..."
)


# =====================================================
# GENERATE RESPONSE
# =====================================================

if question:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Searching documents and generating answer..."):

            answer, documents = ask(question)

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

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "documents": documents,
        }
    )