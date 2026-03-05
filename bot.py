import os
from gtts import gTTS
from PIL import Image, ImageDraw

def generate_video():
    try:
        # Step 1: Kahani (Simple Text)
        story = "Hulk is looking for the best Biryani in Karachi!"
        print(f"⏳ Story: {story}")

        # Step 2: Audio (gTTS)
        print("⏳ Saving Audio...")
        tts = gTTS(text=story, lang='en')
        tts.save("voice.mp3")

        # Step 3: Fast Image Generation (No External API)
        print("⏳ Generating Fast Background...")
        img = Image.new('RGB', (1080, 1920), color=(0, 128, 0)) # Hulk Green Color
        d = ImageDraw.Draw(img)
        # Ek simple box ya text draw kar rahe hain taaki image khali na ho
        d.rectangle([100, 100, 980, 1820], outline=(255, 255, 255), width=10)
        img.save("hulk.jpg")

        # Step 4: Video (FFmpeg with Force Exit)
        print("⏳ Creating Video...")
        # '-y' aur '-t 10' ensure karega ke script na ruke
        cmd = "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 10 -pix_fmt yuv420p -c:a aac -shortest short_video.mp4"
        os.system(cmd)
        
        print("✅ SUCCESS: short_video.mp4 created!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_video()
