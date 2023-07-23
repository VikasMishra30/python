# for loop - iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

name = 'Vikas'
for i in name:
  print(i)
  if(i =="s"):
    print("Mishra")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  if color == "Blue":
    continue              
  print(color)
  for i in color:
    if color == "Green":
      break
    print(i)
  
# continue - stop the current iteration of the loop, and continue with the next

# break - stop the loop before it has looped through all the items

for k in range(3):
  print(k)
  
for k in range(1, 3):
  print(k)

for k in range(1, 8, 3):
  print(k)

for k in range(8, 1, -3):
  print(k)

# Nested For Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
  else:
    print("Finally finished!")

# else - specifies a block of code to be executed when the loop is finished
