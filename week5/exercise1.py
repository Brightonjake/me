# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    for i in range(start-stop+1,stop-stop,-1):
        print(message + " " + str(i))
    print(completion_message)

# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    import math
    hypotenuse = (math.sqrt((base ** 2) + (height ** 2)))
    return hypotenuse

def calculate_area(base, height):
    area = ((base * height)/2)
    return area

def calculate_perimeter(base, height):
    perimeter = (base) + (height) + (calculate_hypotenuse(base,height))
    return perimeter

def calculate_aspect(base, height):
    if base > height:
        return ("wide")
    if base < height:
        return ("tall")
    else:
        return ("equal")

# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
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


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle (facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    if facts_dictionary['height'] > facts_dictionary ['base']:
        return tall.format(height=facts_dictionary['height'], base=facts_dictionary ['base'],hypotenuse=facts_dictionary ['hypotenuse'])
    elif facts_dictionary['height'] < facts_dictionary ['base']:
        return wide.format(height=facts_dictionary['height'], base=facts_dictionary ['base'],hypotenuse=facts_dictionary ['hypotenuse'])
    else:
        return equal.format(height=facts_dictionary['height'], base=facts_dictionary ['base'],hypotenuse=facts_dictionary ['hypotenuse'])

def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    if return_diagram and return_dictionary:
        return {"diagram": tell_me_about_this_right_triangle (get_triangle_facts(base, height)), "facts": get_triangle_facts(base, height)}
    elif return_diagram:
        return tell_me_about_this_right_triangle (get_triangle_facts(base, height))
    elif return_dictionary:
        return get_triangle_facts(base, height)
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    import requests

    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    
    wordlist = []

    def refractor_WP(start,stop,step):
        for i in range(start,stop, step):
            fullurl=url.format(len=i)
            pull = requests.get(fullurl)   
            if pull.status_code is 200:         
                randword = pull.content  
                if randword is None: 
                    pass
                else:
                    randword = str(randword)
                    wordlist.append(randword[2:len(randword)-1])

    refractor_WP(3,21,2)
    refractor_WP(20,2,-2)    
    return wordlist


def get_a_word_of_length_n(length):
    import requests

    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={leng}"
    if type(length) == int and length >= 3:
        fullurl=url.format(leng=length)
        pull = requests.get(fullurl)   
        if pull.status_code is 200:         
            wordn = pull.content  
            wordn = str(wordn)
            outputword = wordn[2:len(wordn)-1]
                #    this retrives the word from the url
        return outputword
    else:
        return None

def list_of_words_with_lengths(list_of_lengths):
    import requests

    list_of_words = []

    for i in list_of_lengths:
        url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={leng}"
        if type(i) == int and i >= 3:
            fullurl=url.format(leng=i)
            pull = requests.get(fullurl)   
            if pull.status_code is 200:         
                wordn = pull.content  
                wordn = str(wordn)
                outputword = wordn[2:len(wordn)-1]
                list_of_words.append(outputword)
        else:
            pass

    return list_of_words

if __name__ == "__main__":
    list_of_words_with_lengths([4,5,8])