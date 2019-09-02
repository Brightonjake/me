import pandas as pd
import os

path = 'week7/Assignment/CSV Files'
files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file == '.DS_Store':
                pass
    #Exception for random file, not sure what it is
        else:
                files.append(os.path.join(r, file))
    #Create list of all the files in the directory        

temp_table= pd.DataFrame()

for f in files: 
        try:
                read_file = pd.read_csv(f)
        except:
                pass
    #Reads different file for each iteration

        search_criteria = read_file['Description']== "Total population (no.)"
        new_info = read_file[search_criteria]
        #Searches the file and obtains rows with certain characteristic

        new_info = new_info.reset_index(drop=True)
        #deletes index column
        
        make_string = str(f)
        split_filepath = make_string.split("/")
        name_and_code= split_filepath[3]
        split_name_and_code= name_and_code.split("_")
        area_code = split_name_and_code[0]
        area_name = split_name_and_code[1]
        #Breaks down filename for area name and code
        
        new_info['Code'] = area_code
        new_info['Area'] = area_name
        #Adds new column with area name and code

        main_table = pd.concat([new_info, temp_table], axis=0)
        temp_table = main_table
        #Combines data from each iteration into one table

main_table= main_table.drop ("MEASURE",axis=1)
main_table= main_table.drop ("Description",axis=1)
#Deletes measure column, description column

new_file = "week7/Assignment/population"
main_table.to_csv(new_file, encoding='utf-8', index=False)