import datetime  # Импортируем модуль для работы с датой и временем
import locale  # Импортируем модуль для работы с локалью
import AuroraSay  # Импортируем модуль для синтеза речи
import time  # Импортируем модуль для работы со временем


def get_current_time():
    """
    Функция для получения текущей даты и времени на русском языке и передачи их для синтеза речи.

    Возвращает:
    None
    """
    current_time = datetime.datetime.now()  # Получаем текущую дату и время
    hour = current_time.hour  # Получаем текущий час
    minute = current_time.minute  # Получаем текущую минуту
    second = current_time.second  # Получаем текущую секунду
    year = current_time.year  # Получаем текущий год
    month_num = current_time.month  # Получаем номер текущего месяца
    day = current_time.day  # Получаем текущий день

    # Устанавливаем русскую локаль для модуля locale
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    # Получаем название текущего месяца на русском языке
    month_name = current_time.strftime("%B")

    print("Текущая дата и время:")
    print(
        f"Сейчас {hour} часов, {minute} минут, {second} секунд, {year} год, {month_name} месяц, {day} число.")

    AuroraSay.AuroraSay(
        "Сейчас {} часов, {} минут, {} секунд, {} год, {} месяц, {} число.".format(
            hour, minute, second, year, month_name, day))
    # Вызываем функцию синтеза речи для озвучивания текущей даты и времени
    print(
        "Аврора: Сейчас {} часов, {} минут, {} секунд, {} год, {} месяц, {} число.".format(
            hour,
            minute,
            second,
            year,
            month_name,
            day))
    # Выводим текущую дату и время в консоль
