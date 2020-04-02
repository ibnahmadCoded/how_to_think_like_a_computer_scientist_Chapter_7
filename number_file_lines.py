def number_file_lines(oldfile, newfile):
    """numbers file lines, starting with number one"""
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        count = 1 #initiate the count variable
        for line in infile:
            outfile.write("{0:<5}{1}".format(count, line))
            count += 1
    
