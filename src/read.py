from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os
def gg_recognise(filename,text):
    if filename == None:filename = "./speech.mp3"
    if os.path.exists(filename):os.remove(filename)
    output = gTTS(text,lang="vi", slow=False)
    output.save(filename)
def play(filename, save):
    playsound(filename)
    if not save:
        os.remove(filename)