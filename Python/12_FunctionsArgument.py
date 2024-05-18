# Default Arguments
# assumes a default value even if a value is not provided

def default(a = "Default", b = "Arguments"):
    print("Hello,", a, b)
default()
default("hii")


# Keyword arguments:
# We can provide arguments with key = value,
# this way the interpreter recognizes the arguments by the parameter name

def keyword(a, b):
    print("Hello,", a, b)
keyword(a = "Keyword", b = "Argument")


# Required Arguments
# In case we don’t pass the arguments with a key = value syntax, 
# then it is necessary to pass the arguments in the correct positional order 
# and the number of arguments passed should match with actual function definition.

def required(a, b):
    print("Hello,", a, b)
required("Required", "Arguments")


# Variable-length arguments
# pass more arguments than those defined in the actual function
# two ways -

# Arbitrary Arguments:
# pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of tuple.

def arbitrary(*a):
    print("Hello,", a[0], a[1], a[1])
arbitrary("Variable-length", "Arbitrary", "Argument")

# Keyword Arbitrary Arguments
# pass a ** before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of dictionary.

def keywordarbitrary(**a):
    print("Hello,", a["b"], a["c"], a["d"])
keywordarbitrary(b="Keyword", c="Arbitrary", d="Argument")


# return Statement
# return the value of the expression back to the calling function.

def ret(a, b):
    return "Hello, " + a + " " + b
print(ret("Return", "Statement"))