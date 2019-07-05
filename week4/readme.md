TODO: Reflect on what you learned this week and what is still unclear.

Tut Notes:

my_list = [54,32,1]
another_list= ["my_string", "!", "2"]
another_list[1]

#dictionary
my_dict= {"key":"value"}
my_dict[key]

#Can call a dictionary inside a dictionary
#Need to read the API files to figure out what needs to be called

&minLength=10&maxLength=10&limit=1
#add to end of URL to make a search criteria




Exercise 1

#Parse some JSON: get information off a file 
#JSON (Javascript object notation) is a dictionary that is universal across all coding languages

json_data = open(LOCAL + "/lazyduck.json").read()
#given: Opens local file + reads it (ie. return to me as text; read is a file function only for the open command)
#To find other function use "dir json_data" or search on the internet

data = json.loads(json_data)
#given: converts messy string from JSON file to a nice dictionary

answer1= data["results"][0]["name"]["last"]
answer2= data["results"][0]["login"]["password"]
#Finding specific data. Use http://www.jsoneditoronline.org/ to understand how JSON file is nested (ie. a list within a list). Find the chain for the information you want. Note: Look out for the type of brackets. [] means list and {} means dictionary, you'll need integer indices for lists, and named keys for dictionaries. Remember indices start from 0.

answer3= int(data["results"][0]["id"]["value"])
answer4= int(data["results"][0]["location"]["postcode"])
answer5= answer3 + answer4
#Note: Answer 3 and 4 converted to integers because they need to be added

return {"lastName": answer1, "password": answer2, "postcodePlusID": answer5}
#Is there a better way to do this?




Word Pyramid
#API- application program (someone's code) interface

    answer=[]

    key = "a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
    template = "http://api.wordnik.com/v4/words.json/randomWords?api_key={key}&minLength={minLength}&maxLength={maxLength}&limit={limit}"
#? Divides website URL from the arguments [key, max length, min length, limit]
    
    #for i in range (8):
    for i in range (3,19,2):
        url = template.format(base=template, minLength=i, maxLength=i, limit=1, key=key)
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            answer.append(str(the_json)

    #for i in range (8):
        #for i in reversed (range (19,3,-2)):
            #url = template.format(base=template, minLength=i, maxLength=i, limit=1, key=key)
            #r = requests.get(url)
            #if r.status_code is 200:
                #the_json = json.loads(r.text)
                #answer.append(str(the_json))
#Define function and recall so you don't have to copy code





Pokedex Problem
#Find tallest pokemon of first 5 entries into the pokedex and return information on them


def pokedex(low=1, high=5):
#1 and 5 are default arguments unless something is assigned
#ie. pokedex (100,151) will search between those IDs

template = "https://pokeapi.co/api/v2/pokemon/{id}"
#Defines variable for later, URL with general arguments

index = -1
tallest = -1
#Variables assigned to remember the index for the tallest pokemon. Given negative value to start to ensure a real value gets assigned

for x in range (low, high):
#Loop created as process the same to check the first 5

    url = template.format(base=template,id=x)
#Template used with new ID to be inserted each loop

    r = requests.get(url)
#Given, requests information from website. Like searching on google

    if r.status_code is 200:
#URL status code check: 200 = working normally. 404 not found etc. Can look up others if needed 

        data = json.loads(r.text)
#Converts URL information (JSON file) into dictionary

        height = data["height"]
#Assessing wanted data from dictionary

        if height > tallest:
            tallest = height
            index = x
#Changes index if height is bigger than the last

url = template.format(base=template,id=index)
r = requests.get(url)
if r.status_code is 200:
    data = json.loads(r.text)
    answer1 = data["name"]
    answer2 = data["weight"]
    answer3 = data["height"]
#Repeated code, gets extra information for the desired pokemon

    return {"name": answer1, "weight": answer2, "height": answer3}



def diarist():
#Read Trispokedovetiles(laser).gcode and count the number of times the laser is turned on and off. That's the command "M10 P1".
#Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.

#What was the purpose of this????



Define error
#Stated there was a syntax error with def of pokedex function
#Error was actually a paranthesis error in the code above
#Take VScode help with a grain of salt

Hash out
#can hash out a whole paragraph of code by highlighting and pressing /
#can also add speech marks before and after instead