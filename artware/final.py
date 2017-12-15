from PyQt5.QtWidgets import * # qApp is in here!
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtMultimedia import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        banner = QLabel(self)
        pixmap = QPixmap('01.jpg')
        banner.setPixmap(pixmap)

        profile = QLabel(self)
        pixmap = QPixmap('4.jpg')
        profile.setPixmap(pixmap)

        pic = QLabel(self)
        a = '5.jpg'
        pixmap = QPixmap(a)
        pic.setPixmap(pixmap)

        heart = QLabel(self)
        pixmap = QPixmap('b1.jpg')
        heart.setPixmap(pixmap)

        icon = QLabel(self)
        pixmap = QPixmap('6.jpg')
        icon.setPixmap(pixmap)

        caption = QLabel(self)
        pixmap = QPixmap('7.jpg')
        caption.setPixmap(pixmap)

        button = QPushButton("Let's upgrade!")
        button.clicked.connect(self.newversion)


        grid = QGridLayout()
        grid.setSpacing(0)
        grid.addWidget(banner, 0, 0, 1, 4)
        grid.addWidget(profile, 1, 0, 1, 4)
        grid.addWidget(pic, 2, 0, 1, 4)
        grid.setRowStretch(2, 1)
        grid.addWidget(icon, 3, 0, 1, 3)
        grid.addWidget(heart, 3, 0, 1, 1)
        grid.addWidget(caption, 4, 0, 1, 1)
        grid.setRowStretch(4, 1)
        grid.addWidget(button, 5, 0)

        mainwidget = QWidget()
        mainwidget.setLayout(grid)
        mainwidget.setObjectName("main")
        self.setCentralWidget(mainwidget)
        self.setWindowTitle("Style Me")
        self.setGeometry(20,20, 500, 600)
        self.show()

    def newversion(self):
        win.hide()
        win2.show()
        QMessageBox.about(self, "New Version is Out Now!", "You can give unlimited amounts of LIKE to other users, so that you can gain more attention from them :D")

class MyWindow2(QWidget):
        def __init__(self, xpos=40, ypos=40):
            super(MyWindow2, self).__init__()
            self.initGUI(xpos, ypos)

        def initGUI(self, xpos, ypos):




            bg = QLabel(self)
            pixmap = QPixmap('bg.jpg')
            bg.setPixmap(pixmap)

            self.button = QPushButton(self)
            self.button.setIcon(QtGui.QIcon("11.jpg"))
            self.button.setStyleSheet("QPushButton{background: transparent;}")
            self.button.setIconSize(QtCore.QSize(400,380))
            self.button.pressed.connect(self.turnOn)
            self.button.released.connect(self.turnOff)

            self.setWindowTitle("NewVersion")
            self.setGeometry(20,20, 500, 700)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.move(xpos, ypos)

        def turnOn(self):
            QSound("kiss.wav").play()
            self.button.setIcon(QtGui.QIcon("10.jpg"))
            print "+1 like"

        def turnOff(self):
            self.button.setIcon(QtGui.QIcon("11.jpg"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win2 = MyWindow2(40, 40)
    sys.exit(app.exec_())
