import requests
from gtts import gTTS

def start_bot():
    try:
        print("AI is writing the story...")
        # Pollinations AI se story likhwana (Free & No API Key)
        prompt = "Write a 1-line funny story about Hulk in Karachi."
        ai_url = f"https://text.pollinations.ai/{prompt.replace(' ', '%20')}"
        
        response = requests.get(ai_url)
        story_text = response.text.strip()
        print(f"AI Story: {story_text}")

        # Audio banana
        gTTS(text=story_text, lang='en').save("hulk_story.mp3")
        print("Audio saved!")

        # Image banana
        img_prompt = f"Hulk in Karachi city, {story_text}, cinematic"
        img_url = f"https://image.pollinations.ai/prompt/{img_prompt.replace(' ', '_')}"
        with open("hulk_image.jpg", "wb") as f:
            f.write(requests.get(img_url).content)
        print("Image saved!")
        
        print("Bot Run Successfully via Pollinations AI!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_bot()
