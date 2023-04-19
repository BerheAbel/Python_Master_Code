import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

with open('/home/aberhe/pythonMasterClass/coverage/data/languages.txt', 'r', encoding="UTF-8") as loader:
    data = json.load(loader)

print(data)