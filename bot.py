import requests
import os
import time
import random
from gtts import gTTS

def generate_viral_halku_video():
    try:
        print("⏳ Step 1: AI Trending Roman Urdu Script likh raha hai...")
        
        topics = [
            "Halku ne Karachi ki sadak par ek gareeb bache ki madad ki",
            "Manager ne Halku ko naukri se nikala, Hulk ne apni company khol li",
            "Halku ne Lamborghini kharid kar apne doston ko hairan kar diya"
        ]
        selected_theme = random.choice(topics)
        
        query = f"Write a long 1:30 minute viral YouTube Shorts script in Roman Urdu about: {selected_theme}. Use dramatic dialogues."
        
        # Script Generation
        try:
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=30)
            story = res.text if res.status_code == 200 else "Halku ne aaj sabko hairan kar diya!"
        except:
            story = "Waqt sabka badalta hai, aaj mera hai kal tera hoga!"

        # Step 2: Audio
        print("⏳ Step 2: Audio generate ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Image (With Safety Check)
        print("⏳ Step 3: AI Image download ho rahi hai...")
        img_url = f"https://image.pollinations.ai/prompt/3D_Pixar_style_cinematic_Hulk_in_Karachi_9_16?seed={random.randint(1,9999)}"
        
        # Retry loop agar image khali download ho
        for i in range(3): 
            img_res = requests.get(img_url, timeout=40)
            if img_res.status_code == 200 and len(img_res.content) > 1000:
                with open("hulk.jpg", "wb") as f:
                    f.write(img_res.content)
                print("✅ Image sahi se save ho gayi!")
                break
            else:
                print(f"⚠️ Image download fail hui, koshish {i+1}...")
                time.sleep(5)

        # Step 4: Final Video (Error handling ke saath)
        if os.path.exists("hulk.jpg") and os.path.getsize("hulk.jpg") > 0:
            print("⏳ Step 4: Video rendering (90 seconds)...")
            cmd = (
                "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 90 "
                "-preset fast -pix_fmt yuv420p -vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
                "-c:a aac -shortest short_video.mp4"
            )
            os.system(cmd)
            print("✅ SUCCESS: Video Taiyar!")
        else:
            print("❌ Error: Sahi image nahi mili, video nahi ban sakti.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_viral_halku_video()
    
