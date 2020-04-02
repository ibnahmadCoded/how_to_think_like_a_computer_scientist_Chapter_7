def write_in_leet(file_name):
    with open(file_name, "r") as infile:
        lines = infile.readlines()

        leet_letters = [("a", "4"), ("A", "4"), ("l", "1"),
                        ("L", "1"), ("i", "1"), ("I", "1"), ("e", "3"), ("E", "3")]

        line = lines[0]

        for letter, replacement in leet_letters:
            line = replacement.join(line.split(letter))
            

        print(line)
        
            
    
