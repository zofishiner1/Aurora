import pyttsx3
import sys  # Импортируем модуль для работы с системными функциями


def AuroraSayF(text):
    """
    Функция для синтеза и воспроизведения речи с помощью Microsoft Speech API (SAPI).

    Аргументы:
    text (str) -- текст, который необходимо преобразовать в речь

    Возвращает:
    None
    """
    # Инициализация синтеза речи
    engine = pyttsx3.init()

    # Установка настроек голоса
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Генерация речи
    engine.say(text)
    engine.runAndWait()

    sys.exit(0)
    # Завершаем работу программы с кодом возврата 0 (успешное завершение)
