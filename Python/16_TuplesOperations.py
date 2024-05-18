# Manipulating Tuples
# Tuples are immutable, 
# first convert the tuple to a list.
# Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
print(type(countries))
print(countries)

temp = list(countries)      # convert to list

temp.append("Russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item

countries = tuple(temp)     # convert back to tuple
print(countries)

# concatenate two tuples
countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
print(countries + countries1)

# Add tuple to a tuple 
countries += countries1
print(countries)

# Unpacking a Tuple
(yellow, white, orange, *green) = countries
print(orange)
print(green)

# Loop Tuples
for x in countries1:
  print(x)

# Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Tuple Methods
# count() - Returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position of where it was found

print(countries.count("India"))
print(countries.index("Russia"))