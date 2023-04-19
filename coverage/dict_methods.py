d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon','cabbage'] 

# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

# p = new_dict.keys()
# print(p)

# code for 'update' method
# d2 = {
#     1 : "great num",
#     5 : "odd number",
#     9 : "finish your gusses"
# }

# d.update(d2)
# for key, value in d.items():
#     print(key, value)

# print()

# y =d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

values =list(d.values())
keys = list(d.keys())

if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(key)
my_dict = {}

for i, items in enumerate(pantry_items):
    my_dict[items] = i
print(my_dict)

# yup = my_dict
# for key, value in yup.items:
#         print(f"{key}{value}")










# value_dict = ""

# while True:
#     # create = bug[v]
#     if value_dict == "0":
#         break
#     if value_dict in v:
#         print(" appear in  this list")
    
#     else:
#         print("not in this dict")
#     value_dict = input(": ")


