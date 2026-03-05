import requests
import os
import random
from gtts import gTTS
from PIL import Image

def generate_hulk_action_video():
    try:
        # Step 1: AI Trending Script (Roman Urdu)
        print("⏳ Step 1: Hulk ke liye trendy dialogues likhe ja rahe hain...")
        trends = ["Hulk in Karachi", "Hulk vs Arrogant Manager", "Hulk buying Lamborghini"]
        query = f"Write a viral 90s YouTube Shorts script in Roman Urdu about: {random.choice(trends)}. Use aggressive dialogues like 'Ae mote kahan ja raha hai'. Start directly with dialogues."
        
        try:
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=25)
            story = res.text if res.status_code == 200 else "Ae mote! Dekh meri Lamborghini! Ab bol kiska waqt hai?"
        except:
            story = "Manager: Ae mote nikal yahan se! Halku: Aaj huss lo mujh par, kal main badla lunga. Ye dekho meri Lamborghini!"

        # Step 2: Audio (gTTS)
        print("⏳ Step 2: Voice generate ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Proper Hulk Image (Replacing unstable AI)
        print("⏳ Step 3: HD Hulk Image download ho rahi hai...")
        # Direct stable link taaki 'Invalid Data' na aaye
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        r = requests.get(img_url)
        with open("temp_hulk.jpg", "wb") as f:
            f.write(r.content)
            
        # Image Fix: FFmpeg ke liye image format sahi karna
        with Image.open("temp_hulk.jpg") as img:
            img.convert("RGB").save("hulk.jpg", "JPEG")
        print("✅ Hulk Image Ready!")

        # Step 4: Full Animation Video (90 Seconds)
        print("⏳ Step 4: Video rendering with Zoom Animation...")
        # zoompan filter se image move karegi (animation effect)
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ SUCCESS: Hulk video tayyar hai!")
        else:
            print("❌ Error: Video file nahi mili.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_hulk_action_video()
    
