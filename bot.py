import os
import requests
from gtts import gTTS
from google import genai

def start_bot():
    try:
        # Client create
        client = genai.Client(api_key=os.environ["GEMINI_KEY"])

        # Generate story
        response = client.models.generate_content(
    model = genai.GenerativeModel('gemini-pro')
    contents="Hulk in Karachi 1 line story"
        )

        story = response.text

        # Save MP3
        tts = gTTS(text=story, lang="en")
        tts.save("hulk.mp3")

        # Download Image
        img_url = "https://image.pollinations.ai/prompt/hulk_karachi_street"
        img_data = requests.get(img_url).content

        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        print("✅ Success:", story)

    except Exception as e:
        print("❌ Error Detail:", e)

if __name__ == "__main__":
    start_bot()
