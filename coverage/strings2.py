
parrot = "abcdefghijklmnopqrstuvwxyz"
backwards = parrot[25:17:-1]
print(backwards)

print("There are {0} days in {1},{2},{3}".format(20,"jan","feb","mar"))

"""
jan {2}
feb {0}
mar {2}
apr {1}
may {2}"""

for i in range(1,13):
    print("hello")
age =24
print("my age is %d years" %age)

days = "mon,tus,wen,tur"
print(days[::3])
data = f"""1:a 2:b 3:c 4:d 5:e"""
print(data[-1:5])

flower = "blue violet"

print('blue'in flower)