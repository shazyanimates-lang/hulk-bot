import os
import requests
import subprocess
from elevenlabs import save
from elevenlabs.client import ElevenLabs


def generate_90s_hulk_video():
    try:
        # STEP 1 — GEMINI SCRIPT
        print("🎬 Step 1: Gemini script generate kar raha hai...")

        gemini_key = os.getenv("GEMINI_API_KEY")

        # ✅ FIX: gemini-2.0-flash (old gemini-1.5-flash is DEAD)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_key}"

        payload = {
            "contents": [{
                "parts": [{
                    "text": "Write a funny 90 second YouTube Shorts script in Roman Urdu. Hulk is in Karachi fighting with a bus driver then buying the whole bus. Make it viral and funny."
                }]
            }]
        }

        res = requests.post(url, json=payload)

        # ✅ FIX: Error check added
        if res.status_code != 200:
            print(f"❌ Gemini API Error {res.status_code}:")
            print(res.text)
            return

        script_text = res.json()['candidates'][0]['content']['parts'][0]['text']
        print("✅ Script generated!")
        print("📝 Script preview:", script_text[:150], "...")

        # STEP 2 — ELEVENLABS VOICE
        print("🎙️ Step 2: Voice generate ho rahi hai...")

        client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        audio = client.generate(
            text=script_text,
            voice="Adam",
            model="eleven_multilingual_v2"
        )

        save(audio, "voice.mp3")
        print("✅ Voice ready!")

        # STEP 3 — DOWNLOAD IMAGE
        print("🖼️ Step 3: Image download ho rahi hai...")

        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"

        img_response = requests.get(img_url)
        if img_response.status_code != 200:
            print("❌ Image download failed!")
            return

        with open("hulk.jpg", "wb") as f:
            f.write(img_response.content)

        print("✅ Image ready!")

        # STEP 4 — VIDEO RENDER
        print("🎥 Step 4: Video render ho raha hai...")

        # ✅ FIX: Output filename matches workflow artifact path
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", "hulk.jpg",
            "-i", "voice.mp3",
            "-c:v", "libx264",
            "-t", "90",
            "-pix_fmt", "yuv420p",
            "-vf", "scale=1080:1920",
            "-c:a", "aac",
            "-shortest",
            "short_video.mp4"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print("❌ FFmpeg Error:", result.stderr)
            return

        print("✅ Video successfully created: short_video.mp4")

    except Exception as e:
        print("❌ Error:", e)


generate_90s_hulk_video()
