import requests
import os
import random
from gtts import gTTS
from PIL import Image

def generate_hulk_perfect_video():
    try:
        # Step 1: AI Trending Script (Har baar naya topic)
        print("⏳ Step 1: AI trendy dialogues soch raha hai...")
        trends = [
            "Halku's grand entry in a Lamborghini",
            "Halku teaches a lesson to a rude rich man",
            "Halku helps a poor person and becomes a hero"
        ]
        
        # Text AI stable hai, isey use kar rahe hain trendy script ke liye
        query = f"Write a 90 seconds dramatic YouTube Short script in Roman Urdu about: {random.choice(trends)}. Use dialogues like 'Ae mote kahan ja raha hai'. Start directly with dialogues."
        try:
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=20)
            story = res.text if res.status_code == 200 else "Ae mote! Dekh meri Lamborghini! Ab bol kiska waqt hai?"
        except:
            story = "Manager: Ae mote nikal yahan se! Halku: Aaj huss lo mujh par, kal main badla lunga. Ye dekho meri Lamborghini!"

        # Step 2: Audio (gTTS)
        print("⏳ Step 2: Voice generate ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Fixed Stable Image (No AI Image Generator)
        print("⏳ Step 3: Hulk image download aur fix ho rahi hai...")
        # Ye direct link hai, isme kabhi 'Invalid Data' nahi aayega
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        r = requests.get(img_url)
        with open("raw_hulk.jpg", "wb") as f:
            f.write(r.content)
            
        # Image ko re-save karna taaki FFmpeg ko koi shak na rahe
        with Image.open("raw_hulk.jpg") as img:
            img.convert("RGB").save("hulk.jpg", "JPEG")
        print("✅ Image 100% Ready!")

        # Step 4: Final Video with Movement
        print("⏳ Step 4: Video render ho rahi hai (1:30 min)...")
        # Zoompan se image video ki tarah move karegi
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ MUBARAK: short_video.mp4 tayyar hai!")
        else:
            print("❌ Error: Video abhi bhi nahi bani.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_hulk_perfect_video()
    
