import os
import requests
import time
from PIL import Image, ImageDraw

def generate_script():
    print("🧠 Step 1: Script generate ho rahi hai...")
    api_key = os.getenv("GEMINI_API_KEY")
    # v1 API ke liye gemini-2.5-flash sabse stable hai
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
    prompt = {"contents": [{"parts": [{"text": "Write a funny Urdu story under 500 characters: Hulk is in Karachi fighting a bus driver. Viral style."}]}]}
    try:
        r = requests.post(url, json=prompt)
        script = r.json()["candidates"][0]["content"]["parts"][0]["text"]
        print("✅ Script Ready!")
        return script
    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return "Hulk Karachi ki bus mein phans gaya!"

def generate_voice(script):
    print("🎙️ Step 2: Voice generate ho rahi hai...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
    headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": eleven_key}
    # Quota check ke liye limit
    data = {"text": script[:500], "model_id": "eleven_multilingual_v2"}
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        print("✅ Voice Ready!")
        return True
    print(f"❌ ElevenLabs Error: {r.text}")
    return False

def create_local_image():
    print("🖼️ Step 3: Creating local background (No Download)...")
    # 1080x1920 ki green image khud bana raha hoon taaki download error na aaye
    img = Image.new('RGB', (1080, 1920), color = (20, 150, 20)) 
    img.save('hulk.jpg')
    print("✅ Image Created!")
    return True

def create_video():
    print("🎬 Step 4: Video render ho rahi hai (90 Seconds)...")
    time.sleep(2)
    # Force 90 seconds video lock
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920,setsar=1\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest hulk_video.mp4"
    )
    os.system(cmd)
    if os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: hulk_video.mp4 tayyar hai!")
    else:
        print("❌ FFmpeg failed to create video.")

def run_bot():
    print("🚀 Hulk Bot Starting...")
    script = generate_script()
    if generate_voice(script) and create_local_image():
        create_video()

if __name__ == "__main__":
    run_bot()
    
