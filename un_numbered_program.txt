def reverse_doc(oldfile, newfile):
    """gets all lines in oldfile, reverses them in newfile"""
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        #get all lines in oldfile into a list.
        lines = infile.readlines()

        lines.append("\n")

        count = -1
        while (count * -1) <= len(lines):
            outfile.write(lines[count])
            count -= 1

        print(lines)

