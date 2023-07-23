# Variables are containers for storing data values.
# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)


# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

x = 4       # x is of type int
x = "x was 4 before and type int but now of type str" # x is now of type str
print(x)


# If you want to specify the data type of a variable, this can be done with casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# You can get the data type of a variable with the type() function

print(type(x))
print(type(y))

# Many Values to Multiple Variables
x, y, z = "Many Values", "to", "Muliple Variables" 
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = "One Value to Multiple Variables"
print(x)
print(y)

# Unpack a Collection
fruits = ["Unpack", "a", "Collection"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variable
x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()

def myfunc2():
  x = "fantastic"
  print("Python is " + x)
myfunc2()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# String variables can be declared either by using single or double quotes
# Variable names are case-sensitive.

