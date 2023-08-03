from PySide6 import QtCore, QtGui, QtWidgets
import subprocess

#Replace these with your expected username and password
EXPECTED_USERNAME = "HiGitHub"
EXPECTED_PASSWORD = "GitHub@123"
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 551)
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 451, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 561))
        self.label.setStyleSheet("border-image: url(BG.jpg);\n"
"border-raduis: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 281, 381))
        self.label_2.setStyleSheet("border-radius:20px;\n"
"background-color: rgba(122, 6, 255, 100);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(105, 80, 251, 351))
        self.label_3.setStyleSheet("background-color: rgba(65, 100, 255, 150);\n"
"border-radius:20px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(190, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(132, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132 , 255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132 , 255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 330, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run_app)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def run_app(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == EXPECTED_USERNAME and password == EXPECTED_PASSWORD:
            self.open_another_application()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def open_another_application(self):
        # Replace this with the code to open the other application
        # For example, you can use subprocess.Popen to run the application
        subprocess.Popen(["python", "supermarket_wth.py"])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", " User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", " Password"))
        self.pushButton.setText(_translate("Form", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())



