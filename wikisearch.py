import os
import wikipedia
import mwxml
import mwparserfromhell
import time
import gc
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

def search_out(page_title):
    os.chdir('data/wikis')
    file_path = f'{page_title}.txt'

    if not os.path.isfile(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            print(f'Файл "{file_path}" создан')
    try:
        if os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as file:
                summary = file.read()
                print(f'Используется содержимое файла "{file_path}"')
                return summary

        page = wikipedia.page(page_title)  # Получаем объект страницы
        summary = page.summary  # Извлекаем краткое содержание

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(summary)
            print(f'Статья сохранена в файл "{file_path}"')

        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        print("Уточните ваш запрос. ", e)
        return None

    except wikipedia.exceptions.PageError as e:
        print("Ничего не найдено на Википедии. ", e)
        return None

    finally:
        os.chdir(global_current_dir)

def search_local(target_title):
    os.chdir(global_current_dir)
    filename = os.path.join(
        global_current_dir,
        "data\\LocWIKI\\ruwiki-latest-pages-articles-multistream.xml")

    def parse_revision(revision):
        wikicode = mwparserfromhell.parse(revision.text)
        text = wikicode.strip_code()
        summary = text.split('\n')[0]
        return summary

    with open(filename, "r", encoding="utf-8") as file:
        dump = mwxml.Dump.from_file(file)
        target_title_lower = target_title.lower()
        print(f"Поиск в файле: {filename}")

        found_in_file = False
        page_count = 0
        for page in dump:
            page_count += 1
            if page.title.lower() == target_title_lower:
                found_in_file = True
                print(f"Статья найдена в файле: {filename}")
                for revision in page:
                    summary = parse_revision(revision)
                    return summary
                break
            else:
                print(f'Статья №{page_count} - {page.title} не совпадает с запросом {target_title}.')
                # Очистка мусора из оперативной памяти
                time.sleep(0.009)
                wikicode = None
                text = None
                del wikicode, text
                gc.collect()

        if not found_in_file:
            print(f"Статья не была найдена в файле: {filename}.")

        file_path = f'{target_title}.txt'
        if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

        return None