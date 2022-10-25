import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel

# Подкласс QMainWindow для настройки главного окна приложения
from PyQt6.uic.uiparser import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выбросы")

        line_edit_date = QLineEdit()
        line_edit_temperature = QLineEdit()
        line_edit_speed = QLineEdit()
        line_edit_humidity = QLineEdit()
        line_edit_pressure = QLineEdit()
        line_edit_concentration = QLineEdit()
        label_date = QLabel("Дата:")
        label_temperature = QLabel("Температура:")
        label_speed = QLabel("Скорость ветра:")
        label_humidity = QLabel("Влажность:")
        label_pressure = QLabel("Давление:")
        label_concentration = QLabel("Концентрация:")
        button_add = QPushButton("Добавить")
        button_upgrate = QPushButton("Обновить")
        button_drop = QPushButton("Удалить")
        button_close = QPushButton("Закрыть")

        box = QVBoxLayout()
        box.addWidget(label_date)
        box.addWidget(line_edit_date)
        box.addWidget(label_temperature)
        box.addWidget(line_edit_temperature)
        box.addWidget(label_speed)
        box.addWidget(line_edit_speed)
        box.addWidget(label_humidity)
        box.addWidget(line_edit_humidity)
        box.addWidget(label_pressure)
        box.addWidget(line_edit_pressure)
        box.addWidget(label_concentration)
        box.addWidget(line_edit_concentration)

        box.addWidget(button_add)
        box.addWidget(button_upgrate)
        box.addWidget(button_drop)
        box.addWidget(button_close)

        container = QWidget()
        container.setLayout(box)

        self.setCentralWidget(container)

    # self.setFixedSize(QSize(600, 600))


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()


