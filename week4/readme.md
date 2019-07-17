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

    
    api_key = 
#Fill in when it arrives!!!!

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key={api_key}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
#? Divides website URL from the arguments [key, max length, min length, limit]
#note nice indentation which breaks it up

    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(api_key="", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    
    for i in range(20, 3, -2):
        url = baseURL.format(api_key="", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list
#Explain




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

gcode_data= open(LOCAL + "/Trispokedovetiles(laser).gcode").read()
#Opens and reads
#No need for JSON.loads line as it is not a JSON file and doesn't need to be converted to a dictionary

count = gcode_data.count("M10 P1")
#Inbuilt function, counts entered argument/substring within the file/string

f = open("week4/lasers.pew", "w+")
#Defines variable. Opens a new file and gives writing permission
#Note: Use of relative path (week4/) before the file name to save in the week 4 folder. started in me folder
#This is different to absolute path which in this case would be "/Users/jbrighton/Documents/1161/me/week4/lasers.pew"

f.write(str(count))
#Command to write in file, f defined above
#note: converted to string, count predefined above

f.close
#Important step, must close when you write for it to work





Other

Define error
#Stated there was a syntax error with def of pokedex function
#Error was actually a paranthesis error in the code above
#Take VScode help with a grain of salt

Hash out
#can hash out a whole paragraph of code by highlighting and pressing command /
#can also add speech marks before and after instead