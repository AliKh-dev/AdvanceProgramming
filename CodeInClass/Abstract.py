from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, shape_type) -> None:
        self.shape_type = shape_type
    @abstractmethod
    def area(self):
        pass
    def set_color(self, color):
        self.color = color


class Square(Shape):
    def __init__(self, size) -> None:
        self.size = size
        super().__init__("Square")
    def area(self):
        return self.size ** 2
    





# Practice

class Motor(ABC):
    def __init__(self, type) -> None:
        self.type = type
    @abstractmethod
    def charge(self):
        pass
    def decharge(self):
        pass

class Motor1(Motor):
    def __init__(self) -> None:
        self.charge_percentage = 100
        super().__init__("motor1")
    def charge(self):
        self.charge_percentage = 50
    def decharge(self):
        self.charge_percentage -= 2

class Motor2(Motor):
    def __init__(self) -> None:
        self.charge_percentage = 100
        super().__init__("motor2")
    def charge(self):
        self.charge_percentage = 100
    def decharge(self):
        self.charge_percentage -= 1
