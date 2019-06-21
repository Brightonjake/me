TODO: Reflect on what you learned this week and what is still unclear.

#How to Push: 
#Step 1: Stage changes, press plus (allows you to save in stages)
#Step 2: Commit changes, press tick (saves)
#Step 3: Push changes, use "push" from drop down menu (send to GIT)



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




For Loops

my_list = [1,2,3,4]
for value in my_list:
    print (my_value) 
#prints each number on own line

for idx in range(5):
    print(idx)
#same as above, without defining variable

list (range(1,6))
#makes list from 1-5 instead of 0-4, which is what happens with range(5)

for idx in range(len(my_list)):
    print (idx)
#len- length, prints 0,1,2,3 if my list is 4 long

for idx in range(len(my-list)):
    print (my_list[idx])
#same as original but sometimes you need index

for idx,value in enummerate (my_list) 
#????   



While Loops

x = 10
y = 99
while y>= x:
    print (my_list[0])
#need to create the condition to end the loop otherwise it won't stop

idx = 0 
while idx < len(my_list):
    print (my_list[idx])
    idx = idx + 1
#starting condition, need to manually increase idx (difference of while loop vs for loop)

range (1, 5)
#range can have multiple input functions, start from 1 end at 5

range (1, 5, 2)
#start  from 1 to 5 with steps of 2

return 
#exclusive to functions, gives value to program. Substitute 

print
#yells and no one grabs