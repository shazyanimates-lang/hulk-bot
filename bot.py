import os
from gtts import gTTS
from PIL import Image, ImageDraw

def make_fail_safe_video():
    try:
        # 1. Voice Script
        text = "Ae mote! Dekh meri Lamborghini! Ab bol kiska waqt hai?"
        print("⏳ Step 1: Voice generate ho rahi hai...")
        tts = gTTS(text=text, lang='hi')
        tts.save("voice.mp3")

        # 2. Create Internal Image (No Download)
        print("⏳ Step 2: Creating Hulk Green background...")
        # 1080x1920 (Vertical for Shorts)
        img = Image.new('RGB', (1080, 1920), color=(0, 128, 0)) 
        d = ImageDraw.Draw(img)
        # Background par likh dete hain taaki khali na lage
        img.save("hulk.jpg")
        print("✅ Image Created internally!")

        # 3. Fast Rendering (No Animation)
        print("⏳ Step 3: Video render ho rahi hai...")
        # Sirf 15 seconds ki video banate hain pehle taaki pakka banay
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 15 "
            "-c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        if os.path.exists("short_video.mp4"):
            print("✅ SUCCESS: short_video.mp4 tayyar hai!")
        else:
            print("❌ Error: Video file abhi bhi nahi mili.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    make_fail_safe_video()
    
