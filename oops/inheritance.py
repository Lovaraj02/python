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



# multilevel
class GrandMother:
    def property(self):
        print("Property from GrandMother")
class Mother(GrandMother):
    def skills(self):
        print("Cooking skills from Mother")
class Son(Mother):   # inherits both Mother & GrandMother
    def education(self):
        print("Education from Son")
obj = Son()
obj.property()
obj.skills()
obj.education()




#multiple
class Father:
    def driving(self):
        print("Driving skill from Father")

class Mother:
    def cooking(self):
        print("Cooking skill from Mother")

class Son(Father, Mother):   # Multiple inheritance
    def sports(self):
        print("Sports skill from Son")

obj = Son()
obj.driving()
obj.cooking()
obj.sports()
 

# hierarchical
class Parent:
    def property(self):
        print("House from Parent")

class Son(Parent):
    def job(self):
        print("Job skill from Son")

class Daughter(Parent):
    def singing(self):
        print("Singing talent from Daughter")

s = Son()
d = Daughter()
s.property()
s.job()
d.property()
d.singing()



# hybrid
class GrandParent:
    def wisdom(self):
        print("Wisdom from GrandParent")

class Father(GrandParent):
    def driving(self):
        print("Driving skill from Father")

class Mother(GrandParent):
    def cooking(self):
        print("Cooking skill from Mother")

class Son(Father, Mother):   # Hybrid inheritance
    def sports(self):
        print("Sports skill from Son")

obj = Son()
obj.wisdom()
obj.driving()
obj.cooking()
obj.sports()

