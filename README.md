# 🤖 AI Chatbot Using Astra API

A simple AI chatbot built with Python using the GPT-6 Astra model through the Astra API.

## Features

- Interactive command-line chatbot
- Conversation history
- AI-generated responses
- Secure API key using environment variables
- Exit commands: exit, quit, bye

## Technologies Used

- Python
- Requests
- python-dotenv
- Astra API

## Project Structure

```text
ai-chatbot/
├── chatbot.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
## 🔑 API Setup

This chatbot uses the KIE AI API to generate AI responses.

### 1. Get an API Key

Create an API key from your KIE AI account.

### 2. Create the `.env` file

Create a file named `.env` in the project folder and add:

```env
API_KEY=YOUR_API_KEY_HERE