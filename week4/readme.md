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

template = "https://pokeapi.co/api/v2/pokemon/{id}"

    url = template.format(base=template, id=5)
    r = requests.get(url)
    if r.status_code is 200:
        the_json = json.loads(r.text)
    return {"name": None, "weight": None, "height": None}

#URL template, ID to be inserted
#ID, number of pokemon in pokedex
#200- url status code, all good. 404 is no access etc.
#Convert json from internet to python

#abil = the_json ["abilities"]
#To finish: create loop, with range 1-4. height 