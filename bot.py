import os
import requests
import subprocess
from elevenlabs import save
from elevenlabs.client import ElevenLabs

def generate_90s_hulk_video():
    try:
        # STEP 1 — MANUA L SCRIPT (Gemini error se bachne ke liye)
        print("🎬 Step 1: Script process ho rahi hai...")
        
        # Ye script itni lambi hai ke 90 seconds tak chalegi
        script_text = (
            "Ae bus walay! Roko ye khatara! Hulk ko Karachi ki sarko par chalna hai! "
            "Bus driver: Abe ja na mote, rasta chorr! "
            "Hulk: Kya bola? Mote? Ab dekh, ye poori bus meri hai. Ye lo paisay aur niklo yahan se! "
            "Ab Hulk Karachi ka naya don hai aur ye CD-70 nahi, ye poori bus ab hawa mein uregi! "
            "Sab log rasta chorr do, warna Hulk ghussay mein sab kuch tor dega! "
            "Showroom walay ne gari nahi di, toh Hulk ne poori transport company kharid li. "
            "Ab bolo, kiska waqt hai? Karachi walay ho jao tayyar, Hulk aa gaya hai!"
        )

        # STEP 2 — ELEVENLABS VOICE
        print("🎙️ Step 2: ElevenLabs voice generate kar raha hai...")
        client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))
        audio = client.generate(text=script_text, voice="Adam", model="eleven_multilingual_v2")
        save(audio, "voice.mp3")

        # STEP 3 — IMAGE
        print("🖼️ Step 3: Image ready ho rahi hai...")
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)

        # STEP 4 — VIDEO RENDER (Force 90 Seconds)
        print("🎥 Step 4: Video render ho raha hai (90s)...")
        # Is baar hum loop ko audio ki length tak nahi balki pakka 90s rakhenge
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-i", "hulk.jpg", "-i", "voice.mp3",
            "-c:v", "libx264", "-t", "90", "-pix_fmt", "yuv420p",
            "-vf", "scale=1080:1920,setsar=1", "-c:a", "aac", "short_video.mp4"
        ]
        subprocess.run(cmd)
        print("✅ Video successfully created: short_video.mp4")

    except Exception as e:
        print("❌ Error:", e)

generate_90s_hulk_video()
