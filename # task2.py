# task2.py

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I study {self.course}.")

# Create three student objects
student1 = Student("Marife", 22, "ITV")
student2 = Student("Nacar", 22, "GE 111")
student3 = Student("Donna", 21, "English")

# Call the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()