import win32com.client
import sys


def AuroraSay(text):
    # Создание объекта для синтеза речи
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    # Установка женского голоса
    for voice in speaker.GetVoices():
        if voice.GetDescription().find("Женский") != -1:
            speaker.SetVoice(voice)
            break

    # Скорость речи
    speaker.Rate = 2  # Значение от -10 до 10, где 0 - нормальный темп

    # Синтез и воспроизведение речи
    speaker.Speak(text)
    sys.exit(0)
