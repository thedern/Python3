#!/usr/bin/python2.7

"""
parses cybersource logs checking for date/time, ID,
and result of each transaction

Note: Date, ID, and Decision are all on seperate but continuous
lines in the log file

"""
import re
import sys
from sys import argv
counter = 0
acceptCounter = 0
rejectCounter = 0
reviewCounter = 0

global date
Path = '/optware/IBM/WebSphere/V7/AppServer/profiles/cve/logs/'

if len(argv) < 2:
    print("usage is: 'cybsDecision.py' 'cybersource logfile name'")
    sys.exit()

script, cybsLog = argv
logFile = Path+cybsLog
#print(logFile)

fhandle = open(logFile)
for line in fhandle:
    #remove whitespace, etc
    line = line.rstrip()
    #print(line)

    #find date/time
    if 'REPLY' in line:
        date = re.findall(r'\b\d{4}-\d\d?-\d\d? \d\d?:\d\d?:\d\d?.\d\d\d', line)

    #find requestID
    if '<c:requestID>' in line:
        id = re.findall('[0-9]*[0-9]', line)

    #find decision
    if '<c:decision>' in line:
        status = re.findall('[A-Z].*[A-Z]', line)

        #print here before next loop else lose variable scope
        print(date, id, status)
        print('\n')

        if 'ACCEPT' in status:
            acceptCounter += 1

        elif 'REJECT' in status:
            rejectCounter += 1

        elif 'REVIEW' in status:
            reviewCounter += 1

        counter += 1


print('\nNumber of transactions {}'.format(counter))
print('\nNumber of ACCEPT {}'.format(acceptCounter))
print('\nNumber of REJECT {}'.format(rejectCounter))
print('\nNumber of REVIEW {}'.format(reviewCounter))
