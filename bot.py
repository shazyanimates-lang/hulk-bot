import os, requests
import google.generativeai as genai
from gtts import gTTS

# API Key configuration
genai.configure(api_key=os.environ["GEMINI_KEY"])

def start_bot():
    try:
        # Sabse stable model call kar rahe hain
        model = genai.GenerativeModel('gemini-pro') 
        response = model.generate_content("Hulk in Karachi 1 line story")
        story = response.text
        
        # Files banana
        gTTS(text=story, lang='en').save("hulk.mp3")
        img_url = "https://image.pollinations.ai/prompt/hulk_karachi_street"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)
        
        print(f"Success! Story: {story}")
    except Exception as e:
        print(f"Error Detail: {e}")

if __name__ == "__main__":
    start_bot()
    
