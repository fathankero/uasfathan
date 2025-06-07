from flask import Flask, render_template, request, jsonify
from google.cloud import translate_v2 as translate
import os

app = Flask(__name__)

# Inisialisasi Google Translate client
translate_client = translate.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    result = translate_client.translate(text, target_language='ja')
    return jsonify({'translated': result['translatedText']})

if __name__ == '__main__':
    # Jalankan di host 0.0.0.0 dan port yang diberikan environment variable PORT (default 8080)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
