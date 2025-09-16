# Aquiring the properties from parent
class Mother:
    def __init__(self,color,blood):
        self.color = color
        self.blood = blood
    def disaplay(self):
        print("color from mother",self.color,self.blood)
class Son(Mother):
    def __init__(self,color,blood,height):
        super().__init__(color,blood)
        self.height = height
    def details(self):
        print("height is",self.height)
obj = Son("black","b +ve","5 feet")
obj.disaplay()
obj.details() 

















# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def details(self):
#         print(self.name,self.age)
# class student(person):
#     def __init__(self, name, age,gender):
#         super().__init__(name, age)
#         self.gender = gender
#     def gen(self):
#         print("name is :",self.name,"age is :",self.age,"gender is :",self.gender)
# obj = student("raju",21,"male") 
# obj.gen()


        
