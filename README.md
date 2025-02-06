# Agentic-AI-Chatbot

## Introduction
The **Agentic AI Chatbot application** allows users to interact with AI-powered agents using advanced LLMs. It integrates **LangGraph, FastAPI, Streamlit, and Tavily Search** for an interactive chatbot experience with optional web search capabilities.

## Features
- Select AI models from Groq (Llama-3.3, Mixtral-8x7b) or OpenAI (GPT-4o-mini).
- Chat with AI agents using a user-friendly Streamlit interface.
- You can enable web search functionality to gather more relevant responses.
- The backend is built with FastAPI for scalability and efficiency.
- Uses LangChain and LangGraph for intelligent agent interactions.


## Phase -1 (Create AI Agent)

1. Setup API Keys for Groq, Tavily, and OpenAI.
2. Setup LLM Tools.
3. Setup AI Agent with Search Tool Functionality.

`pipenv install langchain_groq langchain_openai langchain_community`
`pipenv install langgraph`

## Phase -2 (Setup Backend with FastAPI)

1. Setup Pydantic Model (Schema Validation).
2. Setup AI Agnet from FrontEnd Request.
3. Run the App and explore Swaggers UI docs.

## Phase -3 (Setup FrontEnd)

1. Setup UI with Streamlit.
2. Connect with the backend via URL.

## Tools & Technologies

* LangGraph ReAct Agents
* FastAPI for API calls
* Groq & Open AI for LLM
* Streamlit for UI (FrontEnd)
* LangChain for Tools
* Uvicorn for hosting app
* Python
* VS Code
