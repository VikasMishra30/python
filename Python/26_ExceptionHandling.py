try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print(num**3)
finally:
    print("Exception Handling :)")
   

# Exception Handling
# When an error occurs, or exception as we call it,
# Python will normally stop and generate an error message.
# Exception handling is the process of responding 
# to unwanted or unexpected events when a computer program runs. 
# Exception handling deals with these events to avoid the program 
# or system crashing, and without this process, 
# exceptions would disrupt the normal operation of a program.

# try...except
# handle errors and exceptions

# try:
#      # statements which could generate exception
# except:
#      # Solution of generated exception
# else:
#      # execute when no error
# finally:
#      # block of code which is going to execute in any situation

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.