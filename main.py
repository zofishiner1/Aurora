import config_loader  # Импортируем модуль для загрузки конфигурации
import speech_recognition  # Импортируем модуль для распознавания речи
import nlp  # Импортируем модуль для обработки естественного языка
import logging  # Импортируем модуль для логирования
import time  # Импортируем модуль для работы со временем
from threading import Thread  # Импортируем класс для создания потоков
from AuroraSay import AuroraSay  # Импортируем функцию для синтеза речи
# Импортируем функцию для получения текущего времени
from currtime import get_current_time
# Импортируем функции для работы с заметками
from mynotes import read_note, write_note
# Импортируем функцию для поиска в Википедии
from wikisearch import get_wikipedia_summary
import sys  # Импортируем модуль для работы с системными функциями


def printeff(text):
    """
    Функция для эффектного вывода текста в консоль.

    Аргументы:
    text (str) -- текст для вывода

    Возвращает:
    None
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


def main():
    """
    Главная функция программы.

    Возвращает:
    None
    """
    logging.basicConfig(filename='data/logs/dialogues.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s')
    # Устанавливаем конфигурацию логирования

    intents = config_loader.load_intents()  # Загружаем возможные ответы
    # Получаем путь к модели распознавания речи из конфигурации
    model_path = config_loader.load_spec_config()
    speech_recognizer = speech_recognition.SpeechRecognizer(model_path)
    # Создаем объект для распознавания речи
    nlp_engine = nlp.NLP(intents)
    # Создаем объект для обработки естественного языка

    with open('squ.txt', 'r', encoding="utf-8") as file:
        print(file.read())
    # Выводим содержимое файла squ.txt

    print("Версия программы V1.1b0. Говорите!")
    # Выводим сообщение о запуске программы

    while True:
        # Получаем текст из генератора
        text = next(speech_recognizer.recognize())
        text = str(text)  # Преобразуем текст в строку

        if 'выход' in text:
            # Если пользователь сказал "выход", то программа завершается
            print(f"Вы: {text}")
            Aurora_resp = nlp_engine.get_response(text)
            texts = Aurora_resp

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()
            # Создаем поток для синтеза речи

            printeff(text)

            speech_synthesis_thread.join()
            break
        elif "время" in text:
            # Если пользователь спросил о времени, то выводим текущее время
            get_current_time()
        elif 'что такое' in text:
            # Если пользователь спросил о чем-то, то ищем информацию в
            # Википедии
            search_query = text.replace('что такое', '').strip()
            summary = get_wikipedia_summary(search_query)

            texts = summary

            logging.info(f'Пользователь: {text}, Бот: {summary}')
            # Логируем запрос и ответ

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()
            # Создаем поток для синтеза речи

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {summary}')

            speech_synthesis_thread.join()
        elif 'зачитай заметку' in text:
            # Если пользователь спросил о заметке, то читаем ее
            note_title = input("Введите название заметки: ")
            note_content = read_note(note_title)
            if note_content:
                response = note_content

                logging.info(f'Пользователь: {text}, Бот: {texts}')

                speech_synthesis_thread = Thread(
                    target=AuroraSay, args=(response,))
                speech_synthesis_thread.start()
                # Создаем поток для синтеза речи

                printeff(f'Вы: {text}')
                printeff(f'Аврора: {response}')

                speech_synthesis_thread.join()

            else:
                response = "Заметка не найдена."
                logging.info(f'Пользователь: {text}, Бот: {response}')

                speech_synthesis_thread = Thread(
                    target=AuroraSay, args=(response,))
                speech_synthesis_thread.start()
                # Создаем поток для синтеза речи

                printeff(f'Вы: {text}')
                printeff(f'Аврора: {response}')

                speech_synthesis_thread.join()

        elif 'запиши заметку' in text:
            # Если пользователь хочет записать заметку, то создаем ее
            note_title = input("Введите название заметки: ")
            note_content = input("Введите содержимое заметки: ")
            write_note(note_title, note_content)
            response = "Заметка успешно записана."
            texts = response

            logging.info(f'Пользователь: {text}, Бот: {texts}')
            # Логируем запрос и ответ

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()
            # Создаем поток для синтеза речи

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {texts}')

            speech_synthesis_thread.join()

        else:
            # Если пользователь сказал что-то другое, то отвечаем
            # соответствующим образом
            Aurora_resp = nlp_engine.get_response(text.lower())
            texts = Aurora_resp
            logging.info(f'Пользователь: {text}, Бот: {Aurora_resp}')
            # Логируем запрос и ответ

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()
            # Создаем поток для синтеза речи

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {Aurora_resp}')

            speech_synthesis_thread.join()


if __name__ == '__main__':
    main()
    # Вызываем главную функцию программы
