import os
import requests
import google.generativeai as genai
from gtts import gTTS

# GitHub Secrets se API Key uthana
api_key = os.environ.get("GEMINI_KEY")

if not api_key:
    print("Error: GEMINI_KEY is missing in Secrets!")
else:
    genai.configure(api_key=api_key)

def start_bot():
    try:
        # AGAR FLASH NAHI CHAL RAHA TO YE STABLE MODEL HAI
        model = genai.GenerativeModel('gemini-pro') 
        
        print("Generating story...")
        response = model.generate_content("Hulk in Karachi 1 line story")
        story_text = response.text
        
        # Audio
        gTTS(text=story_text, lang='en').save("hulk.mp3")
        
        # Image
        img_url = "https://image.pollinations.ai/prompt/hulk_eating_biryani_karachi"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)
            
        print(f"SUCCESS! Story: {story_text}")
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    start_bot()
