import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QLabel, QSizePolicy

from main_interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.mic_button.clicked.connect(self.btnclk)
    def btnclk(self):
        label = QLabel(f"New Label")
        label.setMinimumHeight(100)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.verticalLayout_2.addWidget(label)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()