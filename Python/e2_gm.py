import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamph = time.strftime('%H')

timestampm = time.strftime('%M')

timestamps = time.strftime('%S')

# https://docs.python.org/3/library/time.html#time.strftime

g = int(timestamph)

if (0 < g < 4):
    print("Good Night")
elif (4 <= g < 12):
    print("Good Morning")
elif (12 <= g < 4):
    print("Good Afternoon")
else:
    print("Good Night")
