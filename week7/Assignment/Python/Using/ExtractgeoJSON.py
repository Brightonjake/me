import json
import pandas as pd
import os

with open("week7/Pretty_sa2.geojson",'r') as outfile:
        geo_dict=json.load(outfile)

IDs = [9, 304, 25, 537, 266, 330, 130, 110, 102]

area_code_column = []
coordinate_column = []

for x in IDs:
        area_code_column.append(geo_dict["features"][x-1]["properties"]["sa2_maincode_2016"])
        coordinate_column.append(geo_dict["features"][x-1]["geometry"]["coordinates"])

new_table= pd.DataFrame()

new_table['Code'] = area_code_column
new_table['Coordinate'] = coordinate_column

new_file = "week7/geocode_around_uni"
new_table.to_csv(new_file, encoding='utf-8', index=False)