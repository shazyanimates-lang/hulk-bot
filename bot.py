import os
import requests
import time

def generate_script():
    print("🧠 Generating AI script...")
    api_key = os.getenv("GEMINI_API_KEY")
    # v1 API ke liye gemini-2.5-flash
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"

    # Prompt ko thoda short rakha hai taaki ElevenLabs credits bachein
    prompt = {
        "contents": [{"parts": [{"text": "Write a funny Urdu story. Hulk is in Karachi fighting a bus driver. Keep it under 800 characters but very funny."}]}]
    }

    r = requests.post(url, json=prompt)
    if r.status_code != 200:
        print("❌ Gemini Error:", r.text)
        return None

    data = r.json()
    script = data["candidates"][0]["content"]["parts"][0]["text"]
    print("✅ Script ready")
    return script

def generate_voice(script):
    print("🎙️ Generating voice...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    voice_id = "pNInz6obpgDQGcFmaJgB"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": eleven_key}
    
    # Text ko mazeed trim kar diya taaki quota exceeds na ho
    data = {"text": script[:800], "model_id": "eleven_multilingual_v2"}
    
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        print("✅ Voice ready")
        return True
    else:
        print(f"❌ ElevenLabs error: {r.text}")
        return False

def download_image():
    print("🖼️ Downloading Hulk image...")
    img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
    r = requests.get(img_url)
    if r.status_code == 200:
        with open("hulk.jpg", "wb") as f:
            f.write(r.content)
        print("✅ Image ready")
        return True
    return False

def create_video():
    print("🎬 Rendering video...")
    time.sleep(2)
    # '-t 90' video ko 90s tak kheenchega chahe voice choti ho
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac hulk_video.mp4"
    )
    os.system(cmd)
    if os.path.exists("hulk_video.mp4"):
        print("🎉 Video created successfully!")
    else:
        print("❌ Video creation failed")

def run_bot():
    print("🚀 AI Hulk Bot Starting...")
    script = generate_script()
    if not script: return
    if not generate_voice(script): return
    if not download_image(): return
    create_video()

if __name__ == "__main__":
    run_bot()
    
