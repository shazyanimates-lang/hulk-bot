import requests
import os
import random
from gtts import gTTS

def generate_halku_pro_video():
    try:
        # Step 1: Har baar alag Trending Script
        print("⏳ Step 1: AI script generate kar raha hai...")
        trends = [
            "Halku ki Lamborghini entry aur Manager ka munh band",
            "Halku ne dushmanon ko dhool chata di",
            "Halku ne gareeb ki madad ki aur Karachi ka hero ban gaya"
        ]
        
        # Pollinations Text AI (Stable for Roman Urdu)
        query = f"Write a 90 seconds dramatic YouTube Short script in Roman Urdu about: {random.choice(trends)}. Use dialogues like 'Ae mote kahan ja raha hai'. Start directly with dialogues."
        try:
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=20)
            story = res.text if res.status_code == 200 else "Ae mote! Dekh meri Lamborghini! Ab bol kiska waqt hai?"
        except:
            story = "Manager: Ae mote nikal yahan se! Halku: Aaj huss lo mujh par, kal main badla lunga. Ye dekho meri Lamborghini!"

        # Step 2: Audio (gTTS)
        print("⏳ Step 2: Voice tayyar ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Fixed HD Hulk Image (No more errors)
        print("⏳ Step 3: Hulk image download ho rahi hai...")
        # Ye link direct aur stable hai, FFmpeg crash nahi hoga
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        r = requests.get(img_url)
        with open("hulk.jpg", "wb") as f:
            f.write(r.content)

        # Step 4: Final Video with Zoom/Movement
        print("⏳ Step 4: Video render ho rahi hai (1:30 min)...")
        # Is command se video move karegi, ruki hui nahi lagegi
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ SUCCESS: short_video.mp4 ban gayi hai!")
        else:
            print("❌ Error: Video file nahi mili.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_halku_pro_video()
    
