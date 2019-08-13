import os

path = 'week7/Assignment/CSV Files'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file == '.DS_Store':
                pass

        else:
                files.append(os.path.join(r, file))

for f in files:
        make_string = str(f)
        split_filepath = make_string.split("/")
        name_and_code= split_filepath[2]
        split_name_and_code= name_and_code.split("_")
        area_code = split_name_and_code[0]
        area_name = split_name_and_code[1]
        print (area_code, area_name)

