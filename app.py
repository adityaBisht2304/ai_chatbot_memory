# This file launches the web-based chat UI for the memory-enabled chatbot.
# The actual language model logic lives in chatbot.py, while this file connects
# it to a Gradio interface so users can interact with it in the browser.

import gradio as gr
from chatbot import chatFunction


if __name__ == "__main__":
    # Build the chat interface and wire it to the function that handles model
    # responses. Gradio keeps the conversation history and passes it to the
    # backend function on each message.
    gr.ChatInterface(
        fn=chatFunction,
        title="Chat with Memory-Enabled LLM",
        description="A chat interface that remembers the conversation history.",
    ).launch(share=True)  # Set share=True to get a public link for the interface.
