import os
import requests
import time

def generate_script():
    print("🧠 Generating AI script...")
    api_key = os.getenv("GEMINI_API_KEY")
    # v1 API ke liye gemini-2.5-flash sabse stable hai
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"

    # Choti script taaki credits bachein
    prompt = {
        "contents": [{"parts": [{"text": "Write a funny Urdu story under 600 characters about Hulk in Karachi. Dramatic and viral style."}]}]
    }

    try:
        r = requests.post(url, json=prompt)
        script = r.json()["candidates"][0]["content"]["parts"][0]["text"]
        print("✅ Script ready")
        return script
    except:
        return "Hulk Karachi mein bus chala raha hai aur sab darr gaye hain!"

def generate_voice(script):
    print("🎙️ Generating voice...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    voice_id = "pNInz6obpgDQGcFmaJgB"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": eleven_key}
    
    # 600 chars limit taaki quota exceed na ho
    data = {"text": script[:600], "model_id": "eleven_multilingual_v2"}
    
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        print("✅ Voice ready")
        return True
    print(f"❌ ElevenLabs error: {r.text}")
    return False

def download_image():
    print("🖼️ Downloading Hulk image (Secure Stream)...")
    # New Stable Image Link
    img_url = "https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNl9hX3Bob3RvX29mX2FfZ3JlZW5fbXVzY3VsYXJfZ2lhbnRfaHVsa19pc19zdGFuZF9hYmMxMjBhNS0yMzdmLTRlZDEtYmIwYy02ZGRhYjgxMmU2ZjlfMS5qcGc.jpg"
    try:
        r = requests.get(img_url, stream=True, timeout=20)
        if r.status_code == 200:
            with open("hulk.jpg", "wb") as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            print("✅ Image ready and verified")
            return True
    except Exception as e:
        print(f"❌ Image Error: {e}")
    return False

def create_video():
    print("🎬 Rendering 90s video (Force Render)...")
    time.sleep(3)
    
    if not os.path.exists("hulk.jpg") or not os.path.exists("voice.mp3"):
        print("❌ Files missing, can't render!")
        return

    # Pakka 90 seconds video rendering
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -b:a 192k hulk_video.mp4"
    )
    
    exit_code = os.system(cmd)
    
    if exit_code == 0 and os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: Video is ready!")
    else:
        print(f"❌ FFmpeg failed with code {exit_code}")

def run_bot():
    print("🚀 Hulk Bot 2.0 Starting...")
    script = generate_script()
    if generate_voice(script) and download_image():
        create_video()

if __name__ == "__main__":
    run_bot()
                
