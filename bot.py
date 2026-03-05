import requests
import subprocess
import os
import time
from gtts import gTTS

def generate_video():
    try:
        print("⏳ Step 1: Story & Audio...")
        story = requests.get("https://text.pollinations.ai/Hulk_funny_Karachi_joke_1_line").text
        gTTS(text=story, lang='en').save("voice.mp3")

        print("⏳ Step 2: AI Image...")
        img_url = f"https://image.pollinations.ai/prompt/Hulk_in_Karachi_vertical_9_16_{int(time.time())}"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)

        print("⏳ Step 3: Creating MP4...")
        cmd = "ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 10 -pix_fmt yuv420p -vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' -c:a aac -shortest short_video.mp4"
        os.system(cmd)

        # --- NEW: DIRECT DOWNLOAD LINK GENERATOR ---
        print("🚀 Step 4: Generating Direct Download Link...")
        with open("short_video.mp4", "rb") as f:
            # Ye line video ko cloud pe upload karke link degi
            response = requests.put("https://transfer.sh/short_video.mp4", data=f)
            
        if response.status_code == 200:
            print("\n✅ VIDEO TAYYAR HAI!")
            print(f"🔗 Download Link: {response.text}") # Is link pe click karein
        else:
            print("❌ Upload failed, check Artifacts in GitHub.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_video()
