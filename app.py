import streamlit as st
from huggingface_hub import InferenceClient

# Load token from secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(api_key=HF_TOKEN)

MODEL = "Qwen/Qwen2.5-7B-Instruct"

st.title("AI Food & Farmer Assistant")

st.write("Ask questions about crops, fertilizers, pesticides, nutrition, or farming.")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are an AI assistant helping farmers with crops, fertilizers, pesticides, and food nutrition."
        }
    ]

# Chat input
user_input = st.chat_input("Ask your question...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("AI thinking..."):

        response = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
            max_tokens=300
        )

        answer = response.choices[0].message.content

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])