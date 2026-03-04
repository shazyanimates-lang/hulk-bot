import os
import requests
import google.generativeai as genai
from gtts import gTTS

# GitHub Secrets se API Key uthana
api_key = os.environ.get("GEMINI_KEY")

if not api_key:
    print("Error: GEMINI_KEY nahi mili. Secrets check karein!")
else:
    genai.configure(api_key=api_key)

def start_bot():
    try:
        # Stable model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Story generate karna
        prompt = "Write a 1-line funny story about Hulk eating Biryani in Karachi."
        response = model.generate_content(prompt)
        story_text = response.text
        print(f"Story: {story_text}")

        # Audio File (TTS) banana
        tts = gTTS(text=story_text, lang='en')
        tts.save("hulk_story.mp3")
        print("Audio saved as hulk_story.mp3")

        # Image generate karna (Pollinations AI)
        image_prompt = "Hulk sitting at a Karachi food street eating biryani, cinematic lighting, 4k"
        img_url = f"https://image.pollinations.ai/prompt/{image_prompt.replace(' ', '_')}"
        img_data = requests.get(img_url).content
        with open("hulk_image.jpg", "wb") as f:
            f.write(img_data)
        print("Image saved as hulk_image.jpg")

    except Exception as e:
        print(f"Bot mein masla aya: {e}")

if __name__ == "__main__":
    start_bot()
