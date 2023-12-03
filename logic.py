import csv
from PyQt6.QtWidgets import *
from gui import *
import sys


class LoginLogic(QMainWindow, Ui_LogInWindow):
    """
    Class to display UI of accounts.csv and it's information
    """
    INTEREST_RATE = 0.02

    def __init__(self):
        """
        Method to initialize and display the login window
        :return:
        """
        super().__init__()
        self.setup_login_Ui(self)
        self.username = self.username_input
        self.password = self.password_input
        self.account_type = ''
        self.type_Button_no.setChecked(True)

        self.loginButton.clicked.connect(lambda: self.login_verify())
        self.createAccountButton.clicked.connect(lambda: self.create_account())

    def login_verify(self):
        """
        Method to verify username and password before opening the main window
        :return:
        """
        username = str(self.username_input.text())
        password = str(self.password_input.text())

        with open("accounts.csv", "r") as csvfile:
            content = csv.reader(csvfile)
            for line in content:
                try:
                    if (line[0] == username) and (line[1] == password):
                        self.account_line = line
                        self.display_main()
                        break
                    elif line[0] != username:
                        self.error_message.setText("Incorrect username or password")
                except IndexError:
                    pass

    def create_account(self):
        """
        Method to create a new account and write to accounts.csv
        :return:
        """
        username = self.username_input.text()
        password = self.password_input.text()
        if (username == '') or (password == ''):
            self.error_message.setText('Account must have \nusername and password')
            return

        if self.type_Button_yes.isChecked():
            self.account_type = 'savings'
            self.initial_balance = 100
            self.num_deposits = 0
            self.account_info = [username, password, self.account_type, self.initial_balance, self.num_deposits]
        else:
            self.account_type = 'standard'
            self.initial_balance = 0
            self.account_info = [username, password, self.account_type, self.initial_balance]
        self.account_line = self.account_info
        with open("accounts.csv", "a", newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(self.account_info)
            self.display_main()

    def get_line(self):
        """
        Method to quickly access a set csv line in accounts
        :return: csv line with account information
        """
        return self.account_line

    def get_username(self):
        """
        Method to quickly access account's username
        :return: account username
        """
        return self.username

    def get_password(self):
        """
        Method to quickly access account's password
        :return: account password
        """
        return self.password

    def display_main(self):
        """
        Method to set up and display main window of the program
        :return:
        """

        self.setupUi(self)

        self.account_name_label.setText(f"{self.get_username().text()}'s Account")
        self.transaction_history.append(f'Current balance: ${self.calculate_balance():.2f}')
        self.display_interest()
        self.deposit_button.clicked.connect(lambda: self.deposit(float(self.deposit_amount.text())))
        self.withdraw_button.clicked.connect(lambda: self.withdraw(float(self.withdraw_amount.text())))
        self.log_out_button.clicked.connect(lambda: self.close())

    def display_interest(self):
        """
        Method to display interest information for savings accounts
        :return:
        """
        self.__account_info = self.get_line()
        if self.__account_info[2] == 'savings':
            self.interest_rate_label.setText(f'Current Interest Rate: \n{self.INTEREST_RATE}%')

    def deposit(self, amount: float):
        """
        Method to deposit amount into account's balance
        :param amount: amount to be deposited into account
        :return:
        """
        self.__account_info = self.get_line()
        try:
            if float(amount) <= 0: #check for negative or 0 deposits
                raise ValueError
            elif type(amount) == float or type(amount) == int: #check for type of input
                self.__account_info.append(str(amount))

                self.deposit_amount.setText('')
                self.transaction_history.append(f'Account balance is now: ${self.calculate_balance():.2f}')
                if self.__account_info[2] == 'savings':
                    self.__account_info[4] = int(self.__account_info[4]) + 1
                    if float(self.__account_info[4]) % 5 == 0:
                        self.balance_after_interest = self.calculate_interest()
                        self.interest_check_label.setText(f'Number of deposits made: {self.__account_info[4]} \n(5 required for interest to apply)')
                        self.transaction_history.append(f'Account balance after interest: ${self.balance_after_interest:.2f}')
                        self.__account_info[4] = 0

                    else:
                        self.interest_check_label.setText(f'Number of deposits made: {self.__account_info[4]} \n(5 required for interest to apply)')

        except ValueError:
            self.error_label.setText('Deposits cannot be \nnegative or zero')
            pass

    def withdraw(self, amount: float):
        """
        Method to withdraw amount from account balance
        :param amount: amount to be withdrawn from account
        :return:
        """

        self.__account_info = self.get_line()
        try:

            if float(amount) <= 0:
                raise ValueError
            elif (self.__account_info[2] == 'savings') and (self.calculate_balance() - float(amount) < 100):
                self.error_label.setText('Savings account balance \ncannot go below $100')
            elif (self.__account_info[2] == 'standard') and (self.calculate_balance() - float(amount) < 0):
                self.error_label.setText('Standard account balance \ncannot go below $0')
            elif type(amount) == float or type(amount) == int:
                self.__account_info.append(str(-amount))

                self.transaction_history.append(f'Account balance is now: ${self.calculate_balance():.2f}')
                self.withdraw_amount.setText('') #Reset edit line and label
                self.error_label.setText('')

            else: raise ValueError
        except ValueError:
            self.error_label.setText('Withdraw cannot be \nnegative or zero')

    def calculate_balance(self):
        """
        Method to calculate account's current balance
        :return: sum of account transactions
        """
        self.account = self.get_line()
        sum = float(self.account[3])
        for num in self.account[4:]:
            sum += float(num)
        return sum

    def calculate_interest(self):
        """
        Method to add interest to saving account's balance
        :return: account balance with applied interest
        """
        return self.calculate_balance() * (self.INTEREST_RATE + 1)

    def close(self):
        """
        Method to close program
        :return:
        """
        sys.exit()
