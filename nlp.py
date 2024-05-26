from fuzzywuzzy import fuzz  # Импортируем функции для нечеткого сравнения строк
from fuzzywuzzy import process
import random  # Импортируем модуль для генерации случайных чисел
# Импортируем класс для взаимодействия с системой
from system_interactions import SystemInteractions
import config_loader  # Импортируем модуль для загрузки конфигурации

si = SystemInteractions()  # Создаем объект для взаимодействия с системой


class NLP:
    """
    Класс для обработки естественного языка и генерации ответов.
    """

    def __init__(self, intents):
        """
        Инициализация класса NLP.

        Аргументы:
        intents (dict) -- словарь с интентами и соответствующими ответами
        """
        self.responses = config_loader.load_intents(
        )  # Загружаем интенты и ответы из конфигурации

    def get_response(self, input_text):
        """
        Функция для получения ответа на основе входного текста.

        Аргументы:
        input_text (str) -- входной текст от пользователя

        Возвращает:
        str -- ответ бота
        """
        max_similarity = 30  # Минимальный порог схожести для выбора ответа
        # Стандартный ответ, если не найдено подходящего
        response = "Извините, я не поняла вас."
        for key in self.responses:
            # Вычисляем схожесть входного текста с ключами
            similarity = fuzz.ratio(input_text.lower(), key)
            if similarity > max_similarity:
                max_similarity = similarity
                # Выбираем случайный ответ из соответствующего списка
                response = random.choice(self.responses[key])
                if key == 'выключи':
                    si.shutdown_computer()  # Выключаем компьютер
                    pass
                elif key == 'перезагрузи':
                    si.restart_computer()  # Перезагружаем компьютер
                    pass
        return response  # Возвращаем выбранный ответ
