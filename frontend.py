# ********* Phase-3 (Setup FrontEnd) ***************

# Step-1 --> Setup UI with Streamlit (model provider, model, system prompt, web search, query).

import streamlit as st

##initialize our streamlit app

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.header("Agentic AI Chatbot Application")
st.write("Create and Interact with the AI Agents!")

# Sidebar for instructions

st.sidebar.title("Agentic AI Chatbot")
st.sidebar.image("https://miro.medium.com/v2/resize:fit:1400/1*hdd2IGtXs3E8rsa98m-kCg.png", caption="Your Agentic AI Assistant", use_container_width=True)

st.sidebar.title("Instructions 📜")
st.sidebar.markdown(
    """
    1. Enter your Persona/Role for AI agent in first step.
    2. Select your LLM Model Provider i.e, Groq / OpenAI.
    3. Select the Model based on Provider.
    4. Enter your Query and ask Agent!.
    
    """
)

system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        # Step-2 --> Connect with backend via URL
        import requests
        # payload == RequestState
        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
