import wikipedia
import mwxml
import time
import gc
import os
import mwparserfromhell
import re
import requests


def get_wikipedia_summary(search_query):
    if check_internet_connection():
        return search_out(search_query)
    else:
        return search_local(search_query)


def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False


global_current_dir = os.getcwd()

wikipedia.set_lang('ru')

memory_threshold = 100 * 1024 * 1024  # 100 МБ


def search_out(query):
    """
    Функция, которая выполняет поиск статьи по запросу и возвращает ее краткое содержание.

    Аргументы:
    query (str) -- поисковый запрос

    Возвращает:
    str -- краткое содержание статьи
    """
    try:
        # Проверяем наличие текстового файла с названием запроса
        try:
            with open(f"data/wikis/{query}.txt", "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            # Если файл не найден, выполняем поиск статьи по запросу
            page = wikipedia.page(query)

            # Сохраняем текст статьи в текстовый файл
            with open(f"data/wikis/{query}.txt", "w", encoding="utf-8") as file:
                file.write(page.content)

            # Возвращаем краткое содержание статьи
            return page.summary

    except wikipedia.exceptions.PageError:
        return "Статья не найдена."

    except wikipedia.exceptions.DisambiguationError as e:
        # Если найдено несколько страниц, возвращаем первую
        return wikipedia.summary(e.options[0])


def search_local(target_title):
    """
    Функция, которая выполняет поиск статьи по запросу и возвращает ее содержание.

    Аргументы:
    target_title (str) -- поисковый запрос

    Возвращает:
    str -- содержание статьи
    """

    print(f"Запрос: {target_title}")
    os.chdir(global_current_dir)
    index_filename = os.path.join(
        global_current_dir,
        "data\\LocWIKI\\ruwiki-latest-pages-articles-multistream-index.txt")
    dump_filename = os.path.join(
        global_current_dir,
        "data\\LocWIKI\\ruwiki-latest-pages-articles-multistream.xml")

    target_title_lower = target_title.lower()

    # Проверяем наличие текстового файла с названием запроса
    file_path = f'data/wikis/{target_title}.txt'
    if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(f"Статья найдена в файле: {file_path}")
            return file.read()

    with open(index_filename, "r", encoding="utf-8") as index_file:
        for line in index_file:
            parts = line.strip().split(":")
            if parts[-1].strip().lower() == target_title_lower:
                page_id = parts[-2]
                print(f"Page id: {page_id}")
                break
        else:
            print(f"Page id не найдено для статьи {target_title}")
            return None

    with open(dump_filename, "r", encoding="utf-8") as dump_file:
        dump = mwxml.Dump.from_file(dump_file)

        found_in_file = False
        page_count = 0
        for page in dump:
            page_count += 1
            if str(page.id) == page_id:
                found_in_file = True
                print(f"Статья найдена в файле: {dump_filename}")
                for revision in page:
                    summary = revision

                    if summary is not None:
                        text_from_revision = summary.text  # Получение текста из объекта Revision

                        # Используйте mwparserfromhell для обработки текста
                        wikitext = mwparserfromhell.parse(text_from_revision)
                        cleaned_text = " ".join([x.value.strip() for x in wikitext.nodes if isinstance(
                            x, mwparserfromhell.nodes.text.Text) and not x.value.isdigit()])

                        # Сохраняем текст статьи в текстовый файл
                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(cleaned_text)

                        return cleaned_text
                break
            else:
                page_id_int = int(page_id)
                # Преобразуем page_id из строки в целое число и сохраняем в
                # переменную page_id_int

                page_id_int_str = str(page_id_int)
                # Преобразуем page_id_int обратно в строку и сохраняем в
                # переменную page_id_int_str

                page_id_len = len(page_id_int_str)
                # Вычисляем длину строки page_id_int_str и сохраняем в
                # переменную page_id_len

                page_id_int_str_part = page_id_int_str[:page_count]
                # Получаем часть строки page_id_int_str длиной page_count символов с начала строки
                # и сохраняем в переменную page_id_int_str_part

                page_id_int_part = int(page_id_int_str_part)
                # Преобразуем page_id_int_str_part обратно в целое число и
                # сохраняем в переменную page_id_int_part

                page_id_part = int(str(page.id))
                # Преобразуем page.id из объекта в строку, а затем в целое
                # число и сохраняем в переменную page_id_part

                similarity = (page_id_part * 100) // page_id_int_part
                # Вычисляем процент сходства между page_id_part и page_id_int_part
                # Умножаем page_id_part на 100, чтобы получить процент, и делим на page_id_int_part
                # Используем целочисленное деление // для получения целого
                # числа в процентах

                print(
                    f'{similarity}%. Page id текущей статьи: {page.id}',
                    end="\r")
                # Выводим процент сходства и page.id текущей статьи в одной строке
                # Используем end="\r" для перезаписи предыдущей строки

                # Очистка мусора из оперативной памяти
                time.sleep(0.009)
                wikicode = None
                text = None
                page_id_int = None
                page_id_int_str = None
                page_id_len = None
                page_id_int_str_part = None
                page_id_int_part = None
                page_id_part = None
                del wikicode, text, page_id_int, page_id_int_str, page_id_len, page_id_int_str_part, page_id_int_part, page_id_part
                gc.collect()

        if not found_in_file:
            print(f"Статья не была найдена в файле: {filename}.")

        return None
