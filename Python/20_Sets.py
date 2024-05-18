# Sets
# store multiple items in a single variable.
# unordered, unchangeable, and do not allow duplicate values.

set1 = {"abc", 34, True, 40, "male", 1, 0, False, "Hello", 30, 30}

print(set1)
# Sets cannot have two items with the same value.
# The values True and 1 are considered the same value in sets
# The values False and 0 are considered the same value in sets
# Sets are unordered, so you cannot be sure in which order the items will appear.

print(type(set1))

print(len(set1))

# Accessing set items:

for a in set1:
    print(a)

# set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Set items are unchangeable, 
# but you can remove items and add new items.