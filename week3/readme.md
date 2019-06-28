TODO: Reflect on what you learned this week and what is still unclear.

Exercise 1

my_list = []
    while start < stop:
        my_list.append(start)
        start=start+step
    return my_list
#Returns a list between start and stop with steps of step

#Uses a while loop instead of range, have to set the conditions for the repetitions (start<stop) and increase of input (start+step) 

my_list= []
    for i in range (start,stop,step):
        my_list.append(i)
    return my_list
#Same as above but using range instead of while loop

my_list= []
    for i in range (start,stop,2):
        my_list.append(i)
    return my_list
#Step of 2 rather than 'step'

InputNumber = input ("Please input a number: ")
    InputNumber = int(InputNumber)
    while InputNumber < low or InputNumber > high:
        InputNumber = input ("Outside of Range, Please input another number: ")
        InputNumber = int(InputNumber)
    return InputNumber
#Result- Ask for a number until you get a number within a range

#Asks for user input
#converts to an integer
#tests in while loop, continues until condition is met
#asks again if it fails

while True:
        try:
            Input_number = int(input(message))
            print ("Thanks! {} looks good.".format (Input_number))
            return Input_number
        except Exception as e:
            print ("err, you wot, try again ({})".format(e)) 

#can use if and else loop
#try command allows malfunction and code not to break
#except executes when there is an error
#return placed in try loop to stop on successful attempt. Otherwise keeps looping

while True:
        try:
            Input_number = int(input(message))
            print ("Thanks! {} looks good.".format (Input_number))
            break
        except Exception as e:
            print ("err, you wot, try again ({})".format(e)) 
        
    while Input_number < low or Input_number > high:
        Input_number = input ("Outside of Range, Please input another number: ")
        Input_number = int(Input_number)
        return Input_number

#combination of the two above, not perfect