from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui  import QTextCursor
from PIL import Image

class myLabel(QLabel):
    def __init__(self, window, text, font, setX, setY, width, height):
        super().__init__(window)
        self.setText(str(text))
        self.setFont(font)
        self.setGeometry(setX, setY, width, height)

    def changeText(self, newText):
        self.setText(str(newText))

    def alignCenter(self):
        self.setAlignment(QtCore.Qt.AlignCenter)

class picLabel(QLabel):
    def __init__(self, window, picture, setX, setY, width, height):
        super().__init__(window)
        self.pic = picture
        self.setX, self.setY, self.width, self.height = setX, setY, width, height
        self.setPixmap(QtGui.QPixmap(picture))
        self.setGeometry(setX, setY, width, height)

        if width == 0 and picture != "":
            self.width = Determine.getWidth(picture, height)
            self.setGeometry(setX, setY, self.width, height)

        self.setScaledContents(True)
        self.pic = picture

    def changeGeo(self, setX, setY, width, height):
        self.setGeometry(setX, setY, width, height)
        if width == 0:
            self.width = Determine.getWidth(self.pic, height)
            self.setGeometry(setX, setY, self.width, height)

        self.setX, self.setY, self.height = setX, setY, height

    def changePic(self, newPic, shouldAdjust=False):
        self.pic = newPic
        self.setPixmap(QtGui.QPixmap(newPic))
        if shouldAdjust:
            self.width = Determine.getWidth(self.pic, self.height)
            self.setGeometry(self.setX, self.setY, self.width, self.height)

class progressBar(QProgressBar):
    def __init__(self, window, maximum, current, setX, setY, width, height):
        super().__init__(window)
        self.setMaximum(maximum)
        self.setValue(current)
        self.setGeometry(setX, setY, width, height)


class myButton(QPushButton):
    def __init__(self, window, name, setX, setY, width, height):
        super().__init__(window)
        self.setText(name)
        self.setGeometry(setX, setY, width, height)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

class myCheckBox(QCheckBox):
    def __init__(self, window, picture, setX, setY, width, height):
        super().__init__(window)
        self.picture = picture
        self.setGeometry(setX, setY, width, height)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(picture), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(150, 150))


class myTextEdit(QTextEdit):
    def __init__(self, window, font, setX, setY, width, height):
        super().__init__(window)
        self.setFont(font)
        self.setGeometry(setX, setY, width, height)
        self.info = self.toPlainText()
        self.enters = True
        self.curs = self.textCursor().position()

    def keyReleaseEvent(self, e: QtGui.QKeyEvent):
        plainT = self.toPlainText()
        self.curs = self.textCursor().position()
        if len(plainT) <= 15:
            self.info = plainT
            
        elif len(plainT) < len(self.info):
            self.enters = False
            self.info = plainT
            self.setText(self.info)
            print(self.curs)
            cursor = self.textCursor()
            cursor.setPosition(self.curs)
            self.setTextCursor(cursor)


        elif len(plainT) > len(self.info):
            self.setText(self.info)
            cursor = self.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.setTextCursor(cursor)

class Determine:
    infoNeeded = [0, 0, False]
    @staticmethod
    def getWidth(image, hei):
        with Image.open(image) as img:
            width, height = img.size
        width = width/(height/hei)
        return int(width)