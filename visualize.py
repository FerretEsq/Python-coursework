import os, fnmatch, time, json
from datetime import datetime

def pAndl(arg=''):
    print(arg)
    log.write(arg+'\n')
    # Simple function to pAndl and write to a log

start=time.time()
now=datetime.now()
logname='Analyze_log_{ts}'.format(ts=now)
log=open(logname,'w+')

basepath='/home/ferret/CL5235_k1828612_Toms/' # Change directory to 'User' later
logsdir='CL5235_Logs/' # Logs directory
bsdst=basepath+logsdir # Base destination to work with

os.system(command='mv "{log}" {logsdir}'.format(log=logname,logsdir=logsdir)) # Move log to logs directory

pAndl('Program has started, the date is the {day} of {month}, {year}. the time is {time}'.format(day=now.strftime('%d'),month=now.strftime('%B'),year=now.strftime('%Y'),time=now.strftime('%X')))
pAndl()# Prints whitespace for readability