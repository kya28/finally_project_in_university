# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'am.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from ipywidgets.widgets import widget
from sqlalchemy import null

import processing_data
import neiron_lan


class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("выбросы аммиака")
        MainWindow.resize(398, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 240, 381, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        rows = processing_data.select_data()
        self.tableWidget.setRowCount(len(rows))
        ii = 0
        while ii <= len(rows):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(ii, QtWidgets.QTableWidgetItem(item))
            ii += 1
        jj = 0
        while jj <= 6:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(jj, QtWidgets.QTableWidgetItem(item))
            jj += 1
        j = 0
        for i in range(len(rows)):
            while j <= 6:
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(item))
                j += 1
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 261, 231))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_2.setToolTipDuration(-1)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setToolTipDuration(-1)
        self.label.setObjectName("label")
        self.line_edit_pressure = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_pressure.setGeometry(QtCore.QRect(130, 160, 113, 20))
        self.line_edit_pressure.setObjectName("line_edit_pressure")
        self.line_edit_date = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_date.setGeometry(QtCore.QRect(130, 10, 113, 20))
        self.line_edit_date.setObjectName("line_edit_date")
        self.line_edit_date = self.tableWidget.currentItem()
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 91, 16))
        self.label_5.setToolTipDuration(-1)
        self.label_5.setObjectName("label_5")
        self.line_edit_temperature = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_temperature.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.line_edit_temperature.setObjectName("line_edit_temperature")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_3.setToolTipDuration(-1)
        self.label_3.setObjectName("label_3")
        self.line_edit_concentration = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_concentration.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.line_edit_concentration.setObjectName("line_edit_concentration")
        self.line_edit_speed = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_speed.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.line_edit_speed.setObjectName("line_edit_speed")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.label_4.setToolTipDuration(-1)
        self.label_4.setObjectName("label_4")
        self.line_edit_humidity = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_humidity.setGeometry(QtCore.QRect(130, 120, 113, 20))
        self.line_edit_humidity.setObjectName("line_edit_humidity")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_6.setToolTipDuration(-1)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: onDelete_data(self))#lambda: processing_data.func_drop_bd(self.line_edit_date.text()))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: onAdd_data(self))
        self.pushButton_Con = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Con.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.pushButton_Con.setObjectName("pushButton_Con")
        self.pushButton_Con.clicked.connect(lambda: onNeiron_lan(self))
        self.label_load = QtWidgets.QLabel(self.centralwidget)
        self.label_load.setGeometry(QtCore.QRect(300, 150, 75, 23))
        self.label_load.setToolTipDuration(-1)
        self.label_load.setObjectName("label_load")
        self.pushButton_3.clicked.connect(lambda: onDelete_data(self))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.strDate = QString()
        #self.strDate = self.line_edit_date.text()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Экологический мониторинг выбросов"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Концентрация"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Температура"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Скорость ветра"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Влажность"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Давление"))
        rows = processing_data.select_data()
        i = 0
        for row in rows:
            if i == len(rows):
                break
            else:
                for j in range(len(row)):
                    item = self.tableWidget.verticalHeaderItem(i)
                    item.setText(_translate("MainWindow", str(i + 1)))
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
            i += 1
        self.label_2.setText(_translate("MainWindow", "Температура:"))
        self.label.setText(_translate("MainWindow", "Дата:"))
        self.label_5.setText(_translate("MainWindow", "Концентрация:"))
        self.label_3.setText(_translate("MainWindow", "Скорость ветра:"))
        self.label_4.setText(_translate("MainWindow", "Влажность:"))
        self.label_6.setText(_translate("MainWindow", "Давление:"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_4.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_Con.setText(_translate("MainWindow", "Рассчитать"))


def onNeiron_lan(self):
    self.label_load.setText("Рассчитываю..")
    self.line_edit_concentration.setText(str(neiron_lan.neiron_lan(int(self.line_edit_temperature.text()),
                                                                   int(self.line_edit_speed.text()),
                                                                   int(self.line_edit_humidity.text()),
                                                                   int(self.line_edit_pressure.text()))))
    self.label_load.setText("Готово")


def add_data(date, concentration, temperature, speed, humidity, pressure):
    print(date, concentration, temperature, speed, humidity, pressure)
    con = psycopg2.connect(
        database="ammonia",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute(
        "INSERT INTO con_data (date, concentration)  VALUES (%s, %s)", (date, concentration))
    cur.execute(
        "INSERT INTO factors (date, temperature, speed, humidity, pressure) VALUES (%s, %s, %s, %s, %s)",
        (date, temperature, speed, humidity, pressure))
    con.commit()
    con.close()
    add_data(
        line_edit_date.text(),
        line_edit_concentration.text(),
        line_edit_temperature.text(),
        line_edit_speed.text(),
        line_edit_humidity.text(),
        line_edit_pressure.text()
    )


def onAdd_data(self):
    self.label_load.setText("Добавлено")


def onDelete_data(self):
    lambda: processing_data.func_drop_bd(self.line_edit_date.text(self))
    self.label_load.setText("Удалено")


class Modal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(200, 200)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
