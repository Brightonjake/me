"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#Creates a list with 'what', 'does' etc. under variable some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#prints a random word from the list some_words
for word in some_words:
    print(word) #prints 'what'
    #Then repeats and prints 'does', then repeats until all words are printed. Same order as the list was written

#print the words in the list in a random order
for x in some_words:
    print(x) #same as above. Loops until it prints all the words on the list in order

#print the whole list on one line
print(some_words) #prints the list but still in the bracket rather than a sentance

#prints the words than longer than 3 letters
if len(some_words) > 3:
    print('some_words contains more than 3 words') #prints the phrase in the arguement, based on the condition?

def usefulFunction(): #defines
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #No idea, don't understand article
    print(platform.uname()) #Now understand, command prints six attributes of system, node, release, version, machine, and processor for my computer

usefulFunction() #enacts function
