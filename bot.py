import requests
import os
import time
from gtts import gTTS

def generate_video():
    try:
        # Step 1: Kahani (With Timeout)
        print("⏳ Step 1: Generating story...")
        try:
            story_res = requests.get("https://text.pollinations.ai/Hulk_funny_Karachi_joke_1_line", timeout=15)
            story = story_res.text if story_res.status_code == 200 else "Hulk is looking for biryani!"
        except:
            story = "Hulk is very hungry in Karachi!"
        
        print(f"Story: {story}")

        # Step 2: Audio
        print("⏳ Step 2: Saving Audio...")
        tts = gTTS(text=story, lang='en')
        tts.save("voice.mp3")

        # Step 3: AI Image (With Timeout)
        print("⏳ Step 3: Getting AI Image...")
        img_url = f"https://image.pollinations.ai/prompt/Hulk_eating_biryani_9_16_{int(time.time())}"
        try:
            img_data = requests.get(img_url, timeout=20).content
            with open("hulk.jpg", "wb") as f:
                f.write(img_data)
        except:
            print("⚠️ Image generator slow hai, default use kar rahe hain.")
            # Agar image na mile toh ye script ko rukne nahi dega

        # Step 4: Video (The Final Force)
        print("⏳ Step 4: Creating Video...")
        # '-y' aur '-preset ultrafast' taaki jaldi khatam ho
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 10 "
            "-preset ultrafast -pix_fmt yuv420p "
            "-vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        print("✅ SUCCESS: Video Created!")

    except Exception as e:
        print(f"❌ Critical Error: {e}")

if __name__ == "__main__":
    generate_video()
