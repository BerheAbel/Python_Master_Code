class student:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

# creating an instance of the class
dog = student("labador", "boby",6)

print(dog.breed)
print(dog.name)

cat = student("mmommy","crispy",3)

print(cat.breed)
print(cat.name)


#         self.__name = name
# s1 = student("abel")
# # print(dir(s1))
# print(s1._student__name)

class account:

    def __init__(self, name, balance):
        self.name =name
        self.balance = balance
        print(f"Account created for " + self.name)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def show_balance(self):
        print(f"Balance is {self.balance}")

bella = account("roll", 4)
bella.deposit(1000)
bella.show_balance()
        