def write_note(title, content):
    """
    Функция для записи заметки.
    
    :параметр title: Название заметки
    :параметр content: Содержимое заметки
    """
    with open(f"data/notes/{title}.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Заметка '{title}' успешно записана.")

def read_note(title):
    """
    Функция для чтения заметки.
    
    :параметр title: Название заметки
    :return: Содержимое заметки
    """
    try:
        with open(f"data/notes/{title}.txt", "r", encoding="utf-8") as file:
            content = file.read()
        print(f"Содержимое заметки '{title}':")
        print(content)
        return content
    except FileNotFoundError:
        print(f"Заметка с названием '{title}' не найдена.")
        return None