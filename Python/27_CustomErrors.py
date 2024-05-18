# Raise an exception
# you can choose to throw an exception if a condition occurs.

age = input("Enter age: ")
if not 0 < int(age) and not type(age) is int:
    raise ValueError("Not a valid age")


# Defining Custom Exceptions

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...