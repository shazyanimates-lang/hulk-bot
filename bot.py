import os
import requests
import time
from PIL import Image, ImageDraw

def generate_script():
    print("🧠 Script ban rahi hai...")
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
    prompt = {"contents": [{"parts": [{"text": "Write a funny Urdu story under 500 characters: Hulk is in Karachi fighting a bus driver. Viral style."}]}]}
    try:
        r = requests.post(url, json=prompt)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Hulk Karachi ki bus mein phans gaya!"

def generate_voice(script):
    print("🎙️ Voice ban rahi hai...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
    headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": eleven_key}
    data = {"text": script[:500], "model_id": "eleven_multilingual_v2"}
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        return True
    return False

def create_local_image():
    print("🖼️ Creating local Hulk image (No Download)...")
    img = Image.new('RGB', (1080, 1920), color = (0, 128, 0)) # Green Background
    d = ImageDraw.Draw(img)
    # Background image ready, no download needed
    img.save('hulk.jpg')
    print("✅ Local image ready")
    return True

def create_video():
    print("🎬 Rendering 90s video...")
    # Force 90 seconds video lock
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920,setsar=1\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac hulk_video.mp4"
    )
    os.system(cmd)
    if os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: Video tayyar hai!")

def run_bot():
    script = generate_script()
    if generate_voice(script) and create_local_image():
        create_video()

if __name__ == "__main__":
    run_bot()
    
