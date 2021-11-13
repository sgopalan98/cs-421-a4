from nltk.parse.corenlp import CoreNLPServer
from nltk.parse.corenlp import CoreNLPDependencyParser

# Function: get_dependency_parse(input)
# This function accepts a raw string input and returns a CoNLL-formatted output
# string with each line indicating a word, its POS tag, the index of its head
# word, and its relation to the head word.
# Parameters:
# input - A string containing a single text input (e.g., a sentence).
# Returns:
# output - A string containing one row per word, with each row containing the
#          word, its POS tag, the index of its head word, and its relation to
#          the head word.
def get_dependency_parse(input):
    output = ""

    # Make sure your server is running!  Otherwise this line will not work.
    dep_parser = CoreNLPDependencyParser(url="http://localhost:9000")

    # Write your code here.  You'll want to make use of the
    # CoreNLPDependencyParser's raw_parse() method, which will return an
    # iterable object containing DependencyGraphs in order of likelihood of
    # being the correct parse.  Hint: You'll only need to keep the first one!
    #
    # You'll also likely want to make use of the DependencyGraph's to_conll()
    # method---check out the docs to see which style (3, 4, or 10) to select:
    # https://www.nltk.org/_modules/nltk/parse/dependencygraph.html#DependencyGraph.to_conll
    parsedInput = dep_parser.raw_parse(input)
    dependencyTree = parsedInput._next_()
    output = dependencyTree.to_conll(4)

    return output

# Use this main function to test your code when running it from a terminal.
# Sample code is provided to assist with the assignment; feel free to change/remove it if you want.
# You can run the code from terminal as: python3 q1.py
# It should produce the following output:
# 		  $python3 q1.py
#           I	    PRP	2	nsubj
#           love	VBP	0	ROOT
#           NLP	    NNP	2	obj
#           !	    .	2	punct
def main():
    output = get_dependency_parse("I love NLP!")
    print(output)  # Print the output to the terminal.


################ Do not make any changes below this line ################
if __name__ == '__main__':
    exit(main())