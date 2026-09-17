import os
import google.generativeai as genai
from elevenlabs import ElevenLabs
from moviepy.editor import ImageClip, AudioFileClip

# 1. Environment variables se API keys load karna
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
ELEVEN_API_KEY = os.environ.get("ELEVEN_API_KEY")

# 2. Gemini API Configure karna
genai.configure(api_key=GEMINI_API_KEY)

def generate_script():
    print("Step 1: Gemini script likh raha hai...")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Write a short, funny, 2-sentence dialogue for the Hulk in a rage, suitable for a YouTube Short.")
    script_text = response.text
    print(f"Script: {script_text}")
    return script_text

def generate_voice(text):
    print("Step 2: ElevenLabs voice bana raha hai...")
    client = ElevenLabs(api_key=ELEVEN_API_KEY)
    
    # Audio generate karna (Hulk jaisi heavy voice ke liye standard voice ID ya default use kar sakte hain)
    audio = client.generate(
        text=text,
        voice="JBFqnCBsd6RMkjVDRZzb", # Default Adam or any voice ID
        model="eleven_multilingual_v2"
    )
    
    audio_path = "hulk_voice.mp3"
    with open(audio_path, "wb") as f:
        # Check if audio is an iterator or bytes
        if isinstance(audio, bytes):
            f.write(audio)
        else:
            for chunk in audio:
                f.write(chunk)
                
    print("Voice ready!")
    return audio_path

def create_video(audio_path):
    print("Step 3: Local Hulk image use kar rahe hain...")
    
    # Ensure local image exists in your repository
    image_path = "hulk.jpg"
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"'{image_path}' file nahi mili! Apni GitHub repo me hulk.jpg upload karein.")
        
    print("Hulk image loaded successfully!")

    print("Step 4: Rendering Video...")
    # Audio load karein taaki duration pata chale
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    # Image clip banayein audio ki duration ke mutabiq
    image_clip = ImageClip(image_path).set_duration(duration)
    
    # Audio ko video clip ke sath set karein
    video_clip = image_clip.set_audio(audio_clip)

    output_video = "hulk_output.mp4"
    # Video write karein (vertical format ke liye size set kar sakte hain jaise 1080x1920)
    video_clip.resize(height=1920).write_videofile(
        output_video, 
        fps=24, 
        codec='libx264', 
        audio_codec='aac'
    )
    
    print("Video rendering complete!")
    return output_video

if __name__ == "__main__":
    script = generate_script()
    audio_file = generate_voice(script)
    create_video(audio_file)
