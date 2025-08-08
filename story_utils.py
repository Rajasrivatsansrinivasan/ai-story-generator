from gtts import gTTS
import os

def build_prompt(genre, plot, length, prose_style="Standard", language="English", mood=None, is_continuation=False):
    """Build a detailed prompt for story generation with prose style, language, mood, and continuation support"""
    length_map = {
        "Short": "under 200 words",
        "Medium": "300–500 words", 
        "Long": "up to 800 words"
    }

    prose_styles = {
        "Standard": "clear, straightforward narrative style with balanced descriptions",
        "Literary": "sophisticated, literary prose with rich metaphors, complex sentence structures, and deep character introspection",
        "Minimalist": "concise, spare prose with short sentences and understated descriptions, focusing on subtext",
        "Descriptive": "highly detailed, vivid prose with extensive sensory descriptions and atmospheric writing",
        "Dialogue-Heavy": "story driven primarily through character conversations and interactions",
        "Stream of Consciousness": "flowing, unstructured narrative that follows the character's inner thoughts and feelings",
        "Poetic": "lyrical, rhythmic prose with beautiful imagery and metaphorical language",
        "Noir": "dark, gritty prose with cynical tone and atmospheric descriptions typical of detective fiction",
        "Whimsical": "playful, imaginative prose with quirky descriptions and lighthearted tone",
        "Epic": "grand, sweeping prose with heroic language and larger-than-life descriptions"
    }

    language_instruction = f"Write the story in {language}."
    mood_instruction = f"Make the tone of the story {mood.lower()}." if mood else ""
    prose_instruction = f"Write in a {prose_style.lower()} style - {prose_styles.get(prose_style, prose_styles['Standard'])}"

    if is_continuation:
        prompt = f"""{language_instruction}
{mood_instruction}
{prose_instruction}

The following is the beginning of a story. Continue it in a natural and engaging way:

{plot}

[Continue the story from here...]
"""
    else:
        prompt = f"""Create an engaging {genre} story that is {length_map.get(length, 'medium length')} based on this idea:

{plot}

{language_instruction}
{mood_instruction}
{prose_instruction}

Please create a compelling story with:
- A clear beginning, middle, and end
- Appropriate tone and length
- Well-developed characters
- Vivid descriptions and emotional depth
"""

    return prompt.strip()

def text_to_speech(text, output_path, language="en"):
    """Convert text to speech and save as MP3 with language support"""
    try:
        print(f"🔊 Converting text to speech... (Language: {language}, Length: {len(text)} characters)")

        language_codes = {
            "English": "en",
            "Spanish": "es", 
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Russian": "ru",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese (Mandarin)": "zh",
            "Arabic": "ar",
            "Hindi": "hi",
            "Dutch": "nl",
            "Polish": "pl",
            "Turkish": "tr",
            "Swedish": "sv",
            "Danish": "da",
            "Norwegian": "no",
            "Finnish": "fi",
            "Greek": "el",
            "Hebrew": "he",
            "Thai": "th",
            "Vietnamese": "vi",
            "Czech": "cs",
            "Hungarian": "hu",
            "Romanian": "ro",
            "Bulgarian": "bg",
            "Croatian": "hr",
            "Slovak": "sk",
            "Slovenian": "sl",
            "Estonian": "et",
            "Latvian": "lv",
            "Lithuanian": "lt",
            "Urdu": "ur",
            "Bengali": "bn",
            "Tamil": "ta",
            "Telugu": "te",
            "Malayalam": "ml",
            "Kannada": "kn",
            "Gujarati": "gu",
            "Punjabi": "pa",
            "Marathi": "mr",
            "Nepali": "ne",
            "Sinhala": "si",
            "Burmese": "my",
            "Khmer": "km",
            "Lao": "lo",
            "Georgian": "ka",
            "Armenian": "hy",
            "Azerbaijani": "az",
            "Kazakh": "kk",
            "Kyrgyz": "ky",
            "Tajik": "tg",
            "Uzbek": "uz",
            "Mongolian": "mn",
            "Tibetan": "bo",
            "Welsh": "cy",
            "Irish": "ga",
            "Scottish Gaelic": "gd",
            "Basque": "eu",
            "Catalan": "ca",
            "Galician": "gl",
            "Maltese": "mt",
            "Icelandic": "is",
            "Albanian": "sq",
            "Macedonian": "mk",
            "Serbian": "sr",
            "Bosnian": "bs",
            "Montenegrin": "sr",
            "Afrikaans": "af",
            "Swahili": "sw",
            "Yoruba": "yo",
            "Igbo": "ig",
            "Hausa": "ha",
            "Zulu": "zu",
            "Xhosa": "xh",
            "Amharic": "am",
            "Somali": "so",
            "Malay": "ms",
            "Indonesian": "id",
            "Filipino": "tl",
            "Maori": "mi",
            "Hawaiian": "haw"
        }

        lang_code = language_codes.get(language, "en")
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(output_path)

        print(f"✅ Audio saved successfully: {output_path} (Language: {language})")
        return True

    except Exception as e:
        print(f"❌ Text-to-speech error: {e}")
        if language != "English":
            try:
                tts = gTTS(text=text, lang="en", slow=False)
                tts.save(output_path)
                print(f"✅ Audio saved successfully with English fallback: {output_path}")
                return True
            except Exception as fallback_error:
                print(f"❌ Fallback audio generation also failed: {fallback_error}")
                raise fallback_error
        else:
            raise e

def get_supported_languages():
    return [
        "English", "Spanish", "French", "German", "Italian", "Portuguese", 
        "Russian", "Japanese", "Korean", "Chinese (Mandarin)", "Arabic", "Hindi",
        "Dutch", "Polish", "Turkish", "Swedish", "Danish", "Norwegian", 
        "Finnish", "Greek", "Hebrew", "Thai", "Vietnamese", "Czech", 
        "Hungarian", "Romanian", "Bulgarian", "Croatian", "Slovak", 
        "Slovenian", "Estonian", "Latvian", "Lithuanian", "Urdu", 
        "Bengali", "Tamil", "Telugu", "Malayalam", "Kannada", "Gujarati", 
        "Punjabi", "Marathi", "Nepali", "Sinhala", "Burmese", "Khmer", 
        "Lao", "Georgian", "Armenian", "Azerbaijani", "Kazakh", "Kyrgyz", 
        "Tajik", "Uzbek", "Mongolian", "Tibetan", "Welsh", "Irish", 
        "Scottish Gaelic", "Basque", "Catalan", "Galician", "Maltese", 
        "Icelandic", "Albanian", "Macedonian", "Serbian", "Bosnian", 
        "Montenegrin", "Afrikaans", "Swahili", "Yoruba", "Igbo", "Hausa", 
        "Zulu", "Xhosa", "Amharic", "Somali", "Malay", "Indonesian", 
        "Filipino", "Maori", "Hawaiian"
    ]

def get_prose_styles():
    return {
        "Standard": "Balanced, clear narrative - perfect for most stories",
        "Literary": "Sophisticated prose with rich metaphors and deep introspection",
        "Minimalist": "Spare, understated style focusing on subtext and brevity",
        "Descriptive": "Highly detailed with vivid sensory descriptions",
        "Dialogue-Heavy": "Story driven through character conversations",
        "Stream of Consciousness": "Flowing narrative following inner thoughts",
        "Poetic": "Lyrical, rhythmic prose with beautiful imagery",
        "Noir": "Dark, gritty style with cynical tone",
        "Whimsical": "Playful, imaginative with quirky descriptions",
        "Epic": "Grand, heroic language for larger-than-life stories"
    }