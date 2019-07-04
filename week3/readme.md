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


Exercise 3

#Edited from exercise 2
#Added lower bound, error message for outside of bounds, integer check

while True:
        try:
            lower = int(input("Enter a lower bound: "))
            print ("Thanks! {} looks good.".format (lower))
            break
        except Exception as e:
            print ("err, you wot, try again ({})".format(e)) 
#added input for lower bound, within check for integer (exercise 1)
    while True:
        try:
            upper = int(input("Enter an upper bound: "))
            print ("Thanks! {} looks good.".format (upper))
            break
        except Exception as e:
            print ("err, you wot, try again ({})".format(e)) 
#Check for integer added to upper bound input
    while upper < lower:
      print ("Your upper bound is lower than your lower limit!")
      upper = int(input("Enter another upper bound: "))
#Check to make sure upper bound > lower bound
    print("OK then, a number between {} and {} ?".format(lower,upper))
    actualNumber = random.randint(lower, upper)
#range changed from (0,upper) to (lower to upper)
    guessed = False

    while not guessed:
      while True:
        try:
            guessedNumber = int(input("Guess a number: "))
            print ("Thanks! {} looks good.".format (guessedNumber))
            break
        except Exception as e:
            print ("err, you wot, try again ({})".format(e)) 
#check for integer added to guess

      print("You guessed {},".format(guessedNumber),)
      if guessedNumber == actualNumber:
          print("You got it!! It was {}".format(actualNumber))
          guessed = True
      elif guessedNumber < lower or guessedNumber > upper:
          print("Out of Range, try again :'(")
#out of range error for guess
      elif guessedNumber < actualNumber:
          print("Too small, try again :'(")
      else:
          print("Too big, try again :'(")
    
    return "You got it!"



Exercise 4
#Binary search, algorithm (finds answer without input) 

tries = 0
guess = round (low + 0.5*(high-low), None)
#Guess is halfway between high and low, depending on input
#Note: it's rounded, reduces the number of permutations required. First argument is number to be rounded (in this case our expression), 2nd argument is the digit that is rounded to (default is 0, ie. whole numbers)

while guess != actual_number:
#while loop: keeps looping until condition met
    if guess > actual_number:
        high = guess
#changes bound to narrow search
    elif guess < actual_number:
        low = guess
#same as above but opposite as guess < actual_number
    guess = round (low + 0.5*(high-low), None)
    tries = tries + 1
#Must change inputs for while loop!!!!!
    return {"guess": guess, "tries": tries}
#Dictionary. Code more simple if it uses terms required to return as variables