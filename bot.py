import os
import requests
import random
from elevenlabs import save
from elevenlabs.client import ElevenLabs
from google import genai
from google.genai import types

def generate_viral_content():
    try:
        # 1. Setup APIs
        client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        client_11 = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        # 2. Gemini: Trending Script Generation
        print("⏳ Step 1: Gemini trending script likh raha hai...")
        script_prompt = (
            "Write a viral 40-second YouTube Shorts script in Roman Urdu. "
            "Topic: Hulk in a funny or dramatic situation in a local Pakistani setting (like Karachi or Lahore). "
            "Use aggressive and funny dialogues like 'Ae mote kahan ja raha hai'. "
            "Output only the dialogues, no scene descriptions."
        )
        
        script_response = client_gemini.models.generate_content(
            model="gemini-2.0-flash",
            contents=[script_prompt]
        )
        script_text = script_response.text.strip()
        print(f"📜 Script: {script_text}")

        # 3. Gemini: Image Generation (Based on Script)
        print("⏳ Step 2: Gemini image generate kar raha hai...")
        image_prompt = f"Cinematic 3D render, Hulk in a realistic Pakistani street or showroom, high detail, 9:16 aspect ratio, based on this: {script_text}"
        
        image_response = client_gemini.models.generate_content(
            model="gemini-2.0-flash", 
            contents=[image_prompt],
            config=types.GenerateContentConfig(response_modalities=["IMAGE"])
        )
        
        for part in image_response.parts:
            if part.inline_data:
                image = part.as_image()
                image.save("hulk.jpg")
        print("✅ Image Ready!")

        # 4. ElevenLabs: Voice Generation
        print("⏳ Step 3: ElevenLabs voice generate kar raha hai...")
        audio = client_11.generate(
            text=script_text,
            voice="Adam", # "Adam" best hai Hulk type vibes ke liye
            model="eleven_multilingual_v2"
        )
        save(audio, "voice.mp3")
        print("✅ Voice Ready!")

        # 5. FFmpeg: Final Animation & Video
        print("⏳ Step 4: Rendering Final Video...")
        # '-t 45' taaki video shorts ke liye perfect length ki bane
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 45 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        print("✅ SUCCESS: Pro Video Tayyar Hai!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_viral_content()
    
