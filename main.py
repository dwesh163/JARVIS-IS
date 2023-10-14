#from scripts.AI_script import AI

from vosk import Model, KaldiRecognizer
from dotenv import load_dotenv
import os
import pyaudio

load_dotenv()
    
#model
model = Model(os.getenv('VOSK_PATH'))
recognizer = KaldiRecognizer(model, 16000)

#mic
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
print("voix opérationnel")
while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        global text
        text = recognizer.Result()
        text = text[14:-3]
        if text != "":
            print(text)    
        
