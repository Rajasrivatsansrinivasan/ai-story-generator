from flask import Flask, request, jsonify, render_template, send_from_directory
from story_utils import build_prompt, text_to_speech, get_supported_languages, get_prose_styles
import os
from dotenv import load_dotenv
import requests
import json
import traceback

load_dotenv()
app = Flask(__name__)

os.makedirs("static/stories", exist_ok=True)

def call_groq_api(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "You are a versatile, creative storyteller who can write engaging stories in multiple languages and prose styles."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,
        "max_tokens": 2000,
        "top_p": 1,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code != 200:
            raise Exception(f"Groq API error: {response.status_code} - {response.text}")
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            return result["choices"][0]["message"]["content"].strip()
        else:
            raise Exception("No story content received from API")
    except Exception as e:
        raise Exception(f"Error calling Groq API: {str(e)}")

@app.route('/api/languages')
def get_languages():
    return jsonify(get_supported_languages())

@app.route('/api/prose-styles')
def get_prose_styles_api():
    return jsonify(get_prose_styles())

@app.route('/generate', methods=['POST'])
def generate_story():
    try:
        data = request.get_json()

        genre = data.get('genre')
        plot = data.get('plot')
        length = data.get('length')
        prose_style = data.get('prose_style', 'Standard')
        language = data.get('language', 'English')
        mood = data.get('mood') or None

        is_continuation = not all([genre, length])

        prompt = build_prompt(genre, plot, length, prose_style, language, mood, is_continuation)
        story = call_groq_api(prompt)

        if not story or len(story.strip()) < 50:
            raise Exception("Generated story is too short or empty")

        import time
        timestamp = str(int(time.time()))
        text_file_path = f"static/stories/story_{timestamp}.txt"
        audio_file_path = f"static/stories/story_{timestamp}.mp3"

        with open(text_file_path, "w", encoding="utf-8") as f:
            f.write(story)

        audio_success = False
        try:
            text_to_speech(story, audio_file_path, language)
            audio_success = True
        except Exception as audio_error:
            print(f"Audio generation failed: {audio_error}")

        response_data = {
            "story": story,
            "text_file": f"/{text_file_path}",
            "prose_style": prose_style,
            "language": language
        }
        if audio_success:
            response_data["audio_file"] = f"/{audio_file_path}"

        return jsonify(response_data)

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/static/stories/<filename>')
def download_file(filename):
    try:
        return send_from_directory('static/stories', filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/health')
def health_check():
    api_key = os.getenv("GROQ_API_KEY")
    return jsonify({
        "status": "healthy",
        "groq_api_configured": bool(api_key),
        "model": "llama3-8b-8192",
        "supported_languages": len(get_supported_languages()),
        "prose_styles": len(get_prose_styles())
    })

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"""
        <html><body><h1>Error</h1><p>{str(e)}</p></body></html>
        """

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')