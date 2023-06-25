class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department) -> None:
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def calculate_emp_salary(self, hours_work: int) -> None:
        if hours_work > 50:
            overtime = hours_work - 50
            amount_overtime = (overtime * (self.emp_salary / 50))
            return self.emp_salary + amount_overtime
        else:
            return self.emp_salary
    def assign_department(self, new_department :str) -> None:
        self.emp_department = new_department
    def print_employee_details(self):
        details = f"ID: {self.emp_id}\nName: {self.emp_name}\nSalary: {self.emp_salary}\nDepartment: {self.emp_department}"
        print(details)


emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERSTION")

print(emp1.calculate_emp_salary(20))
print(emp2.calculate_emp_salary(100))
print(emp3.calculate_emp_salary(300))
print(emp4.calculate_emp_salary(80))

emp4.print_employee_details()