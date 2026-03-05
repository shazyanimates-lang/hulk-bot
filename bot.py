import os
import google.generativeai as genai
from elevenlabs import save
from elevenlabs.client import ElevenLabs

def generate_hulk_pro():
    try:
        # 1. Setup APIs (Direct Way)
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        client_11 = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        # 2. Gemini 1.5: Script Generation
        print("⏳ Step 1: Gemini 1.5 script likh raha hai...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = "Write a 30-second viral YouTube Shorts script in Roman Urdu. Hulk is in Karachi showroom buying a Lamborghini. Dramatic and funny dialogues."
        response = model.generate_content(prompt)
        script_text = response.text.strip()
        print(f"📜 Script: {script_text}")

        # 3. ElevenLabs: Voice Generation
        print("⏳ Step 2: ElevenLabs voice generate kar raha hai...")
        audio = client_11.generate(
            text=script_text,
            voice="Adam",
            model="eleven_multilingual_v2"
        )
        save(audio, "voice.mp3")

        # 4. Background (Hulk Image)
        # Link fix: Direct HD image use kar rahe hain
        import requests
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)
        print("✅ Image Ready!")

        # 5. FFmpeg: Final Video
        print("⏳ Step 3: Rendering Video...")
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 30 "
            "-vf \"zoompan=z='min(zoom+0.001,1.3)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        print("✅ MUBARAK: Video Tayyar!")

    except Exception as e:
        print(f"❌ Error Detail: {e}")

if __name__ == "__main__":
    generate_hulk_pro()
    
