'''Code for opening and analyzing a folder'''

import os, fnmatch, zipfile 
#import OS to work on directories, fnmatch to check for xml files, and zipfile to extract directories

basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs'
bsdst=basepath+logsdir # Base destination to work with

# Attempts to make logs directory if it doesnt exist. works fine for now
try:
    os.mkdir(logsdir)
except FileExistsError:
    print('Folder exists!')

# Reads directory and prints out all items for now.  
# Printed with respectable folder names and a whitespace.
with zipfile.ZipFile(basepath+'/evtx_logs.zip') as zipref:
    zipref.extractall(bsdst) # Extracts evtx_log.zip into logs directory to work with

directories=os.scandir(bsdst+'/evtx_logs') # Directories to work with

counter1=0 # Subdirectory counter
counter2=0 # File counter

for directory in directories:
    print('Working on {0} directory'.format(directory.name))
    counter1+=1 # Prints the name of the directory and increments counter
    with os.scandir(directory) as vessel:
        for item in vessel:
            #if item.is_file():
            if fnmatch.fnmatch(item,'*.xml'):
                print('You have an XML file, please remove it.') # Tests for XML file extensions
            counter2+=1
            print('Converting {0}...'.format(item.name)) # Prints name of file and increments counter 
            # Figure how to create multiple directories and save the files to respective directories
    print() # Prints whitespace for readability




print('Traversed {0} folders'.format(counter1))
print('Converted {0} files'.format(counter2))
        
#os.rmdir(logsdir)