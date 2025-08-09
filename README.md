# StoryWeaver X — AI Story Generator

**StoryWeaver X** is an AI-powered web app that generates creative stories based on your input. Choose the genre, language, prose style, and mood—or even upload a file—and let the app create or continue a story with voice narration.

---

## Features

- Genre, Mood, Language & Prose Style selection
- AI-powered story creation using Groq’s LLaMA 3
- Upload a file or type to continue an existing story
- Voice narration with MP3 download
- Stylish black-grey-pink themed UI
- Downloadable story and audio files


---

## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Rajasrivatsansrinivasan/ai-story-generator.git
cd ai-story-generator
```

### 2. Set up virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

### 3. Create `.env` file
Inside the project folder, create a file named `.env` and add your Groq API key:
```
   GROQ_API_KEY=your_actual_groq_api_key_here
```

### 4. Run the application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## Folder Structure

```
ai-story-generator/
├── app.py
├── story_utils.py
├── templates/
│   └── index.html
├── static/
│   └── stories/
│       ├── story_1754688319.txt
│       └── story_1754688319.mp3
├── .env
├── requirements.txt
└── README.md
```

---

## Author & Credits

Developed by [Rajasrivatsan Srinivasan](https://github.com/Rajasrivatsansrinivasan)  
Powered by Groq + gTTS for AI story generation and audio

---

## License

This project is licensed under the MIT License.
