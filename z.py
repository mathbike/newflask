import sys

# Read in the file
with open('__init__.py', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('$NAME', sys.argv[1])

# Write the file out again
with open('__init__.py', 'w') as file:
    file.write(filedata)
