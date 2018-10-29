def main(filename):
    """A function which takes a file filled with strings and finds the best acronym based upon scoring

    The lower the score the better the acronym. The acronyms are then stored in an output file"""
    if filename.endswith(".txt"):
        with open(filename, 'r') as filestrings, open("names_abbrevs.txt", 'w') as fileabrevs:
            fullstring = filestrings.readline()
            while(fullstring!=""):
                fullstring = fullstring.upper()
                cleanedstring = fullstring.replace("'", "")
                print(cleanedstring)
                fullstring = filestrings.readline()
    else: 
        print("File is not a .txt. Please try again with a .txt file")