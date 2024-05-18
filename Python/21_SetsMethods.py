thisset = {"apple", "banana", "cherry"}


# Add Items - add one item to a set
thisset.add("orange")   # .add()
print(thisset)

# Add Sets - add items from another set into the current set
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # .update()
print(thisset)

# Add Any Iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# Remove Item

# remove()
thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error.

# discard()
thisset.discard("banana")
print(thisset)
# If the item to discard does not exist, discard() will not raise an error.

# pop() - remove a random item
x = thisset.pop()
print(x)
print(thisset)

# clear() - empties the set
tropical.clear()
print(tropical)

# del - delete the set completely
del tropical


# Join Sets

# union() - returns a new set containing all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# update() - inserts all the items from one set into another
set4 = {"a", "b" , "c"}
set4.update(set2)
print(set4)


# Keep ONLY the Duplicates

# intersection() - return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# intersection_update() - keep only the items that are present in both sets.
x.intersection_update(y)
print(x)


# Keep All, But NOT the Duplicates

# symmetric_difference() - return a new set, 
# that contains only the elements that are NOT present in both sets
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
sd = x1.symmetric_difference(y1)
print(sd)

# symmetric_difference_update() - keep only the elements that are NOT present in both sets.


# # isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	    Returns whether another set contains this set or not
# issuperset()	    Returns whether this set contains another set or not