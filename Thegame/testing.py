from PyQt5.QtWidgets import *
from GameWindows import progressBar
import sys
import time

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.p = progressBar(self, 10, 0, 5, 5, 100, 20)

    def startIt(self):
        for i in range(0, 10):
            self.p.setValue(i)
            app.processEvents()
            time.sleep(0.1)





app = QApplication(sys.argv)
win = MyWindow()
win.show()
win.startIt()
sys.exit(app.exec_())

