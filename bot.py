import os
import requests
import time

def generate_script():
    print("🧠 Step 1: Script process ho rahi hai...")
    api_key = os.getenv("GEMINI_API_KEY")
    # v1 API ke liye gemini-2.5-flash
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
    prompt = {"contents": [{"parts": [{"text": "Write a funny 90s style Urdu story (600 chars) about Hulk in Karachi fighting a bus driver."}]}]}
    try:
        r = requests.post(url, json=prompt)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Hulk Karachi ki bus mein phans gaya aur driver se larnay laga!"

def generate_voice(script):
    print("🎙️ Step 2: ElevenLabs voice generate kar raha hai...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
    headers = {"xi-api-key": eleven_key, "Content-Type": "application/json"}
    # Credit limit check
    data = {"text": script[:600], "model_id": "eleven_multilingual_v2"}
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        print("✅ Voice ready!")
        return True
    return False

def download_hulk():
    print("🖼️ Step 3: Hulk ki image dhoond raha hoon...")
    # Stable Hulk image URL
    img_url = "https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNl9hX3Bob3RvX29mX2FfZ3JlZW5fbXVzY3VsYXJfZ2lhbnRfaHVsa19pc19zdGFuZF9hYmMxMjBhNS0yMzdmLTRlZDEtYmIwYy02ZGRhYjgxMmU2ZjlfMS5qcGc.jpg"
    try:
        r = requests.get(img_url, timeout=20)
        if r.status_code == 200:
            with open("hulk.jpg", "wb") as f:
                f.write(r.content)
            print("✅ Hulk image downloaded!")
            return True
    except:
        print("❌ Image fail ho gayi")
    return False

def create_video():
    print("🎬 Step 4: Video render ho rahi hai (90 Seconds Lock)...")
    # Video length force 90 seconds
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -b:a 192k hulk_video.mp4"
    )
    os.system(cmd)
    if os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: 90s Video ready!")

if __name__ == "__main__":
    script = generate_script()
    if generate_voice(script) and download_hulk():
        create_video()
        
