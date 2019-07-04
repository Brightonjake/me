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

#Parse some JSON: get information off a file (python formatted)

json_data = open(LOCAL + "/lazyduck.json").read()
#given. Opens local file
data = json.loads(json_data)
#given. variable assigned

answer1= data["results"][0]["name"]["last"]
answer2= data["results"][0]["login"]["password"]
#Finding specific data. Use http://www.jsoneditoronline.org/ to understand how JSON file is nested (ie. a list within a list). Find the chain for the information you want. Note: Look out for the type of brackets. [] means list and {} means dictionary, you'll need integer indices for lists, and named keys for dictionaries. Remember indices start from 0.

answer3= int(data["results"][0]["id"]["value"])
answer4= int(data["results"][0]["location"]["postcode"])
answer5= answer3 + answer4
#Note: Answer 3 and 4 converted to integers because they need to be added

return {"lastName": answer1, "password": answer2, "postcodePlusID": answer5}
#Is there a better way to do this?




Pokedex Problem
#Find tallest pokemon of first 5 entries into the pokedex and return information on them

index = -1
tallest = -1
#Variables assigned to remember the index for the tallest pokemon. Given negative value to start to ensure a real value gets assigned

for x in range (low, high):
#Loop created as process the same to check the first 5
    url = template.format(base=template,id=x)
#Template used with new ID to be inserted each loop
    r = requests.get(url)
#Given, command to get information from website
    if r.status_code is 200:
#URL status code check: 200 = working normally. 404 is no access etc. Can look up others if needed 
        data = json.loads(r.text)
#Converts URL information into JSON file
        height = data["height"]
#Assessing wanted data from JSON file
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