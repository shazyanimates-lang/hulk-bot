import requests
import os
import random
from gtts import gTTS
from PIL import Image

def generate_hulk_video():
    try:
        # Step 1: Script
        print("⏳ Step 1: Script likh raha hai...")
        trends = ["Halku in Karachi showroom", "Halku vs Rude Boss"]
        story = f"Halku: Ae mote! Dekh meri nayi Lamborghini! Manager: Maaf karna sir, aap toh king nikle!"
        
        # Step 2: Voice
        print("⏳ Step 2: Voice generate ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: HD Hulk Image (Fixed Source)
        print("⏳ Step 3: Downloading stable image...")
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        r = requests.get(img_url)
        with open("temp.jpg", "wb") as f:
            f.write(r.content)
            
        # Image fix for FFmpeg
        with Image.open("temp.jpg") as img:
            img.convert("RGB").save("hulk.jpg", "JPEG")
        print("✅ Image Ready!")

        # Step 4: Video Animation (90s)
        print("⏳ Step 4: Video render ho rahi hai...")
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        print("✅ SUCCESS: Video ban gayi!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_hulk_video()
    
