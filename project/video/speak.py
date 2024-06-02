# Original from https://www.geeksforgeeks.org/convert-text-speech-python/
from gtts import gTTS
import os


# Open the predetermined file
with open('text_video.txt') as f:
    mytext = f.read()

# Setting language, creating the object
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file
myobj.save("audio.mp3")

# Playing the converted file
os.system("start audio.mp3")
