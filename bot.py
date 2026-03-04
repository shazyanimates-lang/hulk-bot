import os, requests
from gtts import gTTS
import google.generativeai as genai

# Gemini Setup
genai.configure(api_key=os.environ["GEMINI_KEY"])

def start_bot():
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    # AI se story likhwana
    story = model.generate_content("Write a 1-sentence epic Hulk line for Karachi streets").text
    
    # Audio aur Image banana
    gTTS(text=story, lang='en').save("hulk.mp3")
    img_data = requests.get("https://image.pollinations.ai/prompt/angry_hulk_karachi").content
    with open("hulk.jpg", "wb") as f: f.write(img_data)
    
    # Telegram par bhejna (Ye sabse asaan automation hai)
    send_to_telegram("hulk.mp3", "hulk.jpg", story)

def send_to_telegram(audio, photo, text):
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    files = {'photo': open(photo, 'rb'), 'audio': open(audio, 'rb')}
    requests.post(f"https://api.telegram.org/bot{token}/sendPhoto", data={'chat_id': chat_id, 'caption': text}, files={'photo': open(photo, 'rb')})

if __name__ == "__main__":
    start_bot()
  
