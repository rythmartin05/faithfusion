FaithFusion.net E-commerce platform AI Chatbot and Visual Searcher Demo
==============================================================================

ai_ecommerce/
├── backend/
│   ├── app.py
│   ├── riva/
│   │   └── riva_service.py
│   ├── deepstream/
│   │   └── deepstream_service.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    └── styles.css



This demonstrates an AI-powered chatbot for faithfusion.net
e-commerce platform using NVIDIA Riva for Natural Language Understanding (NLU) and Text-to-Speech (TTS) capabilities.

Prerequisites
-------------

Before running the application, ensure you have the following installed and configured:

- Python 3.x
- Flask
- NVIDIA Riva setup with NLU and TTS services configured

Installation
------------

1. Clone the repository:

2. Install dependencies:

Files
-----

### `app.py`

This file contains the Flask application that serves as the backend for the chatbot.

- **Endpoints:**
- `/chat`: Handles POST requests with a JSON payload containing a `message` key. Processes the message using Riva NLU, generates a response based on the identified intent, and returns the response along with NLU and TTS outputs.

- **Running the Flask Application:**
The Flask application will run locally on http://localhost:5000 by default.

### `riva_services.py`

This file encapsulates functions to interact with the NVIDIA Riva services for ASR (Automatic Speech Recognition), NLU (Natural Language Understanding), and TTS (Text-to-Speech).

- **Functions:**
- `riva_nlu(text)`: Sends text data to Riva NLU service endpoint to determine user intents.
- `riva_tts(text)`: Sends text data to Riva TTS service endpoint to generate speech from text.

- **Configurations:**
Update `RIVA_NLU_ENDPOINT` and `RIVA_TTS_ENDPOINT` with your actual Riva service endpoints and configure `API_KEY` for authentication if required.

Usage
-----

1. Ensure the Flask application (`app.py`) is running:

2. Send HTTP POST requests to `http://localhost:5000/chat` with a JSON payload containing a `message` key to interact with the chatbot.

Example:

3. The chatbot will process the message using Riva NLU, generate a response, and use Riva TTS to convert the response into speech.

Notes
-----

- Customize `process_chat_message` function in `app.py` to enhance chatbot logic based on your specific requirements and intents.
- Securely manage API keys and endpoints for Riva services to ensure proper authentication and authorization.
- Monitor logs and handle exceptions to ensure smooth operation of the application.
