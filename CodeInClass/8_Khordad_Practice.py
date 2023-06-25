class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        if balance <= 0:
            self.__balance = 0
        else:
            self.__balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def set_balance(self, balance):
        self.__balance = balance * 100


    def get_balance(self):
        print(f"Account balance: {self.__balance}")

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.__balance - withdraw_amount < 0:
            print("Don't have enough money!")
            return
        self.__balance -= withdraw_amount

    def check_balance(self):
        return self.balance
