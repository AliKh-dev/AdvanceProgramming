class Restaurant:
	def __init__(self, menu_items: list = list(), book_table: list = dict(), customer_orders: dict = dict()):
		self.menu_items = menu_items
		self.book_table = book_table
		self.customer_orders = customer_orders

	def add_item_to_menu(self, item, price):
		self.menu_items.append((item, price))

	def book_tables(self, customer_id, table_number):
		if self.book_table.get(table_number) is None:
			self.book_table[table_number] = customer_id
		else:
			print(f"This table is already reserved by customer id:{self.book_table[table_number]}!")

	def customer_order(self, customer_id, orders: list):
		orders_with_count = dict()
		for order in orders:
			if orders_with_count.get(order) is None:
				orders_with_count[order] = 1
			else:
				orders_with_count[order] += 1

		if self.customer_orders.get(customer_id, 1):
			self.customer_orders[customer_id] = orders_with_count
		else:
			self.customer_orders[customer_id].append(orders_with_count)

	def get_menu(self):
		print("-----Items in menu-----")
		for item in self.menu_items:
			print(f"Item {item[0]} with price {item[1]}")

	def get_table_reservation(self):
		print("-----Tables reserved-----")
		for table_number, customer_id in self.book_table.items():
			print(f"Table {table_number} reserved by {customer_id}")


	def get_customer_orders(self):
		print("-----Customer orders-----")
		for customer_id, orders in self.customer_orders.items():
			print(f"Customer id: {customer_id}", end="\t")
			for order, count in orders.items():
				print(f"Order:{order}\tCount:{count}")


restaurant = Restaurant()
restaurant.add_item_to_menu("Pizza", 1440000)
restaurant.add_item_to_menu("Sandwitch", 82500)
restaurant.add_item_to_menu("Salad", 43500)
restaurant.book_tables(1, 9)
restaurant.book_tables(2, 6)
restaurant.customer_order(1, ["Pizza", "Salad"])
restaurant.customer_order(2, ["Sandwitch"])
restaurant.get_menu()
print()
restaurant.get_table_reservation()
print()
restaurant.get_customer_orders()
print()
restaurant.book_tables(3, 9)
print()
restaurant.get_table_reservation()


