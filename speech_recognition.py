import os  # Импортируем модуль для работы с операционной системой
import pyaudio  # Импортируем модуль для работы с аудио
import json  # Импортируем модуль для работы с JSON-данными
# Импортируем классы для распознавания речи
from vosk import Model, KaldiRecognizer
import config_loader  # Импортируем модуль для загрузки конфигурации


class SpeechRecognizer:
    """
    Класс для распознавания речи в реальном времени с использованием модели Vosk.
    """

    def __init__(self, model_path):
        """
        Инициализация класса SpeechRecognizer.

        Аргументы:
        model_path (str) -- путь к модели распознавания речи
        """
        self.p = pyaudio.PyAudio()  # Создаем объект для работы с аудио
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=16000,
                                  input=True,
                                  frames_per_buffer=8000)
        # Открываем аудио поток с настройками: 16-битный формат, 1 канал,
        # частота дискретизации 16 кГц
        self.stream.start_stream()  # Запускаем аудио поток
        model = Model(model_path)  # Создаем объект модели с указанным путем
        # Создаем объект распознавателя речи
        self.rec = KaldiRecognizer(model, 16000)

    def recognize(self):
        """
        Функция для распознавания речи в реальном времени.

        Возвращает:
        generator -- генератор, который возвращает распознанный текст
        """
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            # Читаем аудио данные из потока порциями по 4000 байт
            if (self.rec.AcceptWaveform(data)) and (len(data) > 0):
                # Если распознаватель принял аудио данные и они не пустые
                answer = json.loads(self.rec.Result())
                # Получаем результат распознавания в формате JSON
                if answer['text']:
                    yield answer['text']
                    # Возвращаем распознанный текст с помощью генератора
