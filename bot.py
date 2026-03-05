import requests
import os
import time
import random
from gtts import gTTS

def generate_trending_urdu_video():
    try:
        print("⏳ Step 1: AI Trending Roman Urdu script likh raha hai...")
        
        # Trending Topics for Halku
        topics = [
            "Hulk ki tooti purani car dekh kar ameer dost ne mazak udaya, phir Hulk ne Lamborghini kharid kar badla liya",
            "Hulk ne Karachi ki sadak par ek gareeb bache ki madad ki aur usay school bheja",
            "Hulk aur uske doston ki laraee hui aur Hulk ne unhe apni taqat dikhaee",
            "Hulk ne boxing match jeeta aur 20 crore inaam haasil kiya"
        ]
        selected_topic = random.choice(topics)
        
        # AI ko Roman Urdu (Hindustani) mein script likhne ka order
        query = (
            f"Write a very long 1:30 minute dramatic YouTube Short script in Roman Urdu/Hindi "
            f"about this: {selected_topic}. Use words like 'Mota', 'Bhai', 'Paisa', 'Badla'. "
            f"Make it a dialogue between Hulk and a Manager or Friend."
        )
        
        try:
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=30)
            # Agar AI Roman Urdu na likhe toh hum fallback script use karenge
            story = res.text if res.status_code == 200 else "Hulk ne kaha: Aaj se main Karachi ka king hoon!"
        except:
            story = "Manager ne bola: Tu bhikhari hai! Hulk ne bola: Dekhna ek din main Lamborghini le kar aaunga!"

        print(f"🎬 Script Preview: {story[:100]}...")

        # Step 2: Audio (Urdu/Hindi Accent)
        print("⏳ Step 2: Voice generate ho rahi hai...")
        # 'hi' lang Roman Urdu ke liye best accent deti hai
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: Cinematic Image (Halku 3D Style)
        print("⏳ Step 3: AI Image generate ho rahi hai...")
        img_prompt = f"3D_Disney_Pixar_style_Hulk_cinematic_Karachi_{selected_topic.replace(' ', '_')}_9_16"
        img_url = f"https://image.pollinations.ai/prompt/{img_prompt}?seed={random.randint(1,9999)}"
        
        img_data = requests.get(img_url, timeout=40).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        # Step 4: Video Rendering (90 Seconds)
        print("⏳ Step 4: 1:30 minute ki video ban rahi hai...")
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 90 "
            "-preset fast -pix_fmt yuv420p "
            "-vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        print("✅ MUBARAK HO! Video tayyar hai.")

    except Exception as e:
        print(f"❌ Error aaya hai: {e}")

if __name__ == "__main__":
    generate_trending_urdu_video()
