# task5.py

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by ${amount}. New salary: ${self.salary}")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}")

# Create an employee and give a raise
employee = Employee("marife", "Software Engineer", 80000)
employee.display_employee()
employee.give_raise(5000)
employee.display_employee()