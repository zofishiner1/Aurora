import random

# База данных слов с указанием части речи
word_database = {
    "существительное": ["привет", "друзья", "вопрос", "ответ", "разговор"],
    "прилагательное": ["хороший", "плохой", "интересный", "забавный", "серьезный"],
    "глагол": ["говорить", "слушать", "спрашивать", "отвечать", "обсуждать"],
    "наречие": ["вежливо", "настойчиво", "осторожно", "весело", "искренне"]
}

# Правила согласования частей речи
part_of_speech_rules = {
    "существительное": ["прилагательное", "глагол"],
    "прилагательное": ["существительное"],
    "глагол": ["существительное", "наречие"],
    "наречие": ["глагол"]
}

def generate_sentence():
    # Выбираем случайную начальную часть речи
    current_part_of_speech = random.choice(list(part_of_speech_rules.keys()))

    sentence = []

    # Генерируем предложение
    while len(sentence) < 4:
        # Выбираем случайное слово для текущей части речи
        word = random.choice(word_database[current_part_of_speech])
        sentence.append(word)

        # Определяем, какие части речи могут следовать за текущей
        next_part_of_speech = random.choice(part_of_speech_rules[current_part_of_speech])
        current_part_of_speech = next_part_of_speech

    # Формируем предложение
    return " ".join(sentence) + "."

def handle_user_input():
    user_input = input("Введите что-нибудь: ")
    response = generate_sentence()
    print(f"Ответ: {response}")

if __name__ == "__main__":
    handle_user_input()
