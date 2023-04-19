import webbrowser
# print(dir())
# print(dir(__builtins__))
# chrome = webbrowser.get(using='google-chrome')
# chrome.open_new('https://www.python.org')

webbrowser.get('chrome %s').open('https://wwww.python.org')


# def parabola(x):
#     y = x * x
#     return y

# for x in range(-100, 100):
#     y= parabola(x)
#     print(y)

string = "hello world"
substring = string[-2::-1]
print(substring)

original_string = "hello world"
reversed_string = ""

for char in original_string:
    reversed_string = char + reversed_string
print(reversed_string)