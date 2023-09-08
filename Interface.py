import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QFrame, QTextEdit

from main_interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.mic_button.clicked.connect(self.btnclk)

    def btnclk(self):
        text_edit = QTextEdit()
        text_edit.setPlainText(
            f"The sun dipped below the horizon, \ncasting a warm, golden hue across the\n tranquil beach. Waves gently lapped at the shore, \ncreating a soothing \nsymphony of nature's melody. Seagulls soared gracefully in the fading light, \nwhile a couple strolled hand in hand, \ntheir footprints etching a fleeting memory in the sand. As the day surrendered to the night, a \nsense of peace enveloped the world, reminding \nus of the simple beauty that exists in \neach passing moment.")
        text_edit.setReadOnly(True)
        text_edit.setMinimumHeight(100)
        text_edit.setMaximumHeight(300)
        text_edit.setContentsMargins(1, 1, 1, 1)
        text_edit.setFrameShape(QFrame.Box)
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
        "border-radius: 5px;"
        "}"
        "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
        "background: none;"
        "}")
        self.verticalLayout_2.addWidget(text_edit)
        # label = QLabel("The sun dipped below the horizon, \ncasting a warm, golden hue across the\n tranquil beach. Waves gently lapped at the shore, \ncreating a soothing \nsymphony of nature's melody. Seagulls soared gracefully in the fading light, \nwhile a couple strolled hand in hand, \ntheir footprints etching a fleeting memory in the sand. As the day surrendered to the night, a \nsense of peace enveloped the world, reminding \nus of the simple beauty that exists in \neach passing moment.")
        # label.setMinimumHeight(100)
        # label.setMaximumHeight(100)
        # label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        # #label.adjustSize()
        # label.setMargin(1)
        # label.setFrameShape(QFrame.Box)
        # self.verticalLayout_2.addWidget(label)
        # spacer = QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Fixed)
        # self.verticalLayout_2.addItem(spacer)
        # self.verticalLayout_2.setSpacing(0)
        # self.verticalLayout_2.setSizeConstraint(QVBoxLayout.SetMinimumSize)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
