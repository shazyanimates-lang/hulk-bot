import requests
import os
import time
import random
from gtts import gTTS

def generate_viral_video():
    try:
        # Step 1: Trending Script (Text AI is usually stable)
        print("⏳ Step 1: AI script likh raha hai...")
        query = "Write a long dramatic 1:30 minute viral story in Roman Urdu about Hulk buying a Lamborghini in Karachi and showing it to his jealous friends."
        try:
            # Text generator aksar phasta nahi hai
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=20)
            story = res.text if res.status_code == 200 else "Hulk ne Karachi mein Lamborghini le li!"
        except:
            story = "Manager ne kaha tum gareeb ho, Hulk ne kaha dekhna ek din main Lamborghini launga. Phir Hulk ne mehnat ki aur apni shandaar car le aya."

        # Step 2: Audio
        print("⏳ Step 2: Voice generate ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Reliable Image (Replacing Pollinations Image AI)
        print("⏳ Step 3: Downloading stable image...")
        # Hum 'Lorem Flickr' use kar rahe hain jo seedha image deta hai, koi data error nahi aata
        img_url = f"https://loremflickr.com/1080/1920/hulk,car,action?lock={random.randint(1,1000)}"
        
        img_data = requests.get(img_url).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)
        print("✅ Image Ready!")

        # Step 4: Final Video (90 Seconds)
        print("⏳ Step 4: Video render ho rahi hai...")
        # 'ultrafast' taaki GitHub jaldi se video bana kar free ho jaye
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 90 "
            "-preset ultrafast -pix_fmt yuv420p "
            "-vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ SUCCESS: Video ban gayi!")
        else:
            print("❌ Error: Video file nahi mili.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_viral_video()
    
