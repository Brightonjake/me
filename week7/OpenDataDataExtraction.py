import pandas as pd
import os

path = 'week7/Data/'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
#Create list of all the files in the directory        

temp_table= pd.DataFrame()

for f in files: 
    read_file = pd.read_csv(f)
    #Reads different file for each iteration

    new_info = read_file[search_criteria]
    #Searches the file and obtains rows with certain characteristic

    new_info = new_info.reset_index(drop=True)
    #deletes index column
 
    new_column = [f,f]
    new_info['Area'] = new_column
    #Adds new column with area name

    main_table = pd.concat([new_info, temp_table], axis=0)
    temp_table = main_table
    #Combines data from each iteration into one table

main_table= main_table.drop ("MEASURE",axis=1)
main_table= main_table.drop ("Description",axis=1)
#Deletes measure column, description column

new_file = "week7/Homeless_around_uni"
main_table.to_csv(new_file, encoding='utf-8', index=False)