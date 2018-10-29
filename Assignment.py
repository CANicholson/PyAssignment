def main(filename):
    """A function which takes a file filled with strings and finds the best acronym based upon scoring

    The lower the score the better the acronym. The acronyms are then stored in an output file"""
    if filename.endswith(".txt"):
        pass
    else: 
        print("File is not a .txt. Please try again with a .txt file")