fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)

# The enumerate function allows you to loop over a sequence (such as a list, tuple, or string) 
# and get the index and value of each element in the sequence at the same time.

# By default, the enumerate function starts the index at 0, 
# but you can specify a different starting index by passing 
# it as an argument to the enumerate function