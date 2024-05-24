# Просто скрипт с тестовым GUI. Ничего важного нет
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class AuroraInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Аврора')
        self.setGeometry(300, 300, 400, 600)

        layout = QVBoxLayout()

        # ну основа тип
        header = QLabel('Аврора')
        header.setFont(QFont('Arial', 20))
        layout.addWidget(header)

        # поле ввода пользователя
        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        # поле вывода ответа Авроры
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        # линия кнопок
        button_bar = QWidget()
        button_bar_layout = QVBoxLayout()

        # кнопка "Команды"
        list_of_commands_button = QPushButton('Команды')
        button_bar_layout.addWidget(list_of_commands_button)

        # Кнопка "Настройки"
        settings_button = QPushButton('Настройки')
        button_bar_layout.addWidget(settings_button)

        # Кнопка "Выход"
        exit_button = QPushButton('Выход')
        exit_button.clicked.connect(self.close)  # подключаем сигнал clicked к слоту close()
        button_bar_layout.addWidget(exit_button)

        button_bar.setLayout(button_bar_layout)
        layout.addWidget(button_bar)

        self.setLayout(layout)

    def add_text_to_output(self, text):
        self.output_area.append(f'Вы: {text}')
    
        # Очищаем поле вывода ответа Авроры
        self.output_area.clear()
    
        # Добавляем ответ Авроры
        Aurora_resp = get_response(text)
        self.output_area.append(f'Аврора: {Aurora_resp}')


def get_response(input_text):
    # Здесь должен быть ваш код для получения ответа от Авроры
    return "скибиди туалет"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = AuroraInterface()
    interface.show()
    
    # Пример вызова метода add_text_to_output с ответом от Авроры
    input_text = "Привет, Аврора"
    interface.add_text_to_output(input_text)
    
    sys.exit(app.exec())
