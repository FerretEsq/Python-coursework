'''Code for opening and analyzing a folder'''

import os, fnmatch, zipfile, time, subprocess
#import OS to work on directories, fnmatch to check for xml files, and zipfile to extract directories

start=time.time()

basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs/' # Logs directory
bsdst=basepath+logsdir # Base destination to work with
script=basepath+'evtx_dump.py'

# Attempts to make logs directory if it doesnt exist. works fine for now
try:
    os.mkdir(logsdir)
except FileExistsError:
    print('Folder exists!')


# Extracts all directories and files into newly created (or existing) 
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
                break
            counter2+=1
            print('Converting {0}...'.format(item.name)) # Prints name of file and increments counter 
            #subprocess.call(['python3','evtx_dump.py',item.name])
            # python3 ~/CL5235_k1828612_Toms/evtx_dump.py PanacheSysmon_vs_AtomicRedTeam01.evtx > pan.xml
            #os.system(command='python3 {0} {1}evtx_logs/{2} > {2} '.format(script,bsdst,item.name))
            print('Conversion complete!')
    print() # Prints whitespace for readability


print('Program finished in {0:.2f} seconds'.format(time.time()-start))
print('Traversed {0} folders'.format(counter1))
print('Converted {0} files'.format(counter2))
        
#os.rmdir(logsdir)