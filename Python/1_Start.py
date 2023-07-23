
print("Hello World!\n\nThis new line is posible because of \\n")
print("Python\'s Escape Character") #Single Quote using \'
print('\' in a string is an illegal character to insert illegal character use an escape character i.e. \\ followed by character\n\n')
print("Octal value\nA backslash followed by three integers will result in a octal value")
print("\110\145\154\154\157") #Hello
print("\nPrint", "more than one object\n")
x=("Print", "a", "tuple")
print(x,"\n")
print("Print two messages,", "and specify the separator", sep="---")
print("Print what to", "print at the end", end="END")

#Comment
"""
A comment is a part of the coding file
that the programmer does not want to execute,
rather the programmer uses it to either explain
a block of code or to avoid the execution of a
specific part of code while testing.
"""

# Escape Characters
"""
- To insert characters that are illegal in a string,
  use an escape character.
- An escape character is a backslash \ 
  followed by the character you want to insert.
- An example of an illegal character is a double quote
  inside a string that is surrounded by double quotes
"""
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# Print Statement
# Python print() function
# Parameters
"""
object(s)
Any object, and as many as you like. Will be converted to string before printed

sep='separator'
Specify how to separate the objects, if there is more than one. Default is ' '

end='end'
Specify what to print at the end. Default is '\n' (line feed)

file
An object with a write method. Default is sys.stdout

flush
A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
"""