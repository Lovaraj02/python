class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"My name is {self.name} and age is {self.age}")
obj = Student("Balu",21)
obj.display()