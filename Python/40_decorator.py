# Decorators
# modify the behavior of functions and methods. 
# They are a way to extend the functionality of a 
# function or method without modifying its source code.

# @decorator_function
# def my_function():
#     pass

# def my_function():
#     pass
# my_function = decorator_function(my_function)



def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)









import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(10,20)