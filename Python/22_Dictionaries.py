# Dictionaries
# store data values in key:value pairs
# ordered, changeable and do not allow duplicates

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1965 # Duplicate values will overwrite existing values
}

print(thisdict)
print(type(thisdict))
print(len(thisdict))

# Accessing Dictionary items

# Accessing single values
print(thisdict['brand'])
print(thisdict.get('model'))

# Accessing multiple values
print(thisdict.values())

# Accessing keys
print(thisdict.keys())

# Accessing key-value pairs
print(thisdict.items())