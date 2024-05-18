import os

# Open the file in read-only mode
f = os.open("ostxt.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

print(contents)

# Close the file
os.close(f)

# Open the file in write-only mode
f = os.open("ostxt.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

os.close(f)

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)

# Create a new directory
# os.mkdir("newdir")

# Run the command and print the output

print(os.system("python --version"))

# Run the "ls" command and get the output as a file-like object
p = os.popen("python --version")

output = p.read()
print(output)
p.close()


