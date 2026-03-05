import requests
import os
import random
from gtts import gTTS

def generate_hulk_action_video():
    try:
        # Step 1: AI Trending Script (Dialogue Style)
        print("⏳ Step 1: AI trendy dialogues soch raha hai...")
        trends = [
            "Halku buys a luxury car after being insulted",
            "Halku helps a poor kid and becomes a hero",
            "Halku enters a wrestling match to win 20 crore"
        ]
        selected = random.choice(trends)
        
        # AI ko specific Roman Urdu order dena
        query = (
            f"Write a 90 seconds dramatic dialogue script in Roman Urdu about: {selected}. "
            f"Start with an insult like 'Ae mote kahan ja raha hai' and end with success. "
            f"Make it high energy for YouTube Shorts."
        )
        
        try:
            res = requests.get(f"https://text.pollinations.ai/{query.replace(' ', '_')}", timeout=30)
            story = res.text if res.status_code == 200 else "Ae mote! Dekh meri Lamborghini! Ab bol kiska waqt hai?"
        except:
            story = "Manager: Ae mote nikal yahan se! Halku: Yaad rakhna, waqt sabka badalta hai. Aaj mere paas cycle hai, kal Lamborghini hogi!"

        # Step 2: Audio (Roman Urdu Accent)
        print("⏳ Step 2: Voice generate ho rahi hai...")
        tts = gTTS(text=story, lang='hi') 
        tts.save("voice.mp3")

        # Step 3: High-Quality Hulk Image (No More Cats)
        print("⏳ Step 3: Proper Hulk Image download ho rahi hai...")
        # Direct stable link taaki billi (cat) ya statue na aye
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        r = requests.get(img_url)
        with open("hulk.jpg", "wb") as f:
            f.write(r.content)

        # Step 4: Final Video with Movement (1:30 min)
        print("⏳ Step 4: Video render ho rahi hai (Zoom Effect)...")
        # Zoompan filter se video move karegi aur static nahi lagegi
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 "
            "-vf \"zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920\" "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        print("✅ SUCCESS: Video ban gayi hai!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_hulk_action_video()
    
