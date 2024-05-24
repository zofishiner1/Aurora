import datetime
import locale
import AuroraSay
import time

def get_current_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    year = current_time.year
    month_num = current_time.month
    day = current_time.day

    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # Установка русской локали для модуля locale
    month_name = current_time.strftime("%B")

    print("Текущая дата и время:")
    print(f"Сейчас {hour} часов, {minute} минут, {second} секунд, {year} год, {month_name} месяц, {day} число.")

    AuroraSay.AuroraSay("Сейчас {} часов, {} минут, {} секунд, {} год, {} месяц, {} число.".format(hour, minute, second, year, month_name, day))
    print("Бот: Сейчас {} часов, {} минут, {} секунд, {} год, {} месяц, {} число.".format(hour, minute, second, year, month_name, day))
