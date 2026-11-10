# ai_chatbot_memory

An AI-powered conversational chatbot that remembers prior conversation turns and uses that context to answer follow-up questions more naturally.

## What this project does

This app creates a small chat interface where a user can ask questions while the assistant keeps track of the recent conversation history. The chatbot is built with:

- Gradio for the web UI
- LangChain for chaining prompts and model calls
- Groq as the LLM provider
- environment variables for managing the API key and model settings

## How the memory works

The chatbot stores previous messages in the chat history, then converts them into LangChain message objects before sending them to the model. This allows the model to answer in context instead of treating each message as isolated and unrelated.

## Setup

1. Create a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Groq credentials:
   ```env
   GROQ_API_KEY=your_api_key_here
   GROQ_MODEL_ID=your_model_name_here
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Project files

- `app.py`: starts the Gradio interface
- `chatbot.py`: handles the chat model, prompt setup, and conversation memory conversion
- `requirements.txt`: Python dependencies

## Notes

This project is a simple example of a memory-enabled chatbot. It is designed to be easy to understand and extend if you want to add more advanced memory, retrieval, or conversation features later.
