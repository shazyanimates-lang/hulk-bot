import requests
import os
import time
from gtts import gTTS

def generate_video():
    try:
        print("⏳ Step 1: Getting Story...")
        story = "Hulk is having a great time in Karachi eating biryani!"
        
        print("⏳ Step 2: Saving Audio...")
        tts = gTTS(text=story, lang='en')
        tts.save("voice.mp3")

        print("⏳ Step 3: Getting AI Image...")
        img_url = f"https://image.pollinations.ai/prompt/Hulk_eating_biryani_in_Karachi_9_16_{int(time.time())}"
        img_data = requests.get(img_url).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        print("⏳ Step 4: Creating Video...")
        # '-y' is the magic word here
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 10 "
            "-pix_fmt yuv420p -vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        print("✅ SUCCESS: short_video.mp4 created!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_video()
