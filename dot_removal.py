#import OS module
import os

# get the list of all files and directories
path = "/Users/mmarom/Downloads/"
dir_list = os.listdir(path)

print ("Files in '",path,"' are:")

#print only the files, not directories
for each_file in dir_list:
	if os.path.isfile(path+each_file):  # only if file
		print (each_file)
		print (each_file.rfind("."))
		
		
		
		