import os
import requests
from gtts import gTTS
from google import genai

# API Key configuration
client = genai.Client(api_key=os.environ["GEMINI_KEY"])

def start_bot():
    try:
        # Latest stable fast model
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="Hulk in Karachi 1 line story"
        )

        story = response.text

        # MP3 file generate
        tts = gTTS(text=story, lang='en')
        tts.save("hulk.mp3")

        # Image download
        img_url = "https://image.pollinations.ai/prompt/hulk_karachi_street"
        img_data = requests.get(img_url).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        print(f"✅ Success! Story: {story}")

    except Exception as e:
        print(f"❌ Error Detail: {e}")

if __name__ == "__main__":
    start_bot()
