import requests

# Update with actual Riva endpoints
RIVA_CHATBOT_URL = 'http://localhost:50051/chatbot'
RIVA_ASR_URL = 'http://localhost:50051/asr'
RIVA_NLU_URL = 'http://localhost:50051/nlu'
RIVA_TTS_URL = 'http://localhost:50051/tts'

def chat_with_riva(user_message):
    try:
        response = requests.post(RIVA_CHATBOT_URL, json={'message': user_message})
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'message': 'Error communicating with Riva service', 'error': str(e)}

def recognize_speech(audio_file):
    try:
        files = {'audio': audio_file.read()}
        response = requests.post(RIVA_ASR_URL, files=files)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'message': 'Error communicating with Riva ASR service', 'error': str(e)}

def understand_nlu(text):
    try:
        response = requests.post(RIVA_NLU_URL, json={'text': text})
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'message': 'Error communicating with Riva NLU service', 'error': str(e)}

def generate_speech(text):
    try:
        response = requests.post(RIVA_TTS_URL, json={'text': text})
        return response.content  # Assuming TTS returns audio data
    except requests.exceptions.RequestException as e:
        return {'message': 'Error communicating with Riva TTS service', 'error': str(e)}
