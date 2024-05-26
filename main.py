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
import json
import psutil  # Импортируем модуль для получения информации об оперативной памяти
from logz import create_session_file
from logz import update_session_file
import datetime

create_session_file()

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
            start_time = time.time()
            Aurora_resp = nlp_engine.get_response(text)
            response_time = start_time - end_time
            memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # Конвертируем в МБ
            texts = Aurora_resp
            end_time = str(datetime.datetime.now())
            session_data = {
                "end_time": end_time,
                "user_utterance": text,
                "assistant_response": texts,
                "response_time": response_time,
                "memory_usage": memory_usage
            }
            
            update_session_file(session_data, end_time)

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
            start_time = time.time()
            summary = get_wikipedia_summary(search_query)
            end_time = time.time()
            response_time = end_time - start_time
            memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # Конвертируем в МБ
            texts = summary
            session_data = {
                "user_utterance": text,
                "assistant_response": texts,
                "response_time": response_time,
                "memory_usage": memory_usage
            }

        
            update_session_file(data=session_data)

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
                start_time = time.time()
                end_time = time.time()
                response_time = end_time - start_time
                memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # Конвертируем в МБ
                session_data = {
                    "user_utterance": text,
                    "assistant_response": response,
                    "response_time": response_time,
                    "memory_usage": memory_usage
                }

            
                update_session_file(data=session_data)

                speech_synthesis_thread = Thread(
                    target=AuroraSay, args=(response,))
                speech_synthesis_thread.start()
                # Создаем поток для синтеза речи

                printeff(f'Вы: {text}')
                printeff(f'Аврора: {response}')

                speech_synthesis_thread.join()

            else:
                response = "Заметка не найдена."
                start_time = time.time()
                end_time = time.time()
                response_time = end_time - start_time
                memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # Конвертируем в МБ
                session_data = {
                    "user_utterance": text,
                    "assistant_response": response,
                    "response_time": response_time,
                    "memory_usage": memory_usage
                }

            
                update_session_file(data=session_data)

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
            start_time = time.time()
            end_time = time.time()
            response_time = end_time - start_time
            memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # Конвертируем в МБ
            texts = response
            session_data = {
                "user_utterance": text,
                "assistant_response": texts,
                "response_time": response_time,
                "memory_usage": memory_usage
            }

            update_session_file(data=ssion_data)

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()
            # Создаем поток для синтеза речи

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {texts}')

            speech_synthesis_thread.join()

        else:
            # Если пользователь сказал что-то другое, то отвечаем
            # соответствующим образом
            start_time = time.time()
            Aurora_resp = nlp_engine.get_response(text.lower())
            end_time = time.time()
            response_time = end_time - start_time
            memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)  # Конвертируем в МБ
            texts = Aurora_resp
            session_data = {
                "user_utterance": text,
                "assistant_response": texts,
                "response_time": response_time,
                "memory_usage": memory_usage
            }
            

            update_session_file(data=session_data)

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()
            # Создаем поток для синтеза речи

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {Aurora_resp}')


            speech_synthesis_thread.join()

if __name__ == '__main__':
    main()
    # Вызываем главную функцию программы