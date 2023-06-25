class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        self.area = self.calculate_area()
    def get_area(self):
        return self.area 
    def calculate_area(self):
        self.length * self.width


class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length=length, width=self.length)

