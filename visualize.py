import os, fnmatch, time, json
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np

def pAndl(arg=''):
    print(arg)
    log.write(arg+'\n')
    # Simple function to print and write to a log

start=time.time()
now=datetime.now()
logname='Visdata_log_{ts}'.format(ts=now)
log=open(logname,'w+')

basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs/' # Logs directory
bsdst=basepath+logsdir # Base destination to work with

os.system(command='mv "{log}" {logsdir}'.format(log=logname,logsdir=logsdir)) # Move log to logs directory

pAndl('Program has started, the date is the {day} of {month}, {year}. the time is {time}'.format(day=now.strftime('%d'),month=now.strftime('%B'),year=now.strftime('%Y'),time=now.strftime('%X')))
pAndl()# Prints whitespace for readability

# Two empty variables to become dictionaries out of JSON file
matcheDict=None
otherDict=None

# Passes JSON dictionaries into global objects
with os.scandir(bsdst) as base:
    for item in base:
        if item.is_file():
            if fnmatch.fnmatch(item.name,'JSON_Analyze_*'):
                with open(item) as jsonFile:
                    data=json.load(jsonFile)
                    matcheDict=data[0]
                    otherDict=data[1]

# Create 4 lists to use for matplot
matchedID=[item for item in matcheDict.keys()]
matchedValue=[item for item in matcheDict.values()]
occuredID=[item for item in otherDict.keys()]
occuredValue=[item for item in otherDict.values()]

# Feedback on all event IDs and their match frequency
pAndl('Analyzing JSON file')
for key,value in matcheDict.items():
    pAndl('Event {0}: Matched {1} times'.format(key,value))
pAndl('')
for key,value in otherDict.items():
    pAndl('Event {0}: Occured {1} times'.format(key,value))

# Create visualization of matched IDs
y_pos=np.arange(len(matchedID))
plt.figure(figsize=(17,10))
plt.barh(y_pos,matchedValue,height=0.5,alpha=0.5)
plt.yticks(y_pos,matchedID,rotation=20)
plt.xlabel('Event ID')
plt.ylabel('Matches')
plt.title('Matched IDs')
plt.savefig('{}/MatchedIDs.png'.format(logsdir))
plt.show()
plt.close('all')

# Create Visualization of all other IDs
y_pos=np.arange(len(occuredID))
plt.figure(figsize=(37,15))
plt.barh(y_pos,occuredValue,height=0.5,alpha=0.5)
plt.yticks(y_pos,occuredID,rotation=10)
plt.xlabel('Occurences')
plt.ylabel('Event IDs')
plt.title('Other Occured IDs')
plt.savefig('{}/OtherIDs.png'.format(logsdir))
plt.show()

log.close()
