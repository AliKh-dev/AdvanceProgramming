# Matrix class
class Matrix:
    def __init__(self, matrix:list) -> None:
        if self.validate(matrix=matrix):
            self.columns = len(matrix[0])
            self.rows = len(matrix)
            self.matrix = matrix
        else:
            raise Exception


    def print_matrix(self):
        for row in self.matrix:
            for column in row:
                print(column, end=" ")
            print()


    def validate(self, matrix):
        self.columns = len(matrix[0])
        try:
            for row in matrix:
                if self.columns != len(row):
                    raise Exception
        except:
            return False
        return True


    def add(self, another_matrix):
        if self.rows != another_matrix.rows or self.columns != another_matrix.columns:
            print("This matrix is not compatible, Try again!")
            return
        result = [[0 for i in range(self.columns)] for j in range(self.rows)]
        for row in range(self.rows):
            for column in range(self.columns):
                result[row][column] = self.matrix[row][column] + another_matrix.matrix[row][column]
        return Matrix(result)


    def multiply(self, another_matrix):
        if self.columns == another_matrix.rows:
            result = [[0 for i in range(self.rows)] for j in range(another_matrix.columns)]
            for i in range(self.rows):
                for j in range(another_matrix.columns):
                    for k in range(another_matrix.rows):
                        result[i][j] += self.matrix[i][k] * another_matrix.matrix[k][j]
            return Matrix(result)
        print("This is not valid matrix!")
        return None

a = Matrix([[1,2],[3,4],[5,6]])
b = Matrix([[7,8],[9,10],[11,12]])
c = Matrix([[1,2,3],[4,5,6]])

a.print_matrix()
c.print_matrix()

print(a.add(b).matrix)
print(a.multiply(c).matrix)

print("--------------------------------------")
# --------------------------------------------------------------------------------


# Map
def power(entry1:int) -> int:
    return entry1 ** 2
list1 = [i for i in range(1,10)]
list_result = list(map(power, list1))
print(list_result)


# Filter
def greater_than_5(entry):
    if entry > 5:
        return True
    return False
list_result = list(filter(greater_than_5, list1))
print(list_result)


# Reduce
from functools import reduce
def multiply(entry1, entry2):
    return entry1 * entry2

def addition(entry1, entry2):
    return entry1 + entry2

result = reduce(multiply, list1)
print(result)
result = reduce(addition, list1)
print(result)


print("--------------------------------------")
# --------------------------------------------------------------------------------


# Abstract methods
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, model) -> None:
        self.model = model
    

    @abstractmethod
    def max_speed(self):
        pass


class Benz(Car):
    def __init__(self) -> None:
        super().__init__("Benz")


    def max_speed(self, speed):
        self.maximum_speed = speed


print("--------------------------------------")
# --------------------------------------------------------------------------------


# BankAccount
class BankAccount():
    def __init__(self, customer_id, customer_name, balance, date_of_opening):
        self.customer_id = customer_id
        self.customer_name = customer_name
        if balance < 0:
            raise Exception("This balance is not valid!")
        else:
            # balance is private field
            self.__balance = balance
        self.date_of_opening = date_of_opening


    def withdraw(self, amount_of_money):
        if amount_of_money > self.__balance:
            print("This operation can't be done beacuase you don't have enough money!")
            return
        self.__balance -= amount_of_money


    def deposit(self, amount_of_money):
        self.__balance += amount_of_money


    def check_balance(self):
        return self.__balance


print("--------------------------------------")
# --------------------------------------------------------------------------------


class Employee:
    def __init__(self, emp_id, emp_name, init_salary, department) -> None:
        self.id = emp_id
        self.name = emp_name
        # initial salary as private
        self.__initial_salary = init_salary
        self.assign_department(department)


    def __str__(self) -> str:
        return f"ID: {self.id}\nFull Name: {self.name}\nDepartment: {self.__department}"


    def calculate_emp_salary(self, hours_of_work:int):
        # set salary as private filed
        if hours_of_work > 50:
            self.__salary = self.__initial_salary + (hours_of_work - 50) * 12
        else:
            self.__salary = self.__initial_salary
        return self.__salary


    def check_salary(self) -> float:
        return self.__salary


    def calculate_tax(self, tax_rate) -> float:
        self.__amount_of_tax = self.__salary * tax_rate
        self.__salary -= self.__amount_of_tax
        return self.__amount_of_tax


    def assign_department(self, department) -> None:
        self.__department = department


    def change_department(self, new_department) -> None:
        self.__department = new_department


    def check_department(self) -> str:
        return self.__department



print("--------------------------------------")
# --------------------------------------------------------------------------------



