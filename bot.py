import os
import requests
import time
from elevenlabs import save
from elevenlabs.client import ElevenLabs
from google import genai
from google.genai import types

def generate_viral_content():
    try:
        # 1. Setup APIs
        client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        client_11 = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

        # 2. Gemini: Script (Using 1.5 Flash for Stability)
        print("⏳ Step 1: Gemini 1.5 script likh raha hai...")
        script_prompt = (
            "Write a funny 30-second YouTube Shorts script in Roman Urdu. "
            "Hulk is in Karachi showroom buying a car. Aggressive and funny dialogues."
        )
        
        # Yahan model change kar diya hai
        script_response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=[script_prompt]
        )
        script_text = script_response.text.strip()
        print(f"📜 Script: {script_text}")

        time.sleep(2) # Chota sa break taaki 429 error na aaye

        # 3. Gemini: Image Generation
        print("⏳ Step 2: Gemini image generate kar raha hai...")
        image_prompt = f"Cinematic 3D render, Hulk in a Karachi showroom, 9:16 aspect ratio, based on: {script_text}"
        
        image_response = client_gemini.models.generate_content(
            model="gemini-1.5-flash",
            contents=[image_prompt],
            config=types.GenerateContentConfig(response_modalities=["IMAGE"])
        )
        
        for part in image_response.parts:
            if part.inline_data:
                image = part.as_image()
                image.save("hulk.jpg")
        print("✅ Image Ready!")

        # 4. ElevenLabs: Voice
        print("⏳ Step 3: ElevenLabs voice...")
        audio = client_11.generate(
            text=script_text,
            voice="Adam",
            model="eleven_multilingual_v2"
        )
        save(audio, "voice.mp3")

        # 5. Rendering
        print("⏳ Step 4: Rendering...")
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 30 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        print("✅ SUCCESS!")

    except Exception as e:
        print(f"❌ Error Detail: {e}")

if __name__ == "__main__":
    generate_viral_content()
    
