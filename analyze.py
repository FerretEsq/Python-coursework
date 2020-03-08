import os, fnmatch, time, json
from datetime import datetime

def pAndl(arg=''):
    print(arg)
    log.write(arg+'\n')
    # Simple function to print and write to a log

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

directories=os.scandir(bsdst+'evtx_logs') # Directories to work with

counter1=0 # File counter
counter2=0 # Total event IDs
counter3=0 # Matched IDs

eventsToMatch={1102:0,4611:0,4624:0,4634:0,4648:0,
               4661:0,4662:0,4663:0,4672:0,4673:0,
               4688:0,4698:0,4699:0,4702:0,4703:0,
               4719:0,4732:0,4738:0,4742:0,4776:0,
               4798:0,4799:0,4985:0,5136:0,5140:0,
               5142:0,5145:0,5156:0,5158:0} # Dictionary of Event IDs, initialized with all 0 values
            
eventsNotMatched={} # Dictionary of unmatched events 

for directory in directories:
    pAndl('Working on "{0}" directory:'.format(directory.name.replace('_',' '))) 
    with os.scandir(directory) as vessel: 
        for item in vessel:
            if fnmatch.fnmatch(item,'*.xml'):
                counter1+=1
                with open(item) as fileToParse:
                        for line in fileToParse: # Iterates over the lines in the file
                            if line.startswith('<EventID'): # Find eventID by start of EventID line 
                                numEvent=int(line[line.find('>')+1:line.find('</')]) # Grab just the ID num with find function
                                pAndl('An event ID:{0} found in file {1}'.format(numEvent,item.name))
                                counter2+=1
                                if numEvent in eventsToMatch:
                                    pAndl('Event ID {0} matched'.format(numEvent))
                                    pAndl()
                                    eventsToMatch[numEvent]+=1
                                    counter3+=1
                                    # If event is matched, print and increment dictionary key value
                                elif numEvent not in eventsToMatch and numEvent not in eventsNotMatched:
                                    eventsNotMatched[numEvent]=1
                                    pAndl('Event {0} not matched'.format(numEvent))
                                    pAndl()
                                    # If event is not present in either dictionaries, create a new dict entry in eventsNotMatched dict
                                else:
                                    pAndl('Event {0} not matched'.format(numEvent))
                                    pAndl()
                                    eventsNotMatched[numEvent]+=1
                                    # If event present in eventsNotMatched, print and increment eventNotMatched event key value
    pAndl()

# Create JSON file consisting of a list of dictionaries(index 0 being matched events, and index 1 being unmatched) to play around with in visualise.py
jsonLogName='JSON_Analyze_{ts}'.format(ts=now)
with open(jsonLogName,'w+') as jsonFile:
    json.dump((eventsToMatch,eventsNotMatched),jsonFile)
os.system(command='mv "{log}" {logsdir}'.format(log=jsonLogName,logsdir=logsdir)) # Move file to logs directory

# Prints matched events
pAndl('The events that were matched are:')
for eventId in eventsToMatch.keys():
    pAndl('Event {id}; matched {num} times.'.format(id=eventId,num=eventsToMatch[eventId]))
pAndl()

#Prints unmached events
pAndl('Events that were recorded but not matched are:')
for eventId in eventsNotMatched.keys():
    pAndl('Event {id}; recorded {num} times.'.format(id=eventId,num=eventsNotMatched[eventId]))
pAndl()

pAndl('Finished parsing all the files!')
pAndl('The time is {time}'.format(time=now.strftime('%X')))
pAndl('Program finished in {0:.2f} seconds'.format(time.time()-start))
pAndl('Parsed {0} folders'.format(counter1))
pAndl('{0} Event IDs found'.format(counter2))
pAndl('{0} Event IDs matched'.format(counter3))
pAndl()

pAndl('Created JSON file under the name "{name}". Index 0 is the matched events dictionary; Index 1 is the unmatched events dictionary.'.format(name=jsonLogName))


log.close()