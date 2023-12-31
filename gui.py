from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LogInWindow(object):
    def setup_login_Ui(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(400, 400)
        LogInWindow.setMinimumSize(QtCore.QSize(400, 400))
        LogInWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(parent=LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(120, 50, 171, 31))
        self.username_input.setObjectName("username_input")
        self.username_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(140, 20, 121, 20))
        self.username_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(120, 120, 171, 31))
        self.password_input.setObjectName("password_input")
        self.password_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(140, 90, 121, 20))
        self.password_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.password_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(50, 260, 121, 51))
        self.loginButton.setIconSize(QtCore.QSize(20, 20))
        self.loginButton.setObjectName("loginButton")
        self.error_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(110, 220, 181, 41))
        self.error_message.setText("")
        self.error_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_message.setObjectName("error_message")
        self.createAccountButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createAccountButton.setGeometry(QtCore.QRect(220, 260, 121, 51))
        self.createAccountButton.setIconSize(QtCore.QSize(20, 20))
        self.createAccountButton.setObjectName("createAccountButton")
        self.type_Button_yes = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.type_Button_yes.setGeometry(QtCore.QRect(190, 180, 82, 17))
        self.type_Button_yes.setObjectName("type_Button_yes")
        self.type_Button_no = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.type_Button_no.setGeometry(QtCore.QRect(250, 180, 82, 17))
        self.type_Button_no.setObjectName("type_Button_no")
        self.create_account_type_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.create_account_type_label.setGeometry(QtCore.QRect(90, 155, 101, 51))
        self.create_account_type_label.setObjectName("create_account_type_label")
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslate_login_Ui(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

    def retranslate_login_Ui(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "Log In"))
        self.username_label.setText(_translate("LogInWindow", "ACCOUNT NAME"))
        self.password_label.setText(_translate("LogInWindow", "PASSWORD"))
        self.loginButton.setText(_translate("LogInWindow", "LOG IN"))
        self.createAccountButton.setText(_translate("LogInWindow", "CREATE ACCOUNT"))
        self.type_Button_yes.setText(_translate("LogInWindow", "YES"))
        self.type_Button_no.setText(_translate("LogInWindow", "NO"))
        self.create_account_type_label.setText(_translate("LogInWindow", "(Create Account) \nSavings Account?:"))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(499, 392))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transaction_history = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.transaction_history.setGeometry(QtCore.QRect(10, 0, 261, 351))
        self.transaction_history.setObjectName("transaction_history")
        self.account_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.account_name_label.setGeometry(QtCore.QRect(340, 10, 111, 31))
        self.account_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.account_name_label.setObjectName("account_name_label")
        self.log_out_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.log_out_button.setGeometry(QtCore.QRect(380, 320, 101, 41))
        self.log_out_button.setObjectName("next_account_button")
        self.deposit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deposit_button.setGeometry(QtCore.QRect(280, 80, 91, 41))
        self.deposit_button.setObjectName("deposit_button")
        self.withdraw_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.withdraw_button.setGeometry(QtCore.QRect(280, 130, 91, 41))
        self.withdraw_button.setObjectName("withdraw_button")
        self.deposit_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.deposit_amount.setGeometry(QtCore.QRect(380, 90, 113, 20))
        self.deposit_amount.setObjectName("deposit_amount")
        self.withdraw_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.withdraw_amount.setGeometry(QtCore.QRect(380, 140, 113, 20))
        self.withdraw_amount.setObjectName("withdraw_amount")
        self.account_type_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.account_type_label.setGeometry(QtCore.QRect(330, 50, 131, 21))
        self.account_type_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.account_type_label.setObjectName("account_type_label")
        self.interest_rate_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.interest_rate_label.setGeometry(QtCore.QRect(330, 220, 121, 41))
        self.interest_rate_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.interest_rate_label.setObjectName("interest_rate_label")
        self.interest_check_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.interest_check_label.setGeometry(QtCore.QRect(315, 265, 165, 51))
        self.interest_check_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.interest_check_label.setObjectName("interest_check_label")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(330, 180, 151, 41))
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accounts"))
        self.account_name_label.setText(_translate("MainWindow", ""))
        self.log_out_button.setText(_translate("MainWindow", "Log Out"))
        self.deposit_button.setText(_translate("MainWindow", "Deposit"))
        self.withdraw_button.setText(_translate("MainWindow", "Withdraw"))
        self.account_type_label.setText(_translate("MainWindow", ""))
        self.interest_rate_label.setText(_translate("MainWindow", ""))
        self.interest_check_label.setText(_translate("MainWindow", ""))
        self.error_label.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LogInWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
