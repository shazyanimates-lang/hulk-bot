import os, requests
import google.generativeai as genai
from gtts import gTTS

# API Key check
api_key = os.environ.get("GEMINI_KEY")
genai.configure(api_key=api_key)

def start_bot():
    try:
        # Sabse stable model use kar rahe hain
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Test generation
        response = model.generate_content("Say 'Hulk is ready' in 1 line.")
        story = response.text
        
        # Audio & Image
        gTTS(text=story, lang='en').save("hulk.mp3")
        img_url = "https://image.pollinations.ai/prompt/hulk_karachi_city"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)
        
        print(f"DONE! Story: {story}")
    except Exception as e:
        print(f"STILL ERROR: {e}")

if __name__ == "__main__":
    start_bot()
    
