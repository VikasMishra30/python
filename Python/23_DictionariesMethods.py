thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1965
}

# Change Values
thisdict["year"] = 1964
thisdict.update({"year": 2020})

# Add Dictionary Items
thisdict["color"] = "red"
thisdict.update({"class": "Pony car"})

# Removing Items
thisdict.pop("year")
thisdict.popitem()      # removes the last inserted item
del thisdict["color"]   # del keyword can also delete the dictionary completely
# clear() method empties the dictionary

print(thisdict)

# Copy Dictionaries
mydict = thisdict.copy()
mydict2 = dict(thisdict)

# fromkeys()
# Create a dictionary with 3 keys, all with the value 0
x = ('key1', 'key2', 'key3')
y = ('value')
fromdict = dict.fromkeys(x, y)
print(fromdict)

# Loop Through a Dictionary

# Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

for x in thisdict.keys():
  print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

# Loop through both keys and values
for x, y in thisdict.items():
  print(x, y)

