from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os
def read(filename,text,save):
    if filename == None:filename = "./speech.mp3"
    if os.path.exists(filename):os.remove(filename)
    output = gTTS(text,lang="vi", slow=False)
    output.save(filename)
    playsound(filename)
    if not save:
        os.remove(filename)

