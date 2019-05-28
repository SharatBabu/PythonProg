#closure

def outer_func():
    x = 5
    def inner_func(y=3):
        return (x + y)
    return inner_func


a = outer_func()

print(a())

############################
print(" ")
############################


def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier


mult5 = multiplier_of(5)
print(mult5(9))

############################
print(" ")
############################


def print_msg(msg):
    def printer():
        print(msg)
    return printer

another = print_msg("Hello")
another()

############################
print(" ")
############################


def outerFunction(text):
    def innerFunction():
        print(text)
    innerFunction()

outerFunction('Hey!')

############################
print(" ")
############################


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print(times3(9))
print(times5(3))
