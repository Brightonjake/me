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

