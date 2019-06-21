TODO: Reflect on what you learned this week and what is still unclear.

#How to Push: 



Exercise 0

a_number + 1
a_number + another_number
#integers add together without formatting

a_string.upper()
#changes a string to uppercase (note: it has no argument + a_string is interchangeable variable)

a_string.upper() + '!'
#concatenate: combine/add. Adds exclamation mark (note: '' to make ! a string)

a_string.upper() + " " + str(a_number)
#Note: " " adds a space, str needed to convert integer to a string



Exercise 1

#Add a breakpoint by clicking on red circle on left of the coding screen

#python by default prints lists in order? 

for word in some_words:
    print(word) 
for x in some_words:
    print(x)
#there are different ways to write the same thing 

if len(some_words) > 3:
#len: returns number within container. For some_words there are 5 words. Condition is true in this case

print(platform.uname())
#prints system, node, release, version, machine, and processor of the computer



Exercise 2

#Debugger pinpoints problems with the code. Be mindful of writing functions/variables, brackets, commas, semi-colons, including quotation marks. Simple mistakes makes the code not work



Exercise 3

bool(a_number%2)
#bool-boolean: true/false = 1/0
#%-modulo division: gives the remainder from division

if moves==True:
        if should_move==False:
            return ("Duct Tape")
        elif should_move==True:
            return ("No Problem")
#For conditional statements (if, elif, else), must have semicolon
#Note: == means equal to, = is for assigning variables
#      != means not equal to