# The readline() method reads a single line from the file. 
# If we want to read multiple lines, we can use a loop.

f = open('myfile.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)


# The writelines() method in Python writes a sequence of strings to a file. 
# The sequence can be any iterable object, such as a list or a tuple.

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()


# The seek() function allows you to 
# move the current position within a file to a specific point. 
# The position is specified in bytes, 
# and you can move either forward or backward from the current position

with open('myfile.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)

  print(data)


# The tell() function returns the current position within the file, in bytes. 
# This can be useful for keeping track of your location within the file 
# or for seeking to a specific position relative to the current position.

with open('myfile.txt', 'r') as f:
  data = f.read(10) # Read the first 10 bytes

  # Save the current position
  current_position = f.tell()
  
  print(current_position)


# with open('myfile.txt', 'w') as f:
#   f.truncate(5)
# with open('myfile.txt', 'r') as f:
#   print(f.read())