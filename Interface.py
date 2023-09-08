import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QFrame, QTextEdit

from main_interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.mic_button.clicked.connect(self.addchat)
        #self.ui.setStyleSheet(self.ui.styleSheet())
        #self.cnt = 1
        #self.scrollArea.setStyleSheet()  # Change to your desired background color



    def addchat(self,flag=0,text=None):
        #prin = "hello" + str(self.cnt)
        text_edit = QTextEdit()
        text_edit.setPlainText("Hello\nhh\nhhhn\nhhh\n6y6y6y\ny6y6uy6u\ny6y6u6u7u\ny66uy6u7u\ny6uy6u7u7\nu7u7u")
        #self.cnt += 1
        text_edit.setReadOnly(True)
        text_edit.setMinimumHeight(100)
        text_edit.setMaximumHeight(100)
        text_edit.setMaximumWidth(350)
        text_edit.setContentsMargins(1, 1, 1, 1)
        text_edit.setFrameShape(QFrame.Box)
        text_edit.setLayoutDirection(Qt.RightToLeft)
        text_edit.setStyleSheet("QTextEdit {"
                                "background-color: lightblue;"
                                "border-radius: 10px;"

                                "}"
                                "QScrollBar:vertical {"
                                "background: #f5f5f5;"
                                "width: 5px;"
                                "}"
                                "QScrollBar::handle:vertical {"
                                "background: #999999;"
                                "min-height: 20px;"
                                "border-radius: 10px;"
                                "}"
                                "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
                                "background: none;"
                                "}")

        self.verticalLayout_2.addWidget(text_edit)
        QTimer.singleShot(100, self.scrblw)
        self.verticalLayout_2.setSpacing(18)

    def scrblw(self):
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
