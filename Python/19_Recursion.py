# Recursion
# Recursion is the process of defining something in terms of itself.

# recursive functions call itself

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
    
def fibonnaci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)
  
# Driver Code 
num = int(input("Enter Number: "))

print("Factorial:",factorial(num))

print(f"Fibonnaci of {num} is {fibonnaci(num)}")