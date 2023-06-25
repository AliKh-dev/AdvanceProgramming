class User:
    def __init__(self, name : str) -> None:
        self.name = name
    def identify(self):
        print(f"name: {self.name}")



class Master(User):
    def __init__(self, id, name : str) -> None:
        super().__init__(name)
        self.id = id

    def identify(self):
        print(f"ID: {self.id}, Name: {self.name}")



class Student(User):
    def __init__(self, student_number, name) -> None:
        super().__init__(name)
        self.student_number = student_number

    def identify(self):
        print(f"Student Number: {self.student_number}, Name: {self.name}")
