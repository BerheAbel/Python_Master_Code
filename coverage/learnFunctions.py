def palianderm_sentense(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()

word = input("please enter a word to check: ")
if palianderm_sentense(word):
    print("'{}'is a paliandrome".format(word))
else:
    print("'{}'is not paliandrem".format(word))
