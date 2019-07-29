import pandas as pd

File_list = ["Kensington_NSW", "Kingsford", "Mascot_Eastlakes", 
"Paddington_MoorePark", "RandwickNorth","RandwickSouth", "Waterloo_Beaconsfield"]

temp_table= pd.DataFrame()

for i in File_list: 
    file_path="week7/Data/{area}.csv".format(area=i)
    read_file = pd.read_csv(file_path)
    #Reads different file for each iteration

    search_criteria = read_file['Description']== "Homeless rate per 10,000 persons"
    new_info = read_file[search_criteria]
    #Searches the file and obtains rows with certain characteristic

    new_info = new_info.reset_index(drop=True)
    #deletes index column

    new_column = [i,i]
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