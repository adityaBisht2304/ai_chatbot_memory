# This module contains the core logic for the memory-enabled chatbot.
# It loads the environment config, creates the LLM, defines the prompt template,
# and converts chat history into a format that LangChain can understand.

import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables such as the Groq API key and model name.
load_dotenv()

# Create the Groq-backed chat model. The model name is pulled from the .env file,
# and the base URL points to the Groq API endpoint.
model = ChatGroq(
    model=os.getenv("GROQ_MODEL_ID"),
    base_url="https://api.groq.com",
)

# Define the prompt template. The system prompt gives the assistant its behavior,
# the history placeholder lets it use previous messages, and the human message
# contains the latest question from the user.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a friendly chatassistant. Use conversation history for context."
        "Answer only what is asked, and never make up information. If unsure, say 'I don't know.'",
    ),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])

# Combine the prompt and model into a single runnable LangChain chain.
chain = prompt | model


def chatFunction(message: str, history: list[dict[str, str]]) -> str:
    """Send a new user message and previous chat history to the LLM.

    Gradio provides the current message plus the full conversation history in a
    list of dictionaries. We convert each role into the proper LangChain message
    type so the model sees the conversation in a consistent structure.
    """
    # Store the converted history in a format expected by LangChain.
    langchain_history = []

    for turn in history:
        # User messages become HumanMessage objects.
        if turn["role"] == "user":
            langchain_history.append(HumanMessage(content=turn["content"]))
        # Assistant messages become AIMessage objects.
        elif turn["role"] == "assistant":
            langchain_history.append(AIMessage(content=turn["content"]))

    # Invoke the prompt chain with the prior conversation context and the newest
    # question. The final .content extracts the assistant text from the model reply.
    return chain.invoke({"history": langchain_history, "question": message}).content
