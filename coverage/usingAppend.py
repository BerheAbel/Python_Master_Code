curentChoice = " "
computerParts = []

while curentChoice != '0':
    if curentChoice in "1,2,3,6":
        print("adding {}".format(curentChoice))
        if curentChoice == '1':
            computerParts.append("computer")
        if curentChoice == "6":
            computerParts.append("monitro")
    else:
        print("please add options from the list below")
        print("1:\tcomputer")
        print("2:\tmonitor")
        print("3:\tmouse")
    curentChoice = input()
print(computerParts)