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

results2 = [] 
    for i in range (number_of_items):
        results2.append(symbol)

    return results2
#Result- row of symbols, number_of_items long

#Line 1: For these type of problems, have to create empty list
#Line 2: Other command for loop, range sets number of repetitions
#Line 3: append command combines argument into list
#Line 4: Returns the desired results to past the test. By having an empty list it's easier to return

results3 = []
    for i in range(10):
        results3.append(loops_1a())
    
    return results3
#Result- 10 x 10 grid of stars, loop_1a - 10x row of stars

#range(10): for loops repeats 10 times, in this case creates 10 rows as result from previous answer (a row of stars) is added into the list every loop

results4 = []

    for i in range (10):
         print_row = [str(i),str(i), str(i), str(i), str(i), str(i), str(i), str(i), str(i), str(i)]
         results4.append(print_row)

    return results4
#Result- 10 x 10 grid of ascending numbers, each row same number

#i - integer
#str (i)- turns each integer into a string, requirement of the question
#In each loop, i increases by 1. Default setting of for loop

results5 = []
    results6 = []

    i=0
    while i < 10:
        results5.append(str(i))
        i=i+1

    for i in range (10):
         results6.append(results5)
    
    return results6
#10 x 10 grid of numbers rising left to right

#A loop followed by a loop, while loop didn't have to be used. First loop creates list 0 to 9, second loop prints that list as another row

results7 = []

    for ii in range (10):
        temp1 = []
        for jj in range(5):
            temp1.append('(i{a}, j{b})'.format(a=ii,b=jj))
        results7.append(temp1)

    return results7
#10 x 10 grid of coordinates

#COPIED
#Uses loop within a loop with a temporary list
#First range defines grid height
#Second range defines width
#.format - substitutes values into formula
#Note: different indentation. First append within range (5) loop for row, second append outside but within range (10) loops to create grid

results8 = []

    for i in range (0,10):
        temp = []
        for j in range (0,i+1):
            temp.append(str(j))
        results8.append(temp)
    return results8
#Wedge of numbers

#Range (0,10)- range between these values
#Variable used in range instead of fixed number for second loop, therefore changes length of each row per repetition


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