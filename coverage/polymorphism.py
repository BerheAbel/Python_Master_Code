class french:
    def say_hello(self):
        print('BNJOUR')

class chinisse:
    def say_hello(self):
        print('ni hao')


def intro(lamg):
    lamg.say_hello()


john = chinisse()
intro(john)

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None):
        if a != None and b !=None:
         s=a+b
        else:
            s=a
        return s
    
s1 = student(10,36)
print(s1.sum())


