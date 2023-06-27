class Parent():
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def print_out(self):
        print(f"att1: {self.attr1}, attr2: {self.attr2}")

class Child(Parent):
    def set_type(self, entry):
        self.child_type = entry

    def get_type(self):
        print(self.child_type)

class Parent2:
    def type_hint(self):
        print(f"type is: {self.type}")

class Child2(Parent, Parent2):
    def set_type(self, entry):
        self.type = entry


parent_obj = Parent("data1", "data2")
child_obj = Child("data3","data4")
child_obj.set_type(12)
child_obj.get_type()
