# Agentic-AI-Chatbot

## Introduction
The **Agentic AI Chatbot application** allows users to interact with AI-powered agents using advanced LLMs. It integrates **LangGraph, FastAPI, Streamlit, and Tavily Search** for an interactive chatbot experience with optional web search capabilities.

## Features
- Select AI models from Groq (Llama-3.3, Mixtral-8x7b) or OpenAI (GPT-4o-mini).
- Chat with AI agents using a user-friendly Streamlit interface.
- You can enable web search functionality to gather more relevant responses.
- The backend is built with FastAPI for scalability and efficiency.
- Uses LangChain and LangGraph for intelligent agent interactions.

## Archtectural Diagram

<img align ="center" alt="Architectral Diagram" width = "400" src="https://github.com/sherryyy19/Agentic-AI-Chatbot/blob/main/architecture%20diagram.png?raw=true">

## Installation and Setup Guide

### Using pipenv
1. Install pipenv (if not already installed):

   ```sh
    pip install pipenv
    ```

### .env File

* Create a .env file to store your private API keys for Groq, Tavily, and OpenAI.
* Use this command to load environment variables: `pipenv shell` 
### Phase-1 (Create AI Agent)

1. Create an ai_agent.py file, and set up LLM Tools and AI Agent with Search Tool Functionality.
2. Install these Dependencies in phase-1 with pipenv:
   ```sh
    pipenv install langchain_groq
    ```
   ```sh
    pipenv install langchain_openai
    ```
   ```sh
    pipenv install langchain_community
    ```
    ```sh
    pipenv install langgraph
    ```

### Phase-2 (Setup Backend with FastAPI)

1. Create a backend.py file and set up the Pydantic Model (Schema Validation).
2. Setup AI Agnet from FrontEnd Request.
3. Run the App and explore Swaggers UI docs.
4. Install these Dependencies in phase-2 with pipenv:
   ```sh
    pipenv install pydantic
    ```
   ```sh
    pipenv install fastapi
    ```
   ```sh
    pipenv install uvicorn
    ```
   
### Phase-3 (Setup FrontEnd)

1. Create a frontend.py file and set up UI with Streamlit.
2. Connect with the backend via URL.
3. Install these Dependencies in phase-3 with pipenv:
   ```sh
    pipenv install streamlit
    ```

## How to Run:
* First load environment variables using: `pipenv shell`
* Make sure the backend Python script is running in a separate terminal using the command: `python backend.py`
* Then run the frontend file using the command: `streamlit run frontend.py`

## Tools & Technologies

* LangGraph ReAct Agents
* FastAPI for API calls
* Groq & Open AI for LLM
* Streamlit for UI (FrontEnd)
* LangChain for Tools
* Uvicorn for hosting app
* Python
* VS Code
