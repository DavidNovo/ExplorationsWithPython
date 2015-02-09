__author__ = 'dnovogrodsky'
import re
import pathlib
import os
from subprocess import call

#machineName = re.compile('(deflogix-pc.def-logix.local)')
machineName = re.compile('(andre_sp3.def-logix.local)')

inputSyslogMessages = open('messages','r')
outputSyslogMessages = open('syslogMessages.txt', 'w')

# read the input syslog line by line
for line in inputSyslogMessages:
    # testing
    print(line)
    # check for matching the machine name in question
    searchResults = re.search(machineName, line)
    if searchResults:
        # if there is a match, write line to new file
        outputSyslogMessages.write(line)

# at end of all lines close file
inputSyslogMessages.close()
outputSyslogMessages.close()

# check that the file exists
input = pathlib.Path('syslogMessages.txt')

# run command line it ingest the file
if input.exists():
    # ingest file into Hadoop
    print("ready to ingest")
    # run this command on the command line
    ## sudo -u hdfs hadoop fs -copyFromLocal ~/Desktop/CDRecords.txt /user/cloudera/vector/callRecords/
    call("sudo -u hdfs hadoop fs -copyFromLocal syslogMessages.txt /user/cloudera/vector/callRecords/",
         shell=True)
    call("hadoop fs -copyFromLocal syslogMessages.txt /user/cloudera/vector/callRecords/",
         shell=True)
    os.system('sudo -u hdfs hadoop fs -copyFromLocal syslogMessages.txt /user/cloudera/vector/callRecords/')

# if there is no file print an error message
print('no file to ingest')
currentDirectory = os.getcwd()
print(currentDirectory)