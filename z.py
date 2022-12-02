with open("__init__.py", "r") as file_input:
    with open("file_output.py", "w") as file_output: 
        for line in file_input:
            if line.lstrip().startswith('#'):
                continue
            if line.lstrip().startswith('print'):
                continue
            file_output.write(line)