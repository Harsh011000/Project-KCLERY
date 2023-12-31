import os
import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFrame, QTextEdit, QDialog

import NLP as nlp
import Ai_NLP as ai_nlp
from dialog import Ui_Dialog
import forMusic
import MusicPorcessingFile
from main_interface import Ui_MainWindow

basedir = os.path.dirname(__file__)
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'DH Dash.KCLERY.1.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.mic_button.clicked.connect(self.opndlg)
        self.music_button.clicked.connect(self.musicWindow)
        self.enter_button.clicked.connect(self.enter)
        self.threadpool = QThreadPool()

    def addchat(self, obj=None, flag=0,text=None,music=None):

        if self.dlg_val == 0:
            if (text == "Sorry, I could not understand your speech." or text == "Sorry, an error occurred"):
                flag = 2
            if (flag == 0):
                user = ai_nlp.username.capitalize()+":\n"
            else:
                user = "KCLERY:\n"
            text_edit = QTextEdit()
            text_edit.setPlainText(user + text)
            text_edit.setReadOnly(True)
            text_edit.setMinimumHeight(100)
            text_edit.setMaximumHeight(100)
            text_edit.setMaximumWidth(350)
            text_edit.setContentsMargins(1, 1, 1, 1)
            text_edit.setFrameShape(QFrame.Shape.Box)
            if (flag == 0):
                text_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
                # color = "lightgreen"
                color ="#A6FF96"
            else:
                text_edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
                # color = "magenta"
                color = "#F2EE9D"
            text_edit.setStyleSheet("QTextEdit {"
                                    "background-color:" + color + ";"
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
            if obj != None and (flag == 0 or flag == 2):
                obj.cls()
            if flag == 0 and music==None:
                self.thread2(text)
            if flag==0 and music==1:
                self.musicThread2(text)

    def scrblw(self):
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def enter(self):
        text=self.extract_text()
        text=text.lower()
        if text!="":
            self.dlg_val=0
            self.addchat(flag=0,text=text)
    def extract_text(self):
        text=str(self.textEdit.toPlainText())
        self.textEdit.setPlainText("")
        return text


    def opndlg(self):
        opn = dlg(self)
        self.dlg_val = 0
        opn.finished.connect(self.close_dlg)
        QTimer.singleShot(50, lambda: self.thread(opn))
        opn.exec()

    def close_dlg(self):
        self.dlg_val = 1;

    def lp(self, arr):

        self.addchat(arr[0], 0, arr[1])

    def lp2(self, arr):
        self.addchat(arr[0], 0, arr[1] ,1)

    def thread(self, obj):
        worker = Worker(obj)
        worker.signal.finish.connect(self.lp)
        self.threadpool.start(worker)

    def thread2(self, text):
        worker2 = Worker2(text)
        worker2.signal.finish.connect(self.get_ai_respo)
        self.threadpool.start(worker2)
    def musicThread(self,obj):
        musicworker = MusicWorker(obj)
        musicworker.signal.Musicfinish.connect(self.lp2)
        self.threadpool.start(musicworker)

    def musicThread2(self,obj):
        musicworker2 = music(obj)
        musicworker2.signal.Musicfinish.connect(self.get_ai_respo)
        self.threadpool.start(musicworker2)
    def get_ai_respo(self, arr):
        if arr[0]=="init":
            self.dlg_val = 0
            self.addchat(flag=1, text=arr[1])
        if arr[0] == 1:
            respo = ai_nlp.app_open_rspo(arr[1])
            self.dlg_val = 0
            if respo!="App not Found":
                self.addchat(flag=1, text="Opening "+respo)
                QTimer.singleShot(2000,lambda :ai_nlp.opn_app(respo))
            else:
                self.addchat(flag=1, text=respo)
        if arr[0]==2:
            respo=ai_nlp.app_close_rspo(arr[1])
            self.dlg_val=0
            if respo!="App not Found" :
                respotext=ai_nlp.crt_nm(respo)
                self.addchat(flag=1, text="Closing "+respo)
                QTimer.singleShot(2000,lambda :ai_nlp.cls_app(respotext))
            else:
                self.addchat(flag=1, text=respo)
        if arr[0]==3:
            respo=ai_nlp.dirct_rspo(arr[1])
            self.dlg_val=0
            if respo!="Disk/Drive not found":
                self.addchat(flag=1,text="Opening dir "+respo)
                QTimer.singleShot(2000,lambda :ai_nlp.opn_dir(respo))
            else:
                self.addchat(flag=1,text=respo)
        if arr[0]==4:
            SearchKey=ai_nlp.filter_google(arr[1])
            filterdSearch=ai_nlp.clear_google(SearchKey)
            self.dlg_val=0
            self.addchat(flag=1, text="opening browser to Search " +filterdSearch)
            QTimer.singleShot(2000, lambda: ai_nlp.search_google(filterdSearch))
        if arr[0]==5:
            respo=ai_nlp.cust_set(arr[1])
            self.dlg_val=0
            self.addchat(flag=1,text="Setting Custom command:-\n"+respo)
        if arr[0]==-4:
            self.dlg_val = 0
            self.addchat(flag=1, text=arr[1])
        if arr[0]==-1:
            self.dlg_val=0
            self.addchat(flag=1,text=arr[1])
        if arr[0]==-2:
            filterdSearch = ai_nlp.clear_google(arr[1])
            self.dlg_val = 0
            self.addchat(flag=1, text="opening browser to Search " + filterdSearch)
            QTimer.singleShot(2000, lambda: ai_nlp.search_google(filterdSearch))
        if arr[0]==10:
            self.dlg_val = 0
            self.addchat(flag=1, text="Searching on Youtube Music")
            QTimer.singleShot(2000, lambda: MusicPorcessingFile.musicProcess(arr[1]))
        if arr[0]==20:
            self.dlg_val = 0
            self.addchat(flag=1, text="Searching on Spotify")
            QTimer.singleShot(2000, lambda: MusicPorcessingFile.musicProcess(arr[1]))
        if arr[0]==30:
            self.dlg_val = 0
            self.addchat(flag=1, text="Searching on Amazon Music")
            QTimer.singleShot(2000, lambda: MusicPorcessingFile.musicProcess(arr[1]))
        if arr[0]==40:
            self.dlg_val = 0
            self.addchat(flag=1, text="Searching on Jio Saavn")
            QTimer.singleShot(2000, lambda: MusicPorcessingFile.musicProcess(arr[1]))
        if arr[0]==50:
            self.dlg_val = 0
            self.addchat(flag=1, text="Searching on Apple Music")
            QTimer.singleShot(2000, lambda: MusicPorcessingFile.musicProcess(arr[1]))
        if arr[0]==60:
            self.dlg_val = 0
            self.addchat(flag=1, text="Searching on Gaana")
            QTimer.singleShot(2000, lambda: MusicPorcessingFile.musicProcess(arr[1]))
        if arr[0]==0:
            self.dlg_val = 0
            self.addchat(flag=1, text="Sorry I can't understand. Please try again.")
    def musicWindow(self):
        opnmmic = dlg(self)
        self.dlg_val = 0
        opnmmic.finished.connect(self.close_dlg)
        QTimer.singleShot(50, lambda: self.musicThread(opnmmic))
        opnmmic.exec()

class dlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def cls(self):
        self.close()


class Worker(QRunnable):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        text = nlp.lang_process()
        arr = [self.obj, text]
        self.signal.finish.emit(arr)


class Worker2(QRunnable):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        arr = ai_nlp.response(self.text)
        self.signal.finish.emit(arr)


class MusicWorker(QRunnable):
    def __init__(self, obj):
        super().__init__()
        self.musicobj= obj
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        musicText = forMusic.music_process()
        musiclist=[self.musicobj,musicText]
        self.signal.Musicfinish.emit(musiclist)

class music(QRunnable):
    def __init__(self, text):
        super().__init__()
        self.musictext = text
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        arr = forMusic.musicSearch(self.musictext)
        self.signal.Musicfinish.emit(arr)
class WorkerSignals(QObject):
    finish = pyqtSignal(list)
    Musicfinish = pyqtSignal(list)

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
