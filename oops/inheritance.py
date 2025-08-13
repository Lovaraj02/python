class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def details(self):
        print(self.name,self.age)
class student(person):
    def __init__(self, name, age,gender):
        super().__init__(name, age)
        self.gender = gender
    def gen(self):
        print("name is :",self.name,"age is :",self.age,"gender is :",self.gender)
obj = student("raju",21,"male") 
obj.gen()


        
