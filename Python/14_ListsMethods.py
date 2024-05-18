# List Methods

l = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# sort()

# list.sort(reverse=True|False, key=myFunc)

l.sort()
print(l)

# sort-reverse
l.sort(reverse=True)
print(l)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

# reverse() - reverses the order of the list.
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
num.reverse()
print(num)

# index() - returns the index of the first occurrence
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(5))

# count() - Returns the count of the number of items with the given value.
print(num.count(2))

# copy() - Returns copy of the list
newList = num.copy()
print(newList)

# append() - appends items to the end of the existing list.
newList.append(0)
print(newList)
newList.append(l)
print(newList)

# insert() - inserts an item at the given index
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)

# extend() - adds an entire list or any other collection datatype to the existing list.
l.extend(colors)
print(l)

# Concatenating two lists
print(num + colors)

# clear()
l.clear()
print(l)

# remove() - Removes the first item with the specified value
colors.remove("green")
print(colors)

# pop() - Removes the element at the specified position
colors.pop(1)
print(colors)