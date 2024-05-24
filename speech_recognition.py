import os
import pyaudio
import json
from vosk import Model, KaldiRecognizer
import config_loader

class SpeechRecognizer:
    def __init__(self, model_path):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=16000,
                                input=True,
                                frames_per_buffer=8000)
        self.stream.start_stream()
        model = Model(model_path)  # Создаем объект модели
        self.rec = KaldiRecognizer(model, 16000)

    def recognize(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if (self.rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(self.rec.Result())
                if answer['text']:
                    yield answer['text']