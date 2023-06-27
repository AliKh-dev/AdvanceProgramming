class Inventory:
    def __init__(self, item_id, item_name, stock_count, price) -> None:
        self.item_details = dict()
        self.item_details[item_id] = {"name": item_name, "stock count" : stock_count, "price" : price}

    def add_item(self, item_id, item_name, price, stock_count=None):
        if self.item_details.get(item_id) == None:
            self.item_details[item_id] = {
                "name": item_name, "stock count": stock_count, "price": price}
        else:
            self.item_details[item_id]["stock count"] += 1
    def update_item(self, item_id, new_name, new_count_stock, new_price):
        self.item_details[item_id] = {
            "name": new_name, "stock count": new_count_stock, "price": new_price}
    def check_item_details(self):
        print(self.item_details)

inventory1 = Inventory(1001, "Speakers", 800, 560)
inventory1.add_item(1002, "Laptop", 760, 1560)
inventory1.add_item(1001, "Speakers", 560)
inventory1.update_item(1002, "LaptopLenovo", 90, 1290)
inventory1.check_item_details()

