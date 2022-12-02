import sys, re

with open("0__init__.py", "r") as file_input:
    with open("__init__.py", "w") as file_output: 
        for line in file_input:
            x = re.sub("$NAME", sys.argv[1], line)
            file_output.write(line)

""" txt = "The rain in Spain"
x = re.sub(sys.argv[1], txt)
print(x) """

