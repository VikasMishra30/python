# Lambda Functions
# a small anonymous function without a name
# lambda arguments: expression

x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
double = lambda x: x * 2

# Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y

# Lambda function to calculate the product of two numbers
product = lambda x, y: x * y

# Lambda function to calculate the product of two numbers,
# with additional print statement
printlambd = lambda x, y: print(f'{x} * {y} = {x * y}')


print("Double: ", double(x))
print("Product: ", product(x, y))
printlambd(x, y)