class BankAccount:
	def __init__(self, account_number, balance, date_of_opening, customer_name):
		self.account_number = account_number
		if balance <= 0:
			self.balance = 0
		else:
			self.balance = balance
		self.date_of_opening = date_of_opening
		self.customer_name = customer_name

	def deposit(self, deposit_amount):
		self.balance += deposit_amount

	def withdraw(self, withdraw_amount):
		if self.balance - withdraw_amount < 0:
			print("Don't have enough money!")
			return
		self.balance -= withdraw_amount


	def check_balance(self):
		return self.balance
