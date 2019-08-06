
 with open("small_Pretty_sa2.geojson copy",'r') as outfile:
        geo_dict=json.load(outfile)

print (geo_dict["features"]["properties"]["sa2_maincode_2016"])


#118021348