import os
import requests
import subprocess
from elevenlabs import save
from elevenlabs.client import ElevenLabs


def generate_90s_hulk_video():
    try:
        # STEP 1 — GEMINI SCRIPT
        print("Step 1: Gemini script generate kar raha hai...")

        gemini_key = os.getenv("GEMINI_API_KEY")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"

        payload = {
            "contents": [{
                "parts": [{
                    "text": "Write a funny 90 second YouTube Shorts script in Roman Urdu. Hulk is in Karachi fighting with a bus driver then buying the whole bus. Make it viral and funny."
                }]
            }]
        }

        res = requests.post(url, json=payload)
        script_text = res.json()['candidates'][0]['content']['parts'][0]['text']

        print("Script generated!")

        # STEP 2 — ELEVENLABS VOICE
        print("Step 2: Voice generate ho rahi hai...")

        client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        audio = client.generate(
            text=script_text,
            voice="Adam",
            model="eleven_multilingual_v2"
        )

        save(audio, "voice.mp3")

        print("Voice ready!")

        # STEP 3 — DOWNLOAD IMAGE
        print("Step 3: Image download ho rahi hai...")

        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"

        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)

        print("Image ready!")

        # STEP 4 — VIDEO RENDER
        print("Step 4: Video render ho raha hai...")

        cmd = [
            "ffmpeg",
            "-loop", "1",
            "-i", "hulk.jpg",
            "-i", "voice.mp3",
            "-c:v", "libx264",
            "-t", "90",
            "-pix_fmt", "yuv420p",
            "-vf", "scale=1080:1920",
            "-c:a", "aac",
            "-shortest",
            "final_video.mp4"
        ]

        subprocess.run(cmd)

        print("Video successfully created: final_video.mp4")

    except Exception as e:
        print("Error:", e)


generate_90s_hulk_video()
