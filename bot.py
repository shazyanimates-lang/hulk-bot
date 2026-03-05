import os
import requests
import time

def generate_script():
    print("🧠 Script likh raha hoon...")
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
    prompt = {"contents": [{"parts": [{"text": "Write a funny Urdu story (600 chars) about Hulk fighting a bus driver in Karachi."}]}]}
    try:
        r = requests.post(url, json=prompt)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Hulk Karachi mein bus rok raha hai!"

def generate_voice(script):
    print("🎙️ Voice generate ho rahi hai...")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
    headers = {"xi-api-key": eleven_key, "Content-Type": "application/json"}
    # Voice length check
    data = {"text": script[:600], "model_id": "eleven_multilingual_v2"}
    r = requests.post(url, json=data, headers=headers)
    if r.status_code == 200:
        with open("voice.mp3", "wb") as f:
            f.write(r.content)
        return True
    return False

def download_hulk():
    print("🖼️ Hulk ki image download ho rahi hai...")
    # Real Hulk Image Link
    img_url = "https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNl9hX3Bob3RvX29mX2FfZ3JlZW5fbXVzY3VsYXJfZ2lhbnRfaHVsa19pc19zdGFuZF9hYmMxMjBhNS0yMzdmLTRlZDEtYmIwYy02ZGRhYjgxMmU2ZjlfMS5qcGc.jpg"
    try:
        r = requests.get(img_url, timeout=20)
        if r.status_code == 200:
            with open("hulk.jpg", "wb") as f:
                f.write(r.content)
            print("✅ Hulk image ready!")
            return True
    except:
        print("❌ Image download failed")
    return False

def create_video():
    print("🎬 Rendering 90s Video (HARD LOCK)...")
    # Loop image to force 90 seconds even if audio is short
    cmd = (
        "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
        "-vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920\" "
        "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -b:a 192k hulk_video.mp4"
    )
    os.system(cmd)
    if os.path.exists("hulk_video.mp4"):
        print("🎉 SUCCESS: 90s Hulk Video Ready!")

if __name__ == "__main__":
    if generate_voice(generate_script()) and download_hulk():
        create_video()
        
