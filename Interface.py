import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QFrame, QTextEdit, QDialog

from main_interface import Ui_MainWindow
from dialog import Ui_Dialog
import NLP as nlp


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.mic_button.clicked.connect(self.opndlg)

    def addchat(self, obj=None, flag=0, text=None):
        if(text=="Sorry, I could not understand your speech." or text=="Sorry, an error occurred"):
            flag=2
        if(flag==0):
            user="User:\n"
        else:
            user="KCLERY:\n"
        text_edit = QTextEdit()
        text_edit.setPlainText(user+text)
        text_edit.setReadOnly(True)
        text_edit.setMinimumHeight(100)
        text_edit.setMaximumHeight(100)
        text_edit.setMaximumWidth(350)
        text_edit.setContentsMargins(1, 1, 1, 1)
        text_edit.setFrameShape(QFrame.Shape.Box)
        if(flag==0):
            text_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            color="lightgreen"
        else:
            text_edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
            color="magenta"
        text_edit.setStyleSheet("QTextEdit {"
                                "background-color:"+color+";"
                                "border-radius: 10px;"

                                "}"
                                """QScrollBar:vertical {
    background: transparent;
    width: 5px; /* Adjust the width of the scrollbar */
}

QScrollBar::handle:vertical {
    background: blue; /* Scrollbar handle color */
    border-radius: 2px;/* Rounded corners */
}





QScrollBar::handle:vertical:hover {
    background: #505050; /* Hovered color */
}


QScrollBar::handle:vertical:pressed {
    background: #303030; /* Pressed color */
}


QScrollBar::sub-page:vertical {
    background: transparent;
}

QScrollBar::add-page:vertical {
    background: transparent;
}


QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    width: 0;
}


QScrollBar::sub-line:vertical {
    border: none;
    background: transparent;
}


QScrollBar::sub-line:vertical:pressed {
    background: transparent;
}


QScrollBar::add-line:vertical {
    border: none;
    background: transparent;
}


QScrollBar::add-line:vertical:pressed {
    background: transparent;
}
""")

        self.verticalLayout_2.addWidget(text_edit)
        QTimer.singleShot(100, self.scrblw)
        self.verticalLayout_2.setSpacing(18)
        if obj != None and (flag==0 or flag==2):
            obj.cls()

    def scrblw(self):
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def opndlg(self):
        opn = dlg(self)
        QTimer.singleShot(50, lambda: self.lp(opn))
        opn.exec()

    def lp(self, obj):
        arr = nlp.lang_process()
        if arr[0]:
            self.addchat(obj, 0, arr[1])


class dlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def cls(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
