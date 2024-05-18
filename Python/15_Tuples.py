# Tuples
# store multiple items in a single variable.
# Ordered
# Unchangeable
# Allow Duplicates

mytuple = ("apple", "banana", "cherry")

print(mytuple)
print(type(mytuple))
print(len(mytuple))

# Create Tuple With One Item
# add a comma after the item, otherwise Python will not recognize it as a tuple.
OneItem = ("apple",)
OneItem_no = ("apple")
print(OneItem, " - ", type(OneItem), "\n", OneItem_no, " - ", type(OneItem_no))

# tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Tuple Items
print(mytuple[-2])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5:1])

# Check for item
if "watermelon" in thistuple:
    print("watermelon is present.")
else:
    print("watermelon is absent.")