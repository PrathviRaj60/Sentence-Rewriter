from flask import Flask, render_template, request, jsonify
import cohere
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

API_KEY = "TgyrJfpx02UujwLyhe7qodbRR0NSsSTLMlBWCZvo"
co = cohere.Client(API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.json
    sentence = data.get('sentence')
    vibe = data.get('vibe')

    prompt = (
        f"Rewrite the following sentence in a {vibe} tone:\n\n"
        f"Sentence: {sentence}\n"
        f"Rewritten:"
    )

    try:
        response = co.generate(
            model="command-xlarge",
            prompt=prompt,
            max_tokens=60,
            temperature=0.7,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["\n"]
        )
        rewritten = response.generations[0].text.strip()
        return jsonify({'rewritten': rewritten})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)
