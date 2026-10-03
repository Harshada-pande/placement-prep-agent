import streamlit as st

from agent import ask_agent


# Page configuration
st.set_page_config(
    page_title="Placement Prep Agent",
    page_icon="🤖",
    layout="centered"
)


# Title
st.title("🤖 Placement Prep Agent")

st.write(
    "Ask questions about DSA, technical interviews, "
    "company preparation, and placement preparation."
)


# User input
question = st.text_area(
    "What do you want help with?",
    placeholder="Example: I have an HSBC technical interview in 5 days. What should I prepare?",
    height=120
)


# Ask button
if st.button("Ask Agent", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Agent is thinking..."):

            answer = ask_agent(question)

        st.subheader("🤖 Agent Response")

        st.write(answer)