import os
import requests
import subprocess


# ---------------------------
# 1. AI SCRIPT (TREND STYLE)
# ---------------------------

def generate_script():

    print("🧠 Generating AI script...")

    api_key = os.getenv("GEMINI_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    prompt = {
        "contents":[
            {
                "parts":[
                    {
                        "text": """
Write a 90 second funny Hulk story in Urdu for YouTube Shorts.

Style:
- Inspired by trending YouTube Shorts humor
- Very dramatic
- Very funny
- Viral style storytelling
- Use simple Urdu

Topic example:
Hulk in Karachi doing something crazy.
Make it highly entertaining.
"""
                    }
                ]
            }
        ]
    }

    r = requests.post(url, json=prompt)

    if r.status_code != 200:
        print("❌ Gemini Error:", r.text)
        return None

    data = r.json()

    script = data["candidates"][0]["content"]["parts"][0]["text"]

    print("✅ Script ready")

    return script


# ---------------------------
# 2. VOICE GENERATION
# ---------------------------

def generate_voice(script):

    print("🎙️ Generating voice...")

    eleven_key = os.getenv("ELEVEN_API_KEY")

    voice_id = "pNInz6obpgDQGcFmaJgB"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": eleven_key
    }

    data = {
        "text": script,
        "model_id": "eleven_multilingual_v2"
    }

    r = requests.post(url, json=data, headers=headers)

    if r.status_code != 200:
        print("❌ ElevenLabs error:", r.text)
        return False

    with open("voice.mp3", "wb") as f:
        f.write(r.content)

    print("✅ Voice ready")

    return True


# ---------------------------
# 3. IMAGE DOWNLOAD
# ---------------------------

def download_image():

    print("🖼️ Downloading Hulk image...")

    img_url = "https://images.unsplash.com/photo-1608889175123-8ee362201f81"

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(img_url, headers=headers)

    if r.status_code != 200:
        print("❌ Image download failed")
        return False

    with open("hulk.jpg", "wb") as f:
        f.write(r.content)

    print("✅ Image ready")

    return True


# ---------------------------
# 4. VIDEO RENDER
# ---------------------------

def create_video():

    print("🎬 Rendering video...")

    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", "hulk.jpg",
        "-i", "voice.mp3",
        "-t", "90",
        "-vf", "scale=1080:1920,setsar=1",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "hulk_video.mp4"
    ]

    subprocess.run(cmd)

    if os.path.exists("hulk_video.mp4"):
        print("🎉 Video created successfully!")
    else:
        print("❌ Video creation failed")


# ---------------------------
# MAIN BOT
# ---------------------------

def run_bot():

    print("🚀 AI Hulk Bot Starting...")

    script = generate_script()

    if not script:
        return

    print("\n📜 SCRIPT:\n")
    print(script)

    if not generate_voice(script):
        return

    if not download_image():
        return

    create_video()


if __name__ == "__main__":
    run_bot()
