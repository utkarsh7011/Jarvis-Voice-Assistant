from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JarvisUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 708)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 1351, 731))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Assets/Images/Interface/Jarvis2.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 660, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(229, 187, 255);\n"
"font: 75 20pt \"Times New Roman\";\n"
"font: 75 20pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 660, 101, 41))
        self.pushButton_2.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"background-color: rgb(255, 116, 111);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Assets/Images/Interface/Jarvis1.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1220, 650, 100, 51))
        self.textBrowser.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font-size: 8pt;\n"
"font-family: 'Segoe UI';\n"
"font-weight: bold;\n"
"border-radius:none;\n"
"padding: 5px;\n"
"border: 2px solid white;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"margin: 5px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1130, 650, 85, 51))
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font-size: 8pt;\n"
"font-family: 'Segoe UI';\n"
"font-weight: bold;\n"
"border-radius:none;\n"
"padding: 5px;\n"
"border: 2px solid white;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"margin: 5px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.terminalOutputBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.terminalOutputBox.setGeometry(QtCore.QRect(320, 600, 700, 100))
        self.terminalOutputBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.terminalOutputBox.setMouseTracking(True)
        self.terminalOutputBox.setStyleSheet("background-color: black;\n"
                                             "color: white;\n"
                                             "font-family: Courier;\n"
                                             "font-size: 10pt;")
        self.terminalOutputBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.terminalOutputBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.terminalOutputBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.terminalOutputBox.setReadOnly(True)
        self.terminalOutputBox.setPlainText("")
        self.terminalOutputBox.setOverwriteMode(True)
        self.terminalOutputBox.setCenterOnScroll(True)
        self.terminalOutputBox.setObjectName("terminalOutputBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis Voice Assistant"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_JarvisUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
