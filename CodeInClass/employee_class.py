class Employee:
    def __init__(self, employee_id, employee_name, salary, department) -> None:
        self.id = employee_id
        self.name = employee_name
        self.salary = salary
        self.department = department
        self.calculate_tax()


    def __str__(self) -> str:
        return f"ID: {self.id}\nName: {self.name}\nTax: {self.tax}"


    def changeDepartment(self, new_department) -> None:
        self.department = new_department
        print("Department change!")


    def calculate_tax(self) -> float:
        if self.salary >= 10000:
            self.tax = self.salary * 0.3
            return self.tax
        elif 10000> self.salary >= 5000:
            self.tax = self.salary * 0.2
            return self.tax
        else:
            self.tax = self.salary * 0.1
            return self.tax
    




employee1 = Employee(1, "Ali Khadempour", 10000, "Software")
print(employee1)