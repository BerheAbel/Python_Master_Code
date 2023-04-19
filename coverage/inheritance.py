# class employes:
#      raise_amt = 1.04

#      def __init__(self, first, last, pay):
#           self.first = first
#           self.last = last
#           self.pay = pay
#           self.email= first + last + "@gmail.com"
#           self.pay_by_first_name = last + first

#      def fullname(self):
#           return f'{self.first}{self.last}'
     
#      def apply_raise(self):
#           self.pay = int (self.pay * self.raise_amt)
#           return self.pay
     
#      def __str__(self):
#           return f"{self.apply_raise()} {self.fullname()}{self.first} {self.last} {self.email}"

# class developer(employes):
#      pass
# find = developer('corey','schafer',3000)
# find_1 = employes('corrr','nancy', 4000)

# print(find.pay)
# find.apply_raise()
# print(find_1.pay)
# # print(help(developer))

    
class abel:

    def __init__(self,age,name):
        self.age = age
        self.name = name
        self.employee_profile = str(age) + name

    def student_age(self):
        self.age = int (self.age)

    def __str__(self):
        return f"{self.age} {self.name} {self.employee_profile}"
    
student = abel(15, 'haile')


# print(student)

class berhe(abel):
    def __init__(self, age, name, amaziah):
        super().__init__(age, name)
        self.amaziah = amaziah

    def __str__(self):
        return super().__str__()

sub_calss = berhe(30, 'bella', 'cute')
print(sub_calss.amaziah)


