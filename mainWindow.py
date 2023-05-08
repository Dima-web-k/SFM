from ui_mainwindow import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import main
import os
import time
from threading import Thread
from audioplayer import AudioPlayer

class MainWindow(QMainWindow):
    mood = ''
    f_path = ''
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
    # def no_init(self):
    #     self.main()
    #     if self.ui.radioButton.isChecked():
    #         pass
    #     else:
    #         pass
    def main(self):
        def new():
            only_time = 900
            while only_time > 0:
                only_time -= 1
                time.sleep(1)
            self.main()

        MainWindow.mood = "," .join(main.test())

        th = Thread(target=new)
        th.start()

    def start(self):
        if MainWindow.mood == 'neutral':
            MainWindow.f_path = os.getcwd() + '\\music\\Neutral'
        elif MainWindow.mood == 'anger':
            MainWindow.f_path = os.getcwd() + '\\music\\Aggressive'
        elif MainWindow.mood == 'happy':
            MainWindow.f_path = os.getcwd() + '\\music\\Happy'
        elif MainWindow.mood == 'sadness':
            MainWindow.f_path = os.getcwd() + '\\music\\Sad'
        else:
            MainWindow.f_path = os.getcwd() + '\\music\\Neutral'

        self.ui.textEdit.setText("\n".join(os.listdir(MainWindow.f_path)))
        def sound():
            for i in os.listdir(MainWindow.f_path):
                self.ui.label.setText(i,)
                AudioPlayer(MainWindow.f_path + '\\' + i).play(block=True)
            self.start()
        th = Thread(target=sound)
        th.start()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    window.main()
    sys.exit(app.exec())