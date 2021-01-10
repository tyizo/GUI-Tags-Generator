# By Tyizo => @1xm0d
try:
    # Importing the library that we gonna use.
    import os
    import sys
    import random
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QFileDialog, QInputDialog
    from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal
    from pathlib import Path

except Exception as e:
    print(e)

    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init_()
            self.setGeometry(380, 380, 355, 355)
            self.setWindowTitle('Tag Generator For Any Social Media')
            os.chdir(os.path.dirname(os.path.realpath(__file__)))
            self.initUI()
            self.tag_list = self.read_tags()

    def initUI(self):

        self.gen_button = QtWidgets.QPushButton(self)
        self.gen_button.setGeometry(QtCore.QRect(270, 70, 75, 51))
        font = QtGui.QFont()
        font.setFamily('Cascadia Mono SemiBold')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gen_button.setFont(font)
        self.gen_button.setObjectName('gen_button')
        self.gen_button.setText('Generate')
        self.gen_button.clicked.connect(self.ganarate)

        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setGeometry(QtCore.QRect(10, 10, 75, 51))
        font = QtGui.QFont()
        font.setFamily('Cascadia Mono SemiBold')
        font.setBold(True)
        font.setWeight(75)

        self.show_button.setFont(font)
        self.show_button.setObjectName('show_button')
        self.show_button.setText('Show Tags')
        self.show_button.clicked.connect(self.show_all)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(13, 140, 331, 211))
        self.textEdit.setObjectName('textEdit')

        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(211, 81, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setProperty('value', 30)
        self.spinBox.setObjectName('spinBox')

        self.lcdNumber = QtWidgets.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 20, 64, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(200)

        self.lcdNumber.setFont(font)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setProperty('value', 0.0)
        self.lcdNumber.setObjectName('lcdNumber')
        self.lcdNumber.setStyleSheet('QLCDNumber { color : black }')
        self.lcdNumber.display(0)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(260, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName('label')
        self.label.setText('Tag Counter: ')


    def read_tags(self):
        tags = [

        ]
        try:
            with open('tags.txt', 'r') as file:
                for word in file.read().split(","):
                    for added in tags:
                        if word == added:
                            continue
                        tags.append(word.split('\n'))
        except Exception as A:
            return A
        return tags

    def generate(self):
        tags = [

        ]
        result = ''
        amount = self.spinBox.value()
        self.lcdNumber.display(int(len(self.tag_list)))

        while len(tags) <= amount:
            word = random.choice(self.tag_list)
            if word not in tags:
                tags.append(word)
        for word in tags:
            result += word + ' '
        self.textEdit.setText(result)

    def show_all(self):
        result = ''
        for word in self.tag_list:
            result += word + ' '
        self.textEdit.setText(result)

    def add_tags(self):
        tags = [

        ]
        start_dir = str(Path.home())
        fname, *_ = QFileDialog.getOpenFileName(self, 'Choose Text File', start_dir)

        try:

            with open(fname, 'r') as file:
                for word in file.read().split(' '):
                    for added in tags:
                        if word == added:
                            continue
                    tags.append(word.strip('\n'))

        except Exception as E:
            return E

        try:

            with open('tags.txt', 'w+') as file:
                for word in file.read().split(' '):
                    for added in tags:
                        if word == added:
                            continue
                        file.write(word + " ")

        except Exception as E:
            return E


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())