import os, fnmatch, time
from datetime import datetime
from bs4 import BeautifulSoup

def pAndl(arg=''):
    print(arg)
    log.write(arg+'\n')
    # Simple function to print and write to a log

start=time.time()
now=datetime.now()

log=open('Analyze_log_{ts}'.format(ts=now),'w+')
os.system(command='mv "{log}" {logsdir}'.format(log=logname,logsdir=logsdir)) # Move log to logs directory

basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs/' # Logs directory
bsdst=basepath+logsdir # Base destination to work with


pAndl('Program has started, the date is the {day} of {month}, {year}. the time is {time}'.format(day=now.strftime('%d'),month=now.strftime('%B'),year=now.strftime('%Y'),time=now.strftime('%X')))
pAndl()# Prints whitespace for readability

directories=os.scandir(bsdst+'evtx_logs') # Directories to work with

counter1=0 # File counter
counter2=0 # Total event IDs
counter3=0 # Matched IDs

eventsToMatch={1102:'',4611:'',4624:'',4634:'',4648:'',
               4661:'',4662:'',4663:'',4672:'',4673:'',
               4688:'',4698:'',4699:'',4702:'',4703:'',
               4719:'',4732:'',4738:'',4742:'',4776:'',
               4798:'',4799:'',4985:'',5136:'',5140:'',
               5142:'',5145:'',5156:'',5158:''}

for directory in directories:
    with os.scandir(directory) as vessel:
        for item in vessel:
            if fnmatch.fnmatch(item,'*.xml'):
                with open(item) as fileToParse:
                    for line in fileToParse:
                        print(fileToParse.readline())
