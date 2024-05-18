class Math:
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3

# In this example, 
# the add method is a static method of the Math class. 
# It takes two parameters a and b and returns their sum. 
# The method can be called on the class itself, 
# without the need to create an instance of the class.