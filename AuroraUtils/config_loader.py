import json  # Импортируем модуль для работы с JSON-данными
import os  # Импортируем модуль для работы с операционной системой


def load_spec_config():
    """
    Функция для загрузки пути к модели распознавания речи из конфигурационного файла.

    Возвращает:
    str -- путь к модели распознавания речи
    """
    config_path = 'data/configs/model.rec'  # Путь к конфигурационному файлу
    with open(config_path, 'r', encoding='utf-8') as file:
        # Открываем файл для чтения в кодировке utf-8
        model = 'data/models/speech_rec/' + file.readline().strip()
        # Читаем первую строку файла, удаляем пробелы и добавляем префикс
    return model  # Возвращаем путь к модели


def load_intents():
    """
    Функция для загрузки интентов из JSON-файла.

    Возвращает:
    dict -- словарь с интентами и соответствующими ответами
    """
    intents_path = 'data/configs/intents.json'  # Путь к файлу с интентами
    with open(intents_path, 'r', encoding='utf-8') as file:
        # Открываем файл для чтения в кодировке utf-8
        responses = json.load(file)
        # Загружаем данные из файла в словарь с помощью json.load()
    return responses  # Возвращаем словарь с интентами и ответами
