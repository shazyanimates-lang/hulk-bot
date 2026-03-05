import requests
import os
import time
from gtts import gTTS

def generate_video():
    try:
        # Step 1: Kahani generate karna
        print("⏳ Step 1: Generating story...")
        story_res = requests.get("https://text.pollinations.ai/Hulk_funny_Karachi_joke_1_line_in_Hindi_Urdu")
        story = story_res.text if story_res.status_code == 200 else "Hulk Karachi mein biryani dhoond raha hai!"
        print(f"Story: {story}")

        # Step 2: Awaz (Audio) banana
        print("⏳ Step 2: Saving Audio...")
        tts = gTTS(text=story, lang='hi') # Urdu/Hindi ke liye 'hi' best hai
        tts.save("voice.mp3")

        # Step 3: AI Image download karna
        print("⏳ Step 3: Getting AI Image...")
        img_url = f"https://image.pollinations.ai/prompt/Hulk_eating_biryani_in_Karachi_9_16_cinematic_{int(time.time())}"
        img_data = requests.get(img_url).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        # Step 4: Video banana (The Fix is Here)
        print("⏳ Step 4: Creating Video (FFmpeg)...")
        # '-y' flag overwrite ki auto-permission deta hai taaki script na ruke
        cmd = (
            "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 10 "
            "-pix_fmt yuv420p -vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' "
            "-c:a aac -shortest short_video.mp4"
        )
        os.system(cmd)
        
        print("✅ SUCCESS: short_video.mp4 tayyar hai!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_video()
