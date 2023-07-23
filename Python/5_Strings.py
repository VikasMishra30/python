# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

a = "Python Strings"

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''' # Multiline Strings

print(a)
print(b)

# Strings are Arrays

print(a[1])  # Get the character at position 1

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in a:
  print(x)

for c in "apple":
    print(c)

# String Length
print("The len() function returns the length of a string")
print(len(b))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

print("Lorem" in b)

if "Lorem" in b:
  print("Yes, 'Lorem' is present.")   # Use it in an if statement

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("Free" not in b)

if "Free" not in b:
  print("Yes, 'Lorem' is not present.")
 
# Slicing

print(b[2:5])  # including 2 but not 5
print(a[:3])   # print(a[:3])
print(b[2:])   # Slice to end
print(a[-5:-2])  #print(b[len(a)-5:len(a)-2])



# Strings are Arrays
# strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type,
# a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.