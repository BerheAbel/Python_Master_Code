def func(p1, p2, *args, k, **kwargs):
    print("positional or keyword....{} {}".format(p1,p2))
    print("var positional......{}".format(args))
    print("keyword....{}".format(k))
    print("var-keyword...{}".format(kwargs))
func(6,6,k=7,key1=7,key2=8,key=9)


def add(a,b):
    c = a*b
    return c

print(add(4,9))

# positional arguments -- called by their position
def person(*name: str):
    print(name)


person('heloo',12)

# keyword argument
def person2(name,age=10):
    print(name)
    print(age)

person2("hello",32)

def sum_number(*valuse: int) -> int:
    """
    calulating mutiple numbers with single argument called star argument
    """
    # return valuse
    result = 0
    for numbers in valuse:
        result += numbers
    return result

print(sum_number(1,3))
person("hi",30)
