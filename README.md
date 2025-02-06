# Agentic-AI-Chatbot

## Introduction
The **Agentic AI Chatbot application** allows users to interact with AI-powered agents using advanced LLMs. It integrates **LangGraph, FastAPI, Streamlit, and Tavily Search** for an interactive chatbot experience with optional web search capabilities.

## Features
- Select AI models from Groq (Llama-3.3, Mixtral-8x7b) or OpenAI (GPT-4o-mini).
- Chat with AI agents using a user-friendly Streamlit interface.
- You can enable web search functionality to gather more relevant responses.
- The backend is built with FastAPI for scalability and efficiency.
- Uses LangChain and LangGraph for intelligent agent interactions.

## Installation and Setup Guide

### Using pipenv
1. Install pipenv (if not already installed):

   `pip install pipenv`

2. Use this command to load environment variables: `pipenv shell` 

### .env File

Create a .env file to store your private API keys for Groq, Tavily, and OpenAI.
### Phase-1 (Create AI Agent)

1. Create an ai_agent.py file, and set up LLM Tools and AI Agent with Search Tool Functionality.
2. Install these Dependencies in phase-1 with pipenv:
   `pipenv install langchain_groq` `langchain_openai` `langchain_community` `langgraph`

### Phase-2 (Setup Backend with FastAPI)

1. Create a backend.py file and set up the Pydantic Model (Schema Validation).
2. Setup AI Agnet from FrontEnd Request.
3. Run the App and explore Swaggers UI docs.
4. Install these Dependencies in phase-2 with pipenv:
   `pipenv install pydantic` `fastapi` `uvicorn`
   
### Phase-3 (Setup FrontEnd)

1. Create a frontend.py file and set up UI with Streamlit.
2. Connect with the backend via URL.
3. Install these Dependencies in phase-3 with pipenv:
   `pipenv install streamlit`

## Note:
Make sure the backend Python script is running in a separate terminal and load environment variables using: `pipenv shell` 

## Tools & Technologies

* LangGraph ReAct Agents
* FastAPI for API calls
* Groq & Open AI for LLM
* Streamlit for UI (FrontEnd)
* LangChain for Tools
* Uvicorn for hosting app
* Python
* VS Code
