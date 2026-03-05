import os
import requests
import time

def generate_script():
    print("🧠 Generating AI script...")
    api_key = os.getenv("GEMINI_API_KEY")
    # v1 API ke liye gemini-2.5-flash sabse stable hai
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"

    prompt = {
        "contents": [{"parts": [{"text": "Write a funny 90 second YouTube Shorts script in Roman Urdu. Hulk is in Karachi fighting with a bus driver then buying the whole bus."}]}]
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
    data = {"text": script, "model_id": "eleven_multilingual_v2"}
    r = requests.post(url, json=data, headers=headers)
    if r.status_code != 200:
        print("❌ ElevenLabs error:", r.text)
        return False
    with open("voice.mp3", "wb") as f:
        f.write(r.content)
    print("✅ Voice ready")
    return True

def download_image():
    print("🖼️ Downloading Hulk image...")
    # Direct high-quality image link
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
    time.sleep(5) # File system sync ke liye intezar
    
    # FFmpeg command optimized for GitHub Actions
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest hulk_video.mp4"
    )
    
    status = os.system(cmd)
    
    if status == 0 and os.path.exists("hulk_video.mp4"):
        print("🎉 Video created successfully: hulk_video.mp4")
    else:
        print("❌ Video creation failed or FFmpeg crashed")

def run_bot():
    print("🚀 AI Hulk Bot Starting...")
    script = generate_script()
    if not script: return
    if not generate_voice(script): return
    if not download_image(): return
    create_video()

if __name__ == "__main__":
    run_bot()
    
