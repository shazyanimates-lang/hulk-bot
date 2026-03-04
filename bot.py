import requests, os
from gtts import gTTS

def start_bot():
    try:
        # 1. AI Story
        story = requests.get("https://text.pollinations.ai/Hulk_in_Karachi_funny_1_line").text
        print(f"Story: {story}")

        # 2. Audio & Image
        gTTS(text=story, lang='en').save("hulk.mp3")
        img_data = requests.get(f"https://image.pollinations.ai/prompt/Hulk_in_Karachi_{story[:20]}").content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)

        # 3. Create Video (Command Line)
        # Ye command photo aur audio ko jorr kar video banaye gi
        os.system("ffmpeg -loop 1 -i hulk.jpg -i hulk.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest video.mp4")
        print("Video Created: video.mp4")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_bot()
