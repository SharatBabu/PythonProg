#decorators

def capitalize(func):
    def uppercase():
        result = func()
        return result.upper()

    return uppercase


@capitalize
def say_hello():
    return "hello"


print(say_hello())
########################
print(" ")
############################


def square(func):
  def multiply(*args):
    f = func(*args)
    return f * f
  return multiply

@square
def addition(x,y):
  return x + y

print(addition(5,7))
print(addition(15,10))

##########################