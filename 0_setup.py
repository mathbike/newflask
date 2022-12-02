import sys, re

with open("0__init__.py", "r") as file_input:
    with open("__init__.py", "w") as file_output: 
        for line in file_input:
            if line.lstrip().startswith('#'):
                continue
            file_output.write(line)
