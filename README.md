<img width="1666" alt="Article_summariser_app" src="https://github.com/user-attachments/assets/68337cac-274b-4faf-b343-c6eef5576c40" />
# llm-summariser-app
  🧠 LLM Summarizer App LLM Summarizer App is a simple and powerful web application that allows users to generate abstractive summaries of long articles using OpenAI's GPT models (like GPT-3.5 or GPT-4). It is built with Streamlit for the frontend and integrates with the OpenAI API to handle the summarization logic.

## 🚀 Features

🔍 Paste any article or text and get a concise abstractive summary

🤖 Powered by OpenAI's gpt-3.5-turbo or gpt-4 models

🎛️ Adjustable parameters (creativity, summary length)

⚡ Fast and lightweight Streamlit interface

🔒 Secure API key handling with .streamlit/secrets.toml

## 🛠️ Tech Stack

Frontend: Streamlit

LLM Backend: OpenAI API

Language: Python 3

## 📦 Setup Instructions

### Clone the repo
git clone https://github.com/yourusername/llm-summarizer-app.git

cd llm-summarizer-app

### Create and activate virtual environment
python -m venv venv

source venv/bin/activate  # or venv\Scripts\activate on Windows

### Install dependencies
pip install -r requirements.txt

### Add your OpenAI API key in .streamlit/secrets.toml

Example secrets.toml:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxx"

## 🧪 Run the App
streamlit run summarizer_app.py

## 📚 Use Case Examples
Summarizing news articles

Digesting long blog posts

Creating executive summaries

Reducing academic or research papers






