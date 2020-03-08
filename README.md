This repository is home to my 2nd year, 2nd TB project for my Cyber Security & Digital Forensics module.


Convert.py takes a load of EVTX files and converts them into XML files for parsing

Analyze.py takes those XML files and parses them for Event IDs and returns two dictionaries(matched event IDs and unmatched but present event IDs) and creates a JSON object for ease of access to those dictionaries and their values

Visualize.py will take that JSON object and create a two visualizations - One of matched event IDs and one for unmatched event IDs - and create a PDF file of the events, their prevalence, and a short representation of each event.


