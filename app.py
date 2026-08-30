from flask import Flask, request, render_template, jsonify
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    raise ValueError("BŁĄD: Brak klucza API ANTHROPIC_API_KEY w zmiennych srodowiskowych")

app = Flask(__name__)
client = anthropic.Anthropic(api_key=api_key)
historia = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    dane = request.get_json()
    wiadomosc = dane.get('message', '')
    
    if not wiadomosc:
        return jsonify({'error': 'Wiadomosc jest pusta'}), 200
    
    historia.append({"role": "user", "content": wiadomosc})
    
    try:
        odpowiedz = client.messages.create(
            model="claude-3-5-sonnet",
            max_tokens=200,
            messages=historia
        )
        tresc = odpowiedz.content[0].text
        historia.append({"role": "assistant", "content": tresc})
        return jsonify({'response': tresc})
    except Exception as e:
        return jsonify({'error': str(e)}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
