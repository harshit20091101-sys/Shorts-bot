import os, asyncio, textwrap
import google.generativeai as genai
import edge_tts
from moviepy.editor import *

genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
story = model.generate_content("Ek 25 sec ki horror hindi story likh, direct story start kar").text

async def make_voice():
    await edge_tts.Communicate(story, "hi-IN-SwaraNeural").save("voice.mp3")
asyncio.run(make_voice())

audio = AudioFileClip("voice.mp3")
txt = TextClip(textwrap.fill(story, width=22), fontsize=60, color='white', size=(720,1280), method='caption', bg_color='black').set_duration(audio.duration).set_audio(audio)
txt.write_videofile("short.mp4", fps=24)
