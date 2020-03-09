'''Code for opening and analyzing a folder'''

import os, fnmatch, zipfile, time
from datetime import datetime

def pAndl(arg=''):
    print(arg)
    log.write(arg+'\n')
    # Simple function to print and write to a log

start=time.time()
now=datetime.now()
logname='Convert_log_{ts}'.format(ts=now)
log=open(logname,'w+')

pAndl('Program has started, the date is the {day} of {month}, {year}. the time is {time}'.format(day=now.strftime('%d'),month=now.strftime('%B'),year=now.strftime('%Y'),time=now.strftime('%X')))
pAndl()# Prints whitespace for readability


basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs' # Logs directory
bsdst=basepath+logsdir # Base destination to work with
script=basepath+'evtx_dump.py' # Convert script

# Attempts to make logs directory if it doesnt exist. works fine for now
try:
    os.mkdir(logsdir)
except FileExistsError:
    pAndl('Folder exists!')

os.system(command='mv "{log}" {logsdir}'.format(log=logname,logsdir=logsdir)) # Move log to logs directory

# Extracts all directories and files into newly created (or existing) 
with zipfile.ZipFile(basepath+'/evtx_logs.zip') as zipref:
    zipref.extractall(bsdst) # Extracts evtx_log.zip into logs directory to work with

directories=os.scandir(bsdst+'/evtx_logs') # Directories to work with


counter1=0 # Subdirectory counter
counter2=0 # File counter

for directory in directories:
    pAndl('Working on "{0}" directory'.format(directory.name.replace('_',' ')))
    counter1+=1 # Prints the name of the directory and increments counter
    with os.scandir(directory) as vessel:
        for item in vessel:
            filename=item.name[:len(item.name)-5].replace(' ','_') 
            #This is the stupidest shit. Get JUST the filename by getting all the letters in the file name except the .evtx
            if fnmatch.fnmatch(item,'*.xml'):
                pAndl('You have an XML file in this folder. please remove it')
                break # Tests for XML file extensions
            counter2+=1
            pAndl('Converting {0}...'.format(item.name)) # Prints name of file and increments counter
            os.system(command='cd {logs}/evtx_logs/{dir};sudo python3 {script} \'{log}\' > {fn}.xml'.format(log=item.name.replace(' ','_'),script=script,logs=logsdir,dir=directory.name,fn=filename))
            # ^This is an absolutely ridiculous way of doing it but it almost works.
            # Chains cd command to move to working dir and then executes script there 
            pAndl('Conversion complete!')
    pAndl() # Prints whitespace for readability



pAndl('Finished converting all the files!')
pAndl('The time is {time}'.format(time=now.strftime('%X')))
pAndl('Program finished in {0:.2f} seconds'.format(time.time()-start))
pAndl('Traversed {0} folders'.format(counter1))
pAndl('Converted {0} files'.format(counter2))

log.close()
