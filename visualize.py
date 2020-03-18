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

matcheDict=None
otherDict=None

# Passes JSON dictionaries into local dictionaries
with os.scandir(bsdst) as base:
    for item in base:
        if item.is_file():
            if fnmatch.fnmatch(item.name,'JSON_Analyze_*'):
                with open(item) as jsonFile:
                    data=json.load(jsonFile)
                    matcheDict=data[0]
                    otherDict=data[1]

# Create 8 lists to use for matplot. Key:value pairs transferred with list comprehension ensures correct order
matchedID=[item for item in matcheDict.keys()]
matchedValue=[item for item in matcheDict.values()]

occuredID=[item for item in otherDict.keys()]
occuredValue=[item for item in otherDict.values()]

matchedID2=[item for item in matchedID if item != '5145'] # Create new list for graph missing event ID 5145 
matchedValue2=[item for item in matchedValue if item<200]

occuredID2=[item for item in occuredID if item != '1'] # Create new list for graph missing event ID 1
occuredValue2=[item for item in occuredValue if item<200]

# Feedback on all event IDs and their match frequency
pAndl('Analyzing JSON file')
for key,value in matcheDict.items():
    pAndl('Event {0}: Matched {1} times'.format(key,value))
pAndl('')
for key,value in otherDict.items():
    pAndl('Event {0}: Occured {1} times'.format(key,value))

# Create visualization of matched IDs
plt.style.use('seaborn-dark')
y_pos=np.arange(len(matchedID))
plt.figure(figsize=(17,15))
plt.barh(y_pos,matchedValue,height=0.5)
plt.yticks(y_pos,matchedID)
plt.xlabel('Event ID')
plt.ylabel('Matches')
plt.title('Matched IDs')
plt.grid(linestyle='--',linewidth=1.2)
plt.savefig('{}/MatchedIDsFull.png'.format(logsdir))
plt.show()

# Create visualization of matched IDs without event 5145 which eclipses all other event IDs
y_pos=np.arange(len(matchedID2))
plt.figure(figsize=(10,15))
plt.barh(y_pos,matchedValue2,height=0.5)
plt.yticks(y_pos,matchedID2)
plt.xlabel('Event ID')
plt.ylabel('Matches')
plt.title('Matched IDs without event ID 5145')
plt.grid(linestyle='--',linewidth=1.2)
plt.savefig('{}/MatchedIDs-5145.png'.format(logsdir))
plt.show()

# Create Visualization of all other IDs
y_pos=np.arange(len(occuredID))
plt.figure(figsize=(25,15))
plt.barh(y_pos,occuredValue,height=0.5)
plt.yticks(y_pos,occuredID)
plt.xlabel('Occurences')
plt.ylabel('Event IDs')
plt.title('Other Occured IDs')
plt.grid(linestyle='--',linewidth=1.2)
plt.savefig('{}/OtherIDsFull.png'.format(logsdir))
plt.show()

# Create visualization without event ID 1 which eclipses all other event IDs in the list
y_pos=np.arange(len(occuredID2))
plt.figure(figsize=(15,15))
plt.barh(y_pos,occuredValue2,height=0.5)
plt.yticks(y_pos,occuredID2)
plt.xlabel('Occurences')
plt.ylabel('Event IDs')
plt.title('Other Occured IDs without event ID 1')
plt.grid(linestyle='--',linewidth=1.2)
plt.savefig('{}/OtherIDs-1.png'.format(logsdir))
plt.show()

log.close()
