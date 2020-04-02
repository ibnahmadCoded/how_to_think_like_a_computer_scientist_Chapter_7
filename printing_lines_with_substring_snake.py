def get_lines_snake(file_name):
    """prints lines with substring snake in a file"""
    with open(file_name, "r") as infile:
        for line in infile:
            if "snake" in line:
                print(line)
