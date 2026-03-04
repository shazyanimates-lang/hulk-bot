import requests
from gtts import gTTS

def start_bot():
    try:
        # No Gemini, No API Key - Purely Free AI
        prompt = "Hulk eating biryani in Karachi"
        # Text AI
        story = requests.get(f"https://text.pollinations.ai/{prompt}").text
        print(f"Story: {story}")
        # Audio
        gTTS(text=story, lang='en').save("hulk.mp3")
        # Image
        img_data = requests.get(f"https://image.pollinations.ai/prompt/{prompt}").content
        with open("hulk.jpg", "wb") as f:
            f.write(img_data)
        print("Done! No API needed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_bot()
  
