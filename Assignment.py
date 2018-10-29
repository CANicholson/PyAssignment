def main(filename):
    """A function which takes a file filled with strings and finds the best acronym based upon scoring

    The lower the score the better the acronym. The acronyms are then stored in an output file"""
    if filename.endswith(".txt"):
        letterscores = valueassign()
        with open(filename, 'r') as filestrings, open("names_abbrevs.txt", 'w') as fileabrevs:
            fullstring = filestrings.readline()
            while(fullstring!=""):
                cleanedlist = cleaning(fullstring)
                scoredlist = scoring(cleanedlist, letterscores)
                print(cleanedlist)
                fullstring = filestrings.readline()
    else: 
        print("File is not a .txt. Please try again with a .txt file")

def cleaning(unclean):
    """Removes apostrophes, capitalizes and returns list of string"""
    fullstring = unclean.upper()
    capstring = fullstring.replace("'", "")
    stringlist = capstring.split()
    return stringlist

def scoring(cleanedlist, letterscores):
    """Iterate through characters and return a list of dictionaries.

    The key is the acronym and the value is the score"""
    acronDict = {}

    return ()

def valueassign():
    """Sets the values of each letter. Source of values is values.txt
    
    Placed in a function in case the user wishes to modify the value of letters."""
    with open("values.txt", "r") as letnumpair: 
        tempstore = letnumpair.readlines()
        tempo = [x.split() for x in tempstore]
        values = {y[0]:int(y[1]) for y in tempo}
        return(values)