from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QWaitCondition, Qt
import os
import json

PATH = "C:/Users/timol/OneDrive/Documents/GitHub/Note/data/data.json"

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Solids calculator")
        self.setWindowIcon(QtGui.QIcon('C:/Users/timol/OneDrive/Documents/GitHub/SolidsCalculator/data/icon.ico'))
        self.component()
        self.css()

    def component(self):
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.choice = QtWidgets.QComboBox()
        self.save = QtWidgets.QPushButton("")
        self.note_list = QtWidgets.QListWidget()

        self.main_layout.addWidget(self.choice)
        self.choice.addItem("Cube")
        self.choice.addItem("Pavé droit")
        self.choice.addItem("Cone")


    def css(self):
        self.setStyleSheet("""
        background-color: #ffffff;
        """)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()