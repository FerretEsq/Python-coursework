import os, fnmatch, time, json
from datetime import datetime
from matplotlib import pyplot as pls 


def pAndl(arg=''):
    print(arg)
    log.write(arg+'\n')
    # Simple function to print and write to a log


start=time.time()
now=datetime.now()
logname='Visdata_log_{ts}'.format(ts=now)
#log=open(logname,'w+')

basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs/' # Logs directory
bsdst=basepath+logsdir # Base destination to work with

os.system(command='mv "{log}" {logsdir}'.format(log=logname,logsdir=logsdir)) # Move log to logs directory

print('Program has started, the date is the {day} of {month}, {year}. the time is {time}'.format(day=now.strftime('%d'),month=now.strftime('%B'),year=now.strftime('%Y'),time=now.strftime('%X')))
print()# Prints whitespace for readability

list1=None
list2=None

with os.scandir(bsdst) as base:
    for item in base:
        if item.is_file():
            if fnmatch.fnmatch(item.name,'JSON_Analyze_*'):
                with open(item) as jsonFile:
                    data=json.load(jsonFile)
                    list1=data[0]
                    list2=data[1]


for key,value in list1.items():
    print('Event {0}: Occured {1} times'.format(key,value))
print('')
for key,value in list2.items():
    print('Event {0}: Occured {1} times'.format(key,value))

