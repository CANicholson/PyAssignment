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

import re

def cleaning(unclean):
    """Removes apostrophes and non-alphanumeric characters, capitalizes and returns list of string"""
    fullstring = unclean.upper()
    capstring = fullstring.replace("'", "")
    stripnanchar = re.compile('[^0-9a-zA-Z]+')
    cleanedstring = stripnanchar.sub(' ', capstring)
    stringlist = cleanedstring.split()
    return stringlist

def scoring(cleanedlist, letterscores):
    """Iterate through characters and return a list of dictionaries.

    The key is the acronym and the value is the score"""
    firstletter = cleanedlist[0]
    for x in cleanedlist:
        for i in range(len(x)):
            if i == 0 and cleanedlist.index(x) == 0:
                pass
            else:
                print("true")
    acronDict = {}
    return (acronDict)

def valueassign():
    """Sets the values of each letter. Source of values is values.txt
    
    Placed in a function in case the user wishes to modify the value of letters."""
    with open("values.txt", "r") as letnumpair: 
        tempstore = letnumpair.readlines()
        tempo = [x.split() for x in tempstore]
        values = {y[0]:int(y[1]) for y in tempo}
        return(values)