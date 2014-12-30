__author__ = 'dnovogrodsky'
import re
machineName = re.compile('(deflogix-pc.def-logix.local)')

inputSyslogMessages = open('messages','r')
outputSyslogMessages = open('syslogMessages.txt', 'w')

# read the input syslog line by line
for line in inputSyslogMessages:
    # testing
    print(line)
    # check for matching the machine name in question
    match = re.match(machineName, line)
    if match:
        # if there is a match, write line to new file
        outputSyslogMessages.write(line)
        # testing stuff
        ## this prints the string 'Hello'
        print(match.string)
        ## this prints the regular exzpression passed to the match() method
        print(match.re)

# at end of all lines close file
inputSyslogMessages.close()
outputSyslogMessages.close()



