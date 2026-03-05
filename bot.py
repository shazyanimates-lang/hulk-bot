import requests
import os
import time
import random
from gtts import gTTS

def generate_viral_halku_video():
    try:
        print("⏳ Step 1: AI Trending Roman Urdu Script likh raha hai...")
        
        # Viral YouTube Trends for Halku
        topics = [
            "Halku ki purani kabaar car dekh kar ameer doston ne uska mazak udaya, Halku ne agle din Lamborghini kharid kar unka munh band kar diya.",
            "Halku ko ek lachaar gareeb bacha mila jisne 3 din se khana nahi khaya tha, Halku ne usey 5 star hotel mein khana khilaya.",
            "Manager ne Halku ko naukri se nikal diya kyunki woh mota tha, lekin Halku ne apni khud ki company khol kar Manager ko hi naukri par rakh liya.",
            "Halku ne ek wrestling ring mein ja kar bade bade pehalwanon ko dhool chata di aur 20 crore ka inaam jeeta."
        ]
        selected_theme = random.choice(topics)
        
        # AI ko Smart Prompt dena taaki 1:30 min ki lambi script mile
        query = (
            f"Write a very long and dramatic 1:30 minute viral YouTube Shorts script in Roman Urdu (Hindustani style). "
            f"Theme: {selected_theme}. "
            f"Start with a sad dialogue, then a struggle, and then a grand success (victory). "
            f"Include dialogues like 'Ae mote kahan ja raha hai', 'Dekhna main ek din bada aadmi banunga', 'Ye le Lamborghini ki chaabi'."
        )
        
        try:
            # AI se 90 seconds layak lambi script mangwana
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=40)
            story = res.text if res.status_code == 200 else "Halku ne aaj sabko hairan kar diya!"
        except:
            # Fallback agar AI slow ho
            story = (
                "Manager ne bola ae mote nikal yahan se, tere paas cycle tak nahi. "
                "Halku ki aankhon mein aansu aa gaye, usne thaan liya ke woh badla lega. "
                "Din raat mehnat ki, aur agle hi hafte 20 crore ki Lamborghini showroom se nikal li. "
                "Manager hairan reh gaya aur Halku ne kaha: Waqt sabka badalta hai!"
            )

        print(f"🎬 Script Ready: {story[:150]}...")

        # Step 2: Audio (Long Duration)
        print("⏳ Step 2: Audio generate ho rahi hai...")
        # 'hi' voice Roman Urdu ke liye natural sound karti hai
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Cinematic Halku Image
        print("⏳ Step 3: AI Image generate ho rahi hai...")
        img_prompt = f"3D_Pixar_style_cinematic_Hulk_emotional_scene_Karachi_city_hyper_realistic_9_16"
        img_url = f"https://image.pollinations.ai/prompt/{img_prompt}?seed={random.randint(1,9999)}"
        
        try:
            img_data = requests.get(img_url, timeout=40).content
            with open("hulk.jpg", "wb") as f:
                f.write(img_data)
        except:
            print("⚠️ Image generator slow tha, background use kar rahe hain.")

        # Step 4: Final Video (1:30 Minute)
        print("⏳ Step 4: Video rendering (90 seconds)...")
        # -t 90 ensures 1:30 min duration
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 90 "
            "-preset fast -pix_fmt yuv420p "
            "-vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        print("✅ SUCCESS: Viral Halku Video Taiyar Hai!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_viral_halku_video()
    
