choice = " "
while True:
    if choice == "0":
        break
    elif choice in "12345":
        print("you chose {}".format(choice))
    else:
        print("1:\tlearn python")
        print("2:\tleasrn java")
    choice = input()