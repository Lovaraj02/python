#Wrapping data and methods into a single unit (class) and restricting access using access modifiers, setters, and getters
class BankAccount:
    def __init__(self,balence):
        self.__balence = balence    #private variable
    def deposit(self,amount):       #setter
        self.__balence += amount
    def get_balence(self):          #getter
        return self.__balence
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balence())
