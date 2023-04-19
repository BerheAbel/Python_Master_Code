options = input("Put yor faberite fruit: ")
fruits = "apple"
for x in range(3):
    if options == fruits:
        print(fruits)
        break 
    else: 
        input("Please select form the options: ")

for x in range (5):
    for y in range(3):
        print(f"{x},{y}")    

for x in "python":
    print(x)
    break

shopping_cart = ['fruits','bread','milk','egg'] 
print(shopping_cart[0])
for item in shopping_cart:
    for index in item:
        print(index)
        break
    print(shopping_cart[0])
    break

count = 0
for x in range(1,10):
    if x%2 == False:
        count += 1
        print(x)
print("we have {} even numbers!!!".format(count))
    
lis_fruits = ['mango','orange','banana','watermelon']
for items in lis_fruits:
    for room in items:
        print(room,end='')
    print()


color = ["red",'yellow','black']  
flours =['unbleached','bleached','pure']
for x in color:
    for y in flours:
        print(x,y)    

for dots in range(0,8):
    for colomns in range(dots+1):
        print("*", end=' ') 
    print()
start = 0
def sum_eo(n,t):
    """
    Switching the value of t in different instance then return sum_eo
    """
    if t == 'e':
        start == 2
    elif t == 'o':
        start == 1
    else:
        return -1
    return sum(range(start, n, 2))
x = sum_eo(11, "spam")
print(x)
        
    
    

    



    
