n = 10
def factorial():
    if n <= 1:
        return 1
    else:
        return n * factorial()

print(factorial())

