import os
import requests
import google.generativeai as genai
from elevenlabs import save
from elevenlabs.client import ElevenLabs

def generate_hulk_pro_video():
    try:
        # 1. API Configuration
        print("⏳ Step 1: APIs connect ho rahi hain...")
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        client_11 = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        # 2. Gemini 1.5 Flash: Script Generation
        print("⏳ Step 2: Gemini 1.5 script generate kar raha hai...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "Write a 30-second funny viral YouTube Shorts script in Roman Urdu. Hulk is in a Karachi bike showroom trying to ride a CD-70. Use aggressive and funny dialogues."
        
        response = model.generate_content(prompt)
        script_text = response.text.strip()
        print(f"📜 Script: {script_text}")

        # 3. ElevenLabs: Voice Generation
        print("⏳ Step 3: ElevenLabs voice process kar raha hai...")
        audio = client_11.generate(
            text=script_text,
            voice="Adam",
            model="eleven_multilingual_v2"
        )
        save(audio, "voice.mp3")

        # 4. Image: HD Hulk Background
        print("⏳ Step 4: Hulk image ready kar raha hoon...")
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        img_data = requests.get(img_url).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)
        print("✅ Image Ready!")

        # 5. FFmpeg: Animation & Final Render
        print("⏳ Step 5: Final Video render ho rahi hai...")
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 30 "
            "-vf \"zoompan=z='min(zoom+0.001,1.3)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ MUBARAK: Video successfully ban gayi!")

    except Exception as e:
        print(f"❌ Error Detail: {e}")

if __name__ == "__main__":
    generate_hulk_pro_video()
    
