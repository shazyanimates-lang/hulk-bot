import requests, os
from gtts import gTTS

def start_bot():
    try:
        # 1. AI Story
        story = requests.get("https://text.pollinations.ai/Hulk_in_Karachi_funny_Short_Story_1_line").text
        print(f"Story: {story}")

        # 2. Audio (Voiceover)
        gTTS(text=story, lang='en').save("voice.mp3")

        # 3. Image (Vertical for Shorts)
        img_url = f"https://image.pollinations.ai/prompt/Hulk_in_Karachi_vertical_aspect_ratio_9_16_{story[:20]}"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)

        # 4. FFmpeg se Shorts Video (9:16) banana
        # Ye command photo ko Shorts ke size mein convert karke audio jor degi
        os.system("ffmpeg -loop 1 -i hulk.jpg -i voice.mp3 -c:v libx264 -t 15 -pix_fmt yuv420p -vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920' -c:a aac -shortest short_video.mp4")
        
        print("Shorts Video Created: short_video.mp4")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_bot()
