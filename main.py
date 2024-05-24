import config_loader
import speech_recognition
import nlp
import logging
import time
from threading import Thread
from AuroraSay import AuroraSay
from currtime import get_current_time
from mynotes import read_note, write_note
from wikisearch import get_wikipedia_summary
import sys

def printeff(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def main():
    logging.basicConfig(filename='data/logs/dialogues.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s')

    intents = config_loader.load_intents() # Загружаем возможные ответы

    model_path = config_loader.load_spec_config()  # Получаем путь к модели распознавания речи из конфигурации
    speech_recognizer = speech_recognition.SpeechRecognizer(model_path)
    nlp_engine = nlp.NLP(intents)

    with open('squ.txt', 'r', encoding="utf-8") as file:
        print(file.read())

    print("Версия программы V1.1b0. Говорите!")
    while True:
        text = next(speech_recognizer.recognize())  # Получаем текст из генератора
        text = str(text)  # Преобразуем текст в строку
        if 'выход' in text:
            print(f"Вы: {text}")
            Aurora_resp = nlp_engine.get_response(text)
            texts = Aurora_resp

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()

            printeff(text)

            speech_synthesis_thread.join()
            break
        elif "время" in text:
            get_current_time()
        elif 'что такое' in text:
            search_query = text.replace('что такое', '').strip()
            summary = get_wikipedia_summary(search_query)

            texts = summary

            logging.info(f'Пользователь: {text}, Бот: {summary}')

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {summary}')

            speech_synthesis_thread.join()

        elif 'зачитай заметку' in text:
            note_title = input("Введите название заметки: ")
            note_content = read_note(note_title)
            if note_content:
                response = note_content

                logging.info(f'Пользователь: {text}, Бот: {texts}')

                speech_synthesis_thread = Thread(target=AuroraSay, args=(response,))
                speech_synthesis_thread.start()

                printeff(f'Вы: {text}')
                printeff(f'Аврора: {response}')

                speech_synthesis_thread.join()

            else:
                response = "Заметка не найдена."
                logging.info(f'Пользователь: {text}, Бот: {response}')

                speech_synthesis_thread = Thread(target=AuroraSay, args=(response,))
                speech_synthesis_thread.start()

                printeff(f'Вы: {text}')
                printeff(f'Аврора: {response}')

                speech_synthesis_thread.join()

        elif 'запиши заметку' in text:
            note_title = input("Введите название заметки: ")
            note_content = input("Введите содержимое заметки: ")
            write_note(note_title, note_content)
            response = "Заметка успешно записана."
            texts = response

            logging.info(f'Пользователь: {text}, Бот: {texts}')

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {texts}')

            speech_synthesis_thread.join()

        else:
            Aurora_resp = nlp_engine.get_response(text.lower())  # Преобразуем текст в нижний регистр
            texts = Aurora_resp
            logging.info(f'Пользователь: {text}, Бот: {Aurora_resp}')

            speech_synthesis_thread = Thread(target=AuroraSay, args=(texts,))
            speech_synthesis_thread.start()

            printeff(f'Вы: {text}')
            printeff(f'Аврора: {Aurora_resp}')

            speech_synthesis_thread.join()

if __name__ == '__main__':
    main()