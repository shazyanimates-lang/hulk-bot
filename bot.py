import os
import requests
import time

def generate_script():
    print("🧠 Step 1: Gemini script likh raha hai...")
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
    prompt = {"contents": [{"parts": [{"text": "Write a funny Urdu story (500 chars) about Hulk in Karachi. Viral style."}]}]}
    try:
        r = requests.post(url, json=prompt)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Hulk Karachi mein bus rok raha hai!"

def generate_voice(script):
    print("🎙️ Step 2: ElevenLabs voice bana raha hai...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
    headers = {"xi-api-key": eleven_key, "Content-Type": "application/json"}
    data = {"text": script[:500], "model_id": "eleven_multilingual_v2"}
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        print("✅ Voice ready!")
        return True
    return False

def download_hulk():
    print("🖼️ Step 3: Hulk ki image download ho rahi hai...")
    # Seedha aur stable link
    img_url = "https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNl9hX3Bob3RvX29mX2FfZ3JlZW5fbXVzY3VsYXJfZ2lhbnRfaHVsa19pc19zdGFuZF9hYmMxMjBhNS0yMzdmLTRlZDEtYmIwYy02ZGRhYjgxMmU2ZjlfMS5qcGc.jpg"
    try:
        r = requests.get(img_url, timeout=20)
        with open("hulk.jpg", "wb") as f:
            f.write(r.content)
        print("✅ Hulk image ready!")
        return True
    except:
        return False

def create_video():
    print("🎬 Step 4: Rendering 90s Video (Looping Audio)...")
    # HARD LOCK: -stream_loop -1 (Audio repeat karega) aur -t 90 (Video length)
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg "
        "-stream_loop -1 -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest hulk_video.mp4"
    )
    os.system(cmd)
    if os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: 90s Video Created!")

if __name__ == "__main__":
    if generate_voice(generate_script()) and download_hulk():
        create_video()
    
