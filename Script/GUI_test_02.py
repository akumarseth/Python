import os
import re
from PyQt5 import QtWidgets, QtGui, QtCore


class WordGame(QtWidgets.QWidget):
    """ GUI Class Buttons, Labels, Graphics, Images. If Images not visible - PYTHONPATH incorrect! """

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.center()
        self.setStyleSheet("background: qlineargradient(x1:1, x2:0, stop:0 #672491, stop:1 #777777);")
        self.wordbtn1 = QtWidgets.QPushButton("Browse", self)
        self.wordbtn1.setStyleSheet("background-color: #777777; color: #FFFD77;")
        self.wordbtn1.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordle1 = QtWidgets.QLineEdit(self)
        self.wordle1.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordle1.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordle2 = QtWidgets.QLineEdit(self)
        self.wordle2.setStyleSheet("padding: 14px; background-color: #777777; color: #141414;")
        self.wordle2.setFont(QtGui.QFont("Tahoma", 21, 95))
        self.wordle2.setReadOnly(True)
        self.wordle2.setEchoMode(2)
        self.wordbtn2 = QtWidgets.QPushButton("PLAY", self)
        self.wordbtn2.setStyleSheet("background-color: #627419; color: #FFFD77;")
        self.wordbtn2.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordle3 = QtWidgets.QLineEdit(self)
        self.wordle3.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordle3.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordle3.setPlaceholderText("Input letter of You word...")
        self.wordbtn3 = QtWidgets.QPushButton("New", self)
        self.wordbtn3.setStyleSheet("background-color: #627419; color: #FFFD77;")
        self.wordbtn3.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordbtn4 = QtWidgets.QPushButton("Statistics", self)
        self.wordbtn4.setStyleSheet("background-color: #627491; color: #FFFD77;")
        self.wordbtn4.setFont(QtGui.QFont("Tahoma", 10, 95))
        self.wordbtn5 = QtWidgets.QPushButton("File", self)
        self.wordbtn5.setStyleSheet("background-color: #627491; color: #FFFD77;")
        self.wordbtn5.setFont(QtGui.QFont("Tahoma", 10, 95))
        self.wordbtn6 = QtWidgets.QPushButton("Close", self)
        self.wordbtn6.setStyleSheet("background-color: #672419; color: #FFFD77;")
        self.wordbtn6.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordte = QtWidgets.QTextEdit(self)
        self.wordte.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordte.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordte.setReadOnly(True)
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.wordbtn1, 0, 0, 1, 1)
        self.grid.addWidget(self.wordle1, 0, 1, 1, 3)
        self.grid.addWidget(self.wordle2, 1, 0, 1, 4)
        self.grid.addWidget(self.wordbtn2, 2, 0, 1, 1)
        self.grid.addWidget(self.wordle3, 2, 1, 1, 3)
        self.grid.addWidget(self.wordbtn3, 3, 0, 1, 1)
        self.grid.addWidget(self.wordbtn4, 3, 1, 1, 1)
        self.grid.addWidget(self.wordbtn5, 3, 2, 1, 1)
        self.grid.addWidget(self.wordbtn6, 3, 3, 1, 1)
        self.grid.addWidget(self.wordte, 4, 0, 1, 4)
        self.setLayout(self.grid)
        self.wgtime1 = QtCore.QTimer()
        self.wgtime1.start(100)
        self.wgtime2 = QtCore.QTimer()
        self.wgtime2.start(150)
        self.wordbtn1.clicked.connect(self.word_btn1)
        self.wordbtn2.clicked.connect(self.word_btn2)
        self.wordbtn3.clicked.connect(self.word_btn3)
        self.wordbtn4.clicked.connect(self.word_btn4)
        self.wordbtn5.clicked.connect(self.word_btn5)
        self.wordbtn6.clicked.connect(self.word_btn6)
        self.wgtime1.timeout.connect(self.on_wgtime1)
        self.wgtime2.timeout.connect(self.on_wgtime2)
        self.wgame = 0
        self.wscore = 0
        self.wbeep = 0
        self.wlost = 0
        self.wordfind = r"([\`а-яА-ЯёЁA-Za-z0-9]+)\s"

    """ OPEN FILES """

    def word_btn1(self):
        self.wbeep = 0
        self.wordte.clear()
        self.wordte.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordte.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.wordfile1 = QtWidgets.QFileDialog.getOpenFileName(self, caption="Images", directory=QtCore.QDir.homePath())
        if self.wordfile1 is not None:
            path1 = os.path.dirname(self.wordfile1[0])
            sys.path.append(str(path1))
            self.wordle1.setText(str(self.wordfile1[0]))
            self.fileread1 = open(self.wordfile1[0], 'r')
            self.fileread12 = self.fileread1.read()
            with open(self.wordfile1[0], 'r') as fileread13:
                self.counter51 = fileread13.readlines()
            self.filestring1 = self.fileread12.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').replace('\v',
                                                                                                                ' ').replace(
                '\f', ' ').replace('\a', ' ').replace('\b', ' ')

    """ START PLAY """

    def word_btn2(self):
        self.wmatch = 0
        self.wgame += 1
        self.wordte.clear()
        self.wordte.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordte.setFont(QtGui.QFont("Tahoma", 12, 95))
        self.word21 = self.wordle3.text()
        self.word22 = self.word21.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').replace('\v', ' ').replace(
            '\f', ' ').replace('\a', ' ').replace('\b', ' ')
        self.word23 = re.findall(r"%s" % (self.word22), self.filestring1, re.S)
        self.word24 = re.findall(self.wordfind, self.filestring1, re.S)
        for w21 in self.word24[0:]:
            if w21 == self.word22:
                self.wmatch += 1
        if len(self.word23) > 0:
            self.wordle2.setStyleSheet("padding: 14px; background-color: #627419; color: #141414;")
            self.wordle2.setEchoMode(2)
            self.wordle2.setText(self.word22)
            self.wbeep = 0
            if self.word22 in self.word24:
                self.wordle2.setEchoMode(0)
                self.wordle2.setText(self.word22)
                self.wordle2.setStyleSheet("padding: 14px; background-color: #627419; color: #01FFD9;")
                self.wordte.setText("YOU")
                self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                self.wordte.append("WINNER !!!")
                self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                self.wordte.setStyleSheet("background-color: #627419; color: #01FFD9;")
                self.wordte.setFont(QtGui.QFont("Tahoma", 34, 95))
                self.wbeep = 1
                self.wscore += 1
                if len(self.word22) == 2:
                    self.wscore += 100
                if len(self.word22) == 3:
                    self.wscore += 1000
                if len(self.word22) == 4:
                    self.wscore += 10000
                if len(self.word22) == 5:
                    self.wscore += 100000
                if len(self.word22) == 6:
                    self.wscore += 1000000
                if len(self.word22) == 7:
                    self.wscore += 10000000
                """ SCORES """
                self.wordte.moveCursor(1)
                if self.wscore > 1000:
                    if self.wscore < 10000:
                        self.wordte.insertPlainText("PRIVATE\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 10000:
                    if self.wscore < 100000:
                        self.wordte.insertPlainText("CORPORAL\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 100000:
                    if self.wscore < 1000000:
                        self.wordte.insertPlainText("SERGEANT\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 1000000:
                    if self.wscore < 10000000:
                        self.wordte.insertPlainText("LEUTENANT\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 10000000:
                    if self.wscore < 100000000:
                        self.wordte.insertPlainText("CAPTAIN\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 100000000:
                    if self.wscore < 1000000000:
                        self.wordte.insertPlainText("MAJOR\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 1000000000:
                    if self.wscore < 10000000000:
                        self.wordte.insertPlainText("COLONEL\n")
                        self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                if self.wscore > 10000000000:
                    self.wordte.insertPlainText("GENERAL\n")
                    self.wordte.setAlignment(QtCore.Qt.AlignCenter)
        if len(self.word23) == 0:
            self.wordle2.setEchoMode(0)
            fault1 = "x" * len(self.word22)
            self.wordle2.setText(fault1)
            self.wbeep = 0
            self.wordle2.setStyleSheet("padding: 14px; background-color: #627419; color: #672419;")
            if self.word22 not in self.word24:
                self.wlost -= 10
                self.wordte.setText("YOU")
                self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                self.wordte.append("LOST !!!")
                self.wordte.setAlignment(QtCore.Qt.AlignCenter)
                self.wordte.setStyleSheet("background-color: #672419; color: #141414;")
                self.wordte.setFont(QtGui.QFont("Tahoma", 34, 95))

    """ NEW GAME """

    def word_btn3(self):
        self.wgame = 0
        self.wmatch = 0
        self.wscore = 0
        self.wbeep = 0
        self.wlost = 0
        self.wordle2.clear()
        self.wordle2.setStyleSheet("padding: 14px; background-color: #777777; color: #141414;")
        self.wordle3.clear()
        self.wordte.clear()
        self.wordte.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordte.setFont(QtGui.QFont("Tahoma", 12, 95))

    """ STATISTICS """

    def word_btn4(self):
        self.wbeep = 0
        self.wordte.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordte.setFont(QtGui.QFont("Tahoma", 12, 95))
        try:
            if self.wscore < 1000:
                f40 = "Rank  :  Pink Girl" + '\n'
            if self.wscore > 1000:
                f40 = "Rank  :  Private" + '\n'
            if self.wscore > 10000:
                f40 = "Rank  :  Corporal" + '\n'
            if self.wscore > 100000:
                f40 = "Rank  :  Sergeant" + '\n'
            if self.wscore > 1000000:
                f40 = "Rank  :  Leutenant" + '\n'
            if self.wscore > 10000000:
                f40 = "Rank  :  Captain" + '\n'
            if self.wscore > 100000000:
                f40 = "Rank  :  Major" + '\n'
            if self.wscore > 1000000000:
                f40 = "Rank  :  Colonel" + '\n'
            if self.wscore > 10000000000:
                f40 = "Rank  :  General" + '\n'
            f41 = "Games  :  " + str(self.wgame) + "\n"
            f42 = "Matches  :  " + str(self.wmatch) + "\n"
            f43 = "Success score  :  " + str(self.wscore) + "\n"
            f44 = "Lost score  :  " + str(abs(self.wlost)) + "\n"
            f45 = "Total Score  :  " + str(self.wscore + self.wlost) + "\n"
            f46 = f40 + f41 + f42 + f43 + f44 + f45
            self.wordte.setText(str(f46))
        except:
            self.wordte.setText("Choose File !")
            self.wordte.setStyleSheet("background-color: #777777; color: #672419;")
            self.wordte.setFont(QtGui.QFont("Tahoma", 19, 95))
            self.wordte.setAlignment(QtCore.Qt.AlignCenter)

    """ READ FILES """

    def word_btn5(self):
        self.wbeep = 0
        self.wordte.setStyleSheet("background-color: #777777; color: #141414;")
        self.wordte.setFont(QtGui.QFont("Tahoma", 12, 95))
        try:
            word51 = re.findall(self.wordfind, self.filestring1, re.S)
            f51 = os.path.basename(self.wordfile1[0])
            f52 = "File name  :  " + str(f51) + "\n"
            f53 = "File size  :  " + str(os.path.getsize(self.wordfile1[0])) + " bytes" + "\n"
            f54 = "Characters in file  :  " + str(len(self.fileread12)) + "\n"
            f55 = "Lines in file  :  " + str(len(self.counter51)) + "\n"
            f56 = "Words in file  :  " + str(len(word51)) + "\n"
            f57 = f52 + f53 + f54 + f55 + f56
            self.wordte.setText(str(f57))
        except:
            self.wordte.setText("Choose File !")
            self.wordte.setStyleSheet("background-color: #777777; color: #672419;")
            self.wordte.setFont(QtGui.QFont("Tahoma", 19, 95))
            self.wordte.setAlignment(QtCore.Qt.AlignCenter)

    def word_btn6(self):
        self.wbeep = 0
        self.close()

    def on_wgtime1(self):
        if self.wbeep == 1:
            self.wordte.setStyleSheet("background-color: #627419; color: #01FFD9;")

    def on_wgtime2(self):
        if self.wbeep == 1:
            self.wordte.setStyleSheet("color: #FFFFFF;")

    def center(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = WordGame()
    window.show()
    sys.exit(app.exec_())