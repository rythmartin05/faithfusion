from flask import Flask, request, jsonify, send_file
from io import BytesIO
from riva.riva_service import chat_with_riva, recognize_speech, understand_nlu, generate_speech
from deepstream.deepstream_service import process_image

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')

    # Process the chat message
    chat_response = process_chat_message(message)

    # Perform NLU using Riva
    nlu_response = riva_nlu(message)

    # Generate TTS using Riva
    tts_response = riva_tts(message)

    return jsonify({
        'chat_response': chat_response,
        'nlu_response': nlu_response,
        'tts_response': base64.b64encode(tts_response).decode('utf-8')  # Encode TTS audio as base64
    })

def process_chat_message(nlu_response):
    # Example: Extract intent from Riva NLU response and generate response accordingly
    if 'intent' in nlu_response:
        intent = nlu_response['intent']['name']
        if intent == 'greet':
            return "Hi there! How can I assist you today?"
        elif intent == 'recommendation':
            # Replace with logic to provide product recommendations based on user preferences
            return "Here are some recommendations for you..."
        elif intent == 'purchase':
            # Replace with logic to assist in making a purchase
            return "Sure, I can help you with that. What product are you interested in?"
    return "I'm sorry, I didn't understand that. Can you please rephrase?"


@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    response = process_image(image)
    return jsonify(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
