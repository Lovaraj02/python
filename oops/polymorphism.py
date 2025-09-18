# compiletime polymorphism(Method over loading)
# overloading possible only with default args(*args)
lst = [1,2,3,4]
name = "raju"
print(len(lst))
print(len(name))    # same len() fun but works accordingly

class runtime:
    def add(self,*args):
        return sum(args)
obj = runtime()
print(obj.add(1,2,3,4))
print(obj.add(1,2,3,4,1,4,5,6))


# Runtime polymorphism(Method overriding)
class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

a = Animal()
a.sound()

d = Dog()
d.sound()   #when i call d.sound its overrides the sound() in Animal


