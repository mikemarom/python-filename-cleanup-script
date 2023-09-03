#import OS module
import os

# get the list of all files and directories
path = "/Users/mmarom/test_files/"
dir_list = os.listdir(path)

#print only the files, not directories
for each_file in dir_list:
    if os.path.isfile(path+each_file):  # only if file
        new_filename = each_file.replace(".", " ", each_file.count('.')-1) # remove all the dots, other than the last one, from the filename
        os.rename(path+each_file,path+new_filename) # change old filename to new one
		
		
		
		