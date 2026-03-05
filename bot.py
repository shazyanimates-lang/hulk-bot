import requests
import os
import random
from gtts import gTTS
from PIL import Image

def make_viral_video():
    try:
        # 1. Script (Dialogue Style)
        print("⏳ Step 1: Writing Script...")
        dialogues = [
            "Manager: Ae mote! Bahar nikal yahan se! Halku: Aaj nikal raha hoon, kal ye pura showroom kharidne aaunga. Yaad rakhna!",
            "Halku: Karachi ka king kaun? Sirf Halku! Aaj Lamborghini li hai, kal pura shehar apna hoga!",
            "Dost: Tu kuch nahi kar sakta mote. Halku: Ye dekh meri mehnat ka phal! Ab bol kiska waqt hai?"
        ]
        script = random.choice(dialogues)
        
        # 2. Voice
        print("⏳ Step 2: Generating Voice...")
        tts = gTTS(text=script, lang='hi')
        tts.save("voice.mp3")

        # 3. Hulk Image (HD & Stable)
        print("⏳ Step 3: Downloading & Fixing Image...")
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        r = requests.get(img_url)
        with open("raw.jpg", "wb") as f:
            f.write(r.content)
        
        # Ye step 'Invalid Data' error ko fix karta hai
        with Image.open("raw.jpg") as img:
            img.convert("RGB").save("hulk.jpg", "JPEG")
        print("✅ Image Ready!")

        # 4. Video Rendering (90 Seconds Animation)
        print("⏳ Step 4: Rendering Video...")
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ MUBARAK: Video ban gayi!")
        else:
            print("❌ Error: Video render nahi hui.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    make_viral_video()
    
