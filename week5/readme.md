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



#New functions


def countdown(message, start, stop, completion_message):
    for i in range(start,stop-1,-1):
#Stop -1 so it includes the value of stop
#-1 Step so it counts down
        print(message + " " + str(i))
    print(completion_message)




def calculate_hypotenuse(base, height):
    import math
#Needed package. Has .sqrt (square root) function
    hypotenuse = (math.sqrt((base ** 2) + (height ** 2)))
# ** 2 = the power of 2
    return hypotenuse



#Note: Skipped boring examples!!!!



def calculate_perimeter(base, height):
    perimeter = (base) + (height) + (calculate_hypotenuse(base,height))
#calls upon another function for calculation
#Don't convert to integers because this round the values!
    return perimeter




def calculate_aspect(base, height):
    if base > height:
        return ("wide")
    if base < height:
        return ("tall")
    else:
        return ("equal")
#Could only write this function once I understood what is was used for (to categorise each triangle for the diagram as either wide, tall or equal)



def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }
#Summarising function, returns as dictionary and calls upon other functions. 
#Lot easier to read this way!




def tell_me_about_this_right_triangle (facts_dictionary):
#Generally the arguments, while they may not be defined are generally suppose to be used
#Allows get_triangle_facts to be inserted later. Therefore has to call from dictionary, clue in variable name

if facts_dictionary['height'] > facts_dictionary ['base']:
#This could be changed to:
# if facts_dicitonary [aspect] == 'tall'
        return tall.format(height=facts_dictionary['height'], base=facts_dictionary ['base'],hypotenuse=facts_dictionary ['hypotenuse'])
#returns the pre-made tall triangle diagram with relevent parts  
#could be made visually simpler by changing facts_dictionary['height'] into another variable    
    elif facts_dictionary['height'] < facts_dictionary ['base']:
        return wide.format(height=facts_dictionary['height'], base=facts_dictionary ['base'],hypotenuse=facts_dictionary ['hypotenuse'])
    else:
        return equal.format(height=facts_dictionary['height'], base=facts_dictionary ['base'],hypotenuse=facts_dictionary ['hypotenuse'])
#same as above except for other triangle types




def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    if return_diagram and return_dictionary:
        return {"diagram": tell_me_about_this_right_triangle (get_triangle_facts(base, height)), "facts": get_triangle_facts(base, height)}
    elif return_diagram:
        return tell_me_about_this_right_triangle (get_triangle_facts(base, height))
    elif return_dictionary:
        return get_triangle_facts(base, height)
    else:
        print("You're an odd one, you don't want anything!")
#Ultimate function. Calls other functions if requested



def get_a_word_of_length_n(length):
#Altered word pyramid function
    import requests

    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={leng}"
    if type(length) == int and length >= 3:
#Safeguard: Makes sure length given is number and more than 3 (otherwise not really a word)
        fullurl=url.format(leng=length)
        pull = requests.get(fullurl)   
        if pull.status_code is 200:         
            wordn = pull.content  
            wordn = str(wordn)
            outputword = wordn[2:len(wordn)-1]
#wordn[2:len(wordn)-1] : returns 3rd letter to the length of word -1 from the string. 
#AKA removes 'b ' from start and end
        return outputword
    else:
        return None
#Returns nothing if safeguard wasn't met




def list_of_words_with_lengths(list_of_lengths):
    import requests
    import time

    pyramid_list = []

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key={api_key}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1")
    
    for i in range(2):
        url = baseURL.format(api_key="yl8vro4nxaxv736r8qv0bhxcgpjj1oab3zm0yzfmxyh5yiypo",length=(list_of_lengths[i]))
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)

    return pyramid_list
#Uses the old URL, still works



if __name__ == "__main__":
    get_a_word_of_length_n(5)
#At end of the exercise if you want to test something without having to type it in the debugger




Exercise 2



def abba(source="abba", guard=3):
    
    parts = list(source)
#Splits the word into a list of letters eg abba = [a, b, b, a]. More friendly format
    result = list(map(apply_rules, parts))
#Applies rules to each letter in list
    new_string = "".join(result)
#Turns new list into a combined string    
    guard -= 1
#Takes 1 off the guard, otherwise it would run forever
    if guard > 0:
        return abba(new_string, guard)
#repeats function with input of new_string, smaller guard
    else:
        return new_string
#returns string after a few rounds

def apply_rules(letter):
#substitution function or the rules
    if letter == "a":
            return "bba"
        elif letter == "b":
            return "aob"
        elif letter == "o":
            return "oa" 
        else:
            return letter




def italian_dinner(axiom="tomatoes", guard=6):

#This differs from abba by:

#1st line:
parts = axiom.split(" ")
#Splits by each word rather than individual letters

#3rd line
new_string = " ".join(result)
#Subtle difference. Space left between ""
#Joins the string with a space between so it reads as a sentance