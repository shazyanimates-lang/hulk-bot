import os
import requests

def run_90s_hulk_bot():
    try:
        # 1. FIXED SCRIPT (Gemini bypass to avoid 429 error)
        print("🎬 Step 1: Script process ho rahi hai...")
        script_text = (
            "Ae bus walay! Roko ye khatara! Hulk ko Karachi ki sarko par chalna hai! "
            "Bus driver bolta hai: Abe ja na mote, rasta chorr! "
            "Hulk ko gussa aa gaya! Hulk bola: Kya bola? Mote? Ab dekh, ye poori bus meri hai. "
            "Ye lo paisay aur niklo yahan se! Ab Hulk Karachi ka naya don hai aur ye bus ab hawa mein uregi! "
            "Sab log rasta chorr do, warna Hulk ghussay mein sab kuch tor dega! "
            "Showroom walay ne gari nahi di, toh Hulk ne poori transport company kharid li. "
            "Ab bolo, kiska waqt hai? Karachi walay ho jao tayyar, Hulk aa gaya hai!"
        )

        # 2. ELEVENLABS DIRECT API (Library bypass to avoid AttributeError)
        print("🎙️ Step 2: ElevenLabs voice generate kar raha hai...")
        eleven_key = os.getenv("ELEVEN_API_KEY")
        voice_id = "pNInz6obpgDQGcFmaJgB" # Adam's Voice ID
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": eleven_key
        }
        
        data = {
            "text": script_text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
        }
        
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            with open("voice.mp3", "wb") as f:
                f.write(response.content)
            print("✅ Voice ready!")
        else:
            print(f"❌ ElevenLabs Error: {response.text}")
            return

        # 3. IMAGE DOWNLOAD
        print("🖼️ Step 3: Image ready ho rahi hai...")
        img_url = "https://w0.peakpx.com/wallpaper/559/393/HD-wallpaper-hulk-3d-hulk-superhero-green-man-marvel-avengers.jpg"
        with open("hulk.jpg", "wb") as f:
            f.write(requests.get(img_url).content)

        # 4. FFMPEG RENDER (Pakka 90 Seconds)
        print("🎥 Step 4: Video render ho raha hai (90s)...")
        os.system("ffmpeg -y -loop 1 -i hulk.jpg -i voice.mp3 -t 90 -vf \"scale=1080:1920,setsar=1\" -c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest short_video.mp4")
        print("✅ DONE: short_video.mp4 tayyar hai!")

    except Exception as e:
        print(f"❌ Critical Error: {e}")

if __name__ == "__main__":
    run_90s_hulk_bot()
    
