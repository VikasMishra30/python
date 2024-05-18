# Lists
# store multiple items in a single variable
# Lists are ordered collection of data items.
# Lists are changeable meaning we can alter them after creation.
# Lists = [value1, value2,...,valuen]

list1 = [1,2,2,3,5,4,6]
list3 = ["Red", 1, 0.1, True]
print(list1)
print(list3)


# List Index

colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
#          [0]      [1]     [2]      [3]      [4]

# Accessing list items

# Positive Indexing
print(colors[0])

# Negative Indexing
# print(colors[len(colors)-n])
# print(colors[-n])
print(colors[-1])

# Check whether an item in present in the list
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

# Range of Index
# You can print a range of list items
# specify start, end & skip

# listName[start : end : jumpIndex]

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# printing elements within a particular range
print(num[2:7])

# printing all element from a given index till the end
print(num[5:])
print(num[-2:])

# printing all elements from start to a given index
print(num[:5])

# Printing alternate values
print(num[::2])
print(num[2:7:3])


# List Comprehension
# List comprehensions are used for creating new lists 
# from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

square = [x*x for x in num]
print(square)