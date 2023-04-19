with open("/home/aberhe/pythonMasterClass/coverage/data/Jabberwocky.txt") as poem:
    first = poem.readline().rstrip()
    print(first)

chars = "'Twas"
# second = first.strip(chars)
# print(second)

for charcter in first:
    if charcter in chars:
     print(charcter)


twas_removing = first.removeprefix("'Twas")
toves_removing = first.removesuffix("toves")

print(twas_removing)
print(toves_removing)
