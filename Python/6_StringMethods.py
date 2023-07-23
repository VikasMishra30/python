# Strings are immutable

a = "!!!Vikas!! !!!!!!!!! VIKAS"

print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Vikas", "Mishra"))
print(a.split(" "))
blogHeading = "introduction tO PYthon"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Vikas"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

# capitalize()
# Converts the first character to upper case

# casefold()	
# Converts string into lower case

# center()	
# Returns a centered string

# count()	
# Returns the number of times a specified value occurs in a string

# encode()	
# Returns an encoded version of the string

# endswith()	
# Returns true if the string ends with the specified value

# expandtabs()	
# Sets the tab size of the string

# find()	
# Searches the string for a specified value and returns the position of where it was found

# format()	
# Formats specified values in a string

# format_map()	
# Formats specified values in a string

# index()	
# Searches the string for a specified value and returns the position of where it was found

# isalnum()	
# Returns True if all characters in the string are alphanumeric

# isalpha()	
# Returns True if all characters in the string are in the alphabet

# isdecimal()	
# Returns True if all characters in the string are decimals

# isdigit()	
# Returns True if all characters in the string are digits

# isidentifier()	
# Returns True if the string is an identifier

# islower()	
# Returns True if all characters in the string are lower case

# isnumeric()	
# Returns True if all characters in the string are numeric

# isprintable()	
# Returns True if all characters in the string are printable

# isspace()
# Returns True if all characters in the string are whitespaces

# istitle()	
# Returns True if the string follows the rules of a title

# isupper()	
# Returns True if all characters in the string are upper case

# join()	
# Joins the elements of an iterable to the end of the string

# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string

# maketrans()	
# Returns a translation table to be used in translations

# partition()	
# Returns a tuple where the string is parted into three parts

# replace()	
# Returns a string where a specified value is replaced with a specified value

# rfind()	
# Searches the string for a specified value and returns the last position of where it was found

# rindex()	
# Searches the string for a specified value and returns the last position of where it was found

# rjust()	
# Returns a right justified version of the string

# rpartition()	
# Returns a tuple where the string is parted into three parts

# rsplit()	
# Splits the string at the specified separator, and returns a list

# rstrip()	
# Returns a right trim version of the string

# split()	
# Splits the string at the specified separator, and returns a list

# splitlines()	
# Splits the string at line breaks and returns a list

# startswith()	
# Returns true if the string starts with the specified value

# strip()	
# Returns a trimmed version of the string

# swapcase()	
# Swaps cases, lower case becomes upper case and vice versa

# title()	
# Converts the first character of each word to upper case

# translate()	
# Returns a translated string

# upper()	
# Converts a string into upper case

# zfill()	
# Fills the string with a specified number of 0 values at the beginning