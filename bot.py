import requests
import os
import time
import random
from gtts import gTTS

def generate_viral_video():
    try:
        print("⏳ Step 1: Script likhi ja rahi hai...")
        story = "Halku ne aaj Karachi ki biryani khai aur bola, ye toh kamaal hai bhai! Phir usne Lamborghini li aur nikal gaya."
        
        # Audio
        print("⏳ Step 2: Voice tayyar ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Image (Direct URL taaki download fail na ho)
        print("⏳ Step 3: Image check...")
        img_url = "https://image.pollinations.ai/prompt/3D_Pixar_style_Hulk_in_Karachi_9_16?seed=123"
        r = requests.get(img_url)
        with open("hulk.jpg", "wb") as f:
            f.write(r.content)

        # Step 4: Video (Iska naam exact 'short_video.mp4' hona chahiye)
        print("⏳ Step 4: Video render ho rahi hai (90 seconds)...")
        # Maine preset 'ultrafast' kar diya hai taaki jaldi bane
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 90 "
            "-preset ultrafast -pix_fmt yuv420p "
            "-vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        # Check if file exists
        if os.path.exists("short_video.mp4"):
            print("✅ SUCCESS: short_video.mp4 ban gayi hai!")
        else:
            print("❌ ERROR: Video file nahi mili!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_viral_video()
    
