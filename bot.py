import requests
import subprocess
import os
import time
from gtts import gTTS

def generate_video():
    try:
        print("⏳ Step 1: Story generate ho rahi hai...")
        # Pollinations AI se story fetch karna
        story_res = requests.get("https://text.pollinations.ai/A_short_funny_joke_about_Hulk_getting_stuck_in_Karachi_traffic_1_sentence")
        story_text = story_res.text.strip()
        print(f"📖 Story: {story_text}")

        print("⏳ Step 2: Audio (Voiceover) ban raha hai...")
        tts = gTTS(text=story_text, lang='en')
        tts.save("voice.mp3")

        print("⏳ Step 3: AI Image generate ho rahi hai...")
        # Mobile 9:16 aspect ratio ke liye prompt
        img_prompt = f"Hulk_in_Karachi_streets_cinematic_vertical_9_16_{int(time.time())}"
        img_url = f"https://image.pollinations.ai/prompt/{img_prompt}"
        
        img_data = requests.get(img_url).content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        print("⏳ Step 4: FFmpeg se MP4 ban raha hai...")
        # Ye command mobile (Termux) ke liye optimized hai
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-i", "hulk.jpg", "-i", "voice.mp3",
            "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", 
            "-b:a", "128k", "-pix_fmt", "yuv420p", "-shortest",
            "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
            "short_video.mp4"
        ]
        
        # Subprocess use karna mobile par zyada stable hai
        subprocess.run(cmd, check=True)
        
        print("\n✅ MUBARAK HO! 'short_video.mp4' tayyar hai.")
        print("📁 Aap isse apne mobile gallery mein dekh sakte hain.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_video()
