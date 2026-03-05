import os
import requests
import time

def generate_script():
    print("🧠 Generating AI script...")
    api_key = os.getenv("GEMINI_API_KEY")
    # v1 API ke liye gemini-2.5-flash sabse stable hai
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"

    # Choti script taaki credits bachein magar video lambi bane
    prompt = {
        "contents": [{"parts": [{"text": "Write a funny Urdu story under 700 characters. Hulk is in Karachi buying a bus and fighting a driver. Dramatic style."}]}]
    }

    r = requests.post(url, json=prompt)
    if r.status_code != 200:
        print(f"❌ Gemini Error: {r.text}")
        return None

    script = r.json()["candidates"][0]["content"]["parts"][0]["text"]
    print("✅ Script ready")
    return script

def generate_voice(script):
    print("🎙️ Generating voice...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    voice_id = "pNInz6obpgDQGcFmaJgB"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": eleven_key}
    
    # Quota check ke liye safety limit
    data = {"text": script[:700], "model_id": "eleven_multilingual_v2"}
    
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        print("✅ Voice ready")
        return True
    print(f"❌ ElevenLabs error: {r.text}")
    return False

def run_bot():
    print("🚀 AI Hulk Bot Starting...")
    
    script = generate_script()
    if not script: return

    if not generate_voice(script): return

    # STEP 3: FAIL-SAFE IMAGE DOWNLOAD
    print("🖼️ Downloading Hulk image...")
    img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
    try:
        img_data = requests.get(img_url, timeout=15).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)
        print("✅ Image ready")
    except Exception as e:
        print(f"❌ Image Download Failed: {e}")
        return

    # STEP 4: MANDATORY 90 SECONDS RENDER
    print("🎬 Rendering 90s video (Isme time lagega)...")
    time.sleep(2)
    
    # Force 90 seconds regardless of audio length
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac hulk_video.mp4"
    )
    
    exit_code = os.system(cmd)
    
    if exit_code == 0 and os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: hulk_video.mp4 is ready!")
    else:
        print("❌ Video rendering failed!")

if __name__ == "__main__":
    run_bot()
    
