def remove_numbering(oldfile, newfile):
    """removes numbering from a file"""
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            outfile.write(line[5:])
