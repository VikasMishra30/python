# Type Casting

# Python program to demonstrate implicit type Casting

a = 7        # Python automatically converts a to int
print(type(a))
 
b = 3.0      # Python automatically converts b to float
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
 
# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

# Python program to demonstrate Explicit Type Casting

# int variable
a = 5
 
# typecast to float
n = float(a)
 
print(n)
print(type(n))

# Type Casting is the method to convert the variable data type into a certain data type 
# in order to the operation required to be performed by users. 

# There can be two types of Type Casting in Python –

# Implicit Type Casting
# Explicit Type Casting

# Implicit Type Conversion
# Python converts data type into another data type automatically.
# In this process, users don’t have to involve in this process.

# Explicit Type Casting
# Python need user involvement to convert the variable data type into certain data type 
# in order to the operation required.
# Mainly in type casting can be done with these data type function:
# Int() : Int() function take float or string as an argument and return int type object.
# float() : float() function take int or string as an argument and return float type object.
# str() : str() function take float or int as an argument and return string type object.