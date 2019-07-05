TODO: Reflect on what you learned this week and what is still unclear.

Tut Notes

Writing a function
Def function_name (arguments)
#To test: put hold point on next function, then enter manually into debugger
#Or
#Add line after eg. hyp = calculate_hypotenuse(3,4)

#Can't test the function if you haven't called it. Been baked into the previous week exercises 

Recursive
#Function that calls itself

def sum(list):
    if len(list) == 1: 
    return list [0]
#base case
    else:
    return list[0] + sum list[1:]
#Slice list. Super useful
#Recursive step

print(sum([5,7,3,8,10]))  
#Test

#Another example:
def recur_fibo(n):
    if n <= 1:
        return n
    else
        return (recur_fibo (n-1) + recur_fibo (n-2))

print (recur_fibo(9))
# 1 1 2 3 5 8 13 21 34




Exercise 1

#Deleted bad function
def do_bunch_of_bad_things():
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)

#write notes on the rest

