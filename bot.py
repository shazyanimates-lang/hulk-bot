import os, requests
from gtts import gTTS
import google.generativeai as genai

# API Key Secrets se ayegi
genai.configure(api_key=os.environ["GEMINI_KEY"])

def start_bot():
    try:
        # Version ka masla khatam karne ke liye simple name
        model = genai.GenerativeModel('gemini-pro') 
        story = model.generate_content("Hulk in Karachi 1 line epic story").text
        
        # Audio & Image creation
        gTTS(text=story, lang='en').save("hulk.mp3")
        img_url = "https://image.pollinations.ai/prompt/hulk_karachi_street"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)
        
        print(f"Success! Story: {story}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_bot()
    
