# https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ

#while True:
#    print("Hello world")

#for loop
exampleList = [1,4,3,2,4,65,3]
for eachNumber in exampleList:
    print(eachNumber)

for x in range(1,11):
    print(x)


x = 51
y = 8
if x > y:
    print("X is greater than Y")

#user defined range
z = 10
if z in range(y,x):
    print("Z is between Y and X")
else:
    print("Z is not between Y and X")

# if...else...elif else
x = 5
y = 10
z = 22
if x > y:
    print('X is greater than Y')
elif x < z:
    print('X is less than Z')
# this will not be run because the previous condition is met
elif 2 < 5:
    print('2 is less than 5')
else:
    print('if and elif(s) never ran')
print('/n/n/n')


#
# defining a function
print('\n\n')
def example():
    print('start of block')
    # note the indent

#calling the function
example()

def simple_addition(num1,num2):
    int(num1)
    int(num2)
    answer = num1 + num2
    print(answer)

simple_addition(3,4)


#assigning default
def simple_addition(num1,num2=3):
    int(num1)
    int(num2)
    answer = num1 + num2
    print(answer)

simple_addition(4)

# now some primitive type checking
def simple_addition(num1,num2):
    try:
        val1 = int(num1)
        val2 = int(num2)
        answer = num1 + num2
        print(answer)
    except ValueError:
        print("the input must be numbers")

simple_addition('a',4)


#global and local variables
x = 6
def example():
    #without this, get an unbounded error
    # with global, can access and change
    global x
    z = 5
    print(z)
    print(x)
    x = x +1
example()

# writing to file
# two methods: writing and appending
# writing overwrites the contents
# append adds to the file
text = 'Sample text to save \nA New line!'
saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()

# now we append to a file
appendMe = '\nNew bit of information'
appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()

#reading from a file
## reads the entire file at once
readMe = open('exampleFile.txt','r').read()
print(readMe)

## reads the file at one line at a time and
## stores results in a Python list
readMe = open('exampleFile.txt','r').readlines()
print(readMe)

# first class
class Calculator:
    def addition(x,y):
        added = x + y
        print(added)
    def substraction(x,y):
        sub = x-y
        print(sub)


Calculator.addition(3,4)


# FAQ of Python

# tells Linux where python executable is
# not needed for Windows
#!/usr/bin/python

# import suporting scripts
## import eppicscript
#not to call something from the script
## epicscript.epic()

# getting user input, video 22
x = input('What is your name? ')
print('Hello', x)

# basic math and module statistics module
# comes with Python 3
import statistics
from statistics import variance
example_list = [1,3,4,5,76,88,76,54,3,3,3,4]
x = statistics.mean(example_list)
print(x)
y = variance(example_list)
print(y)

# making modules
## a module is a script
## rules to make a module is the same as a script
## infact, a module is a Python script
## note that the script needs to be in one of the checked paths
## say /usr/local/Python/lib/site-packages...

# lists and tuples
### tuple is immutable
### list is mutable
x = 5,6,2,6  # is a tuple
x2 = (5,6,2,6) #is a tuple

### here are lists
y = [5,6,2,6]
y2 = [3,22,65,7]


# list manipulations
q = [6,44,3,6,78,65,3,45,4]
q.append(10)
print(q)

### insert data into index=2 spot in list
q.insert(2,101)
print(q)

### remove data, by index number
q.remove(q[2])
print(q)

### get a slice
### includes first element, excludes last element
### index of 5, index of 6, stops at index of 7
print(q[5:7])

### negative numbers for index starting the end of the list
print(q[-1])

### find number of elements of a certain value in a list
print(q.count(4))

# multi-dimensional lists
r = [[5,4,3],[3,2,3],[3,2,3]]
print(r)
### getting specific elements
print(r[1])
### prints 3
print(r[1][0])


# reading from a CSV spreadsheet, lesson 29
# comma seperated variables
import csv
with open('testData.txt') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    #the following print statement produces <_csv.reader object at 0x0369EDF0>
    # address of the object
    #print(readCSV)

    dates = []
    colors = []
    for row in readCSV:
        # this prints out the rows, the rows
        # become lists ['1/21/2014', '4', '5', '6', 'red']
        print(row)
        print(row[0]) #index of 0

        color = row[4]
        date = row[0]
        dates.append(date)
        colors.append(color)
        print(colors)
        print(dates)
whatColor = input('What color do you wish to know the date of?')

colorIndex = colors.index(whatColor.lower())
theDate = dates[colorIndex]
print('The date of ', whatColor,' is ', theDate)

# error handling
import csv
with open('testData.txt') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    #the following print statement produces <_csv.reader object at 0x0369EDF0>
    # address of the object
    #print(readCSV)

    dates = []
    colors = []
    for row in readCSV:
        # this prints out the rows, the rows
        # become lists ['1/21/2014', '4', '5', '6', 'red']
        print(row)
        print(row[0]) #index of 0

        color = row[4]
        date = row[0]
        dates.append(date)
        colors.append(color)
        print(colors)
        print(dates)
    try:
        whatColor = input('What color do you wish to know the date of?')
        colorIndex = colors.index(whatColor.lower())
        theDate = dates[colorIndex]
        print('The date of ', whatColor,' is ', theDate)
    except Exception as e:
        print(e)
    print('continue')


# multi line print
print('''

 This is a multi line print
 This fo for ASCII designs

''')

# dictionaries
### unordered assortment of data
### key-value pairs
exDict = {'Jack':15, "Bob":21, 'Alice':12}
print(exDict)
### how old is Jack?
print(exDict['Jack'])
### add elements to dictionary
exDict['Tim'] = 14
print(exDict)
### the key is always kept unique
## the value is overwritten
exDict['Tim'] = 17
print(exDict)
### remove a pair
del exDict['Tim']
print(exDict)
### the values can be values..
## the value becomes and array of values
exDict2 = {'Jack':[15,'blonde'], "Bob":[21,'brown'], 'Alice':[12,'red']}
print(exDict2['Jack'][1])


# built-in functions
### for a full list go here: https://docs.python.org/3/library/functions.html
### to get help type help() at the python prompt
### like man pages
###
### math is a built in function
### math.<name of function>
###
### type casting
intMe = 55
print(float(intMe))


# OS module, lesson 35
import os
currentDir = os.getcwd()
print(currentDir)
### make new directory in current working directory
### note if the directory already exists there will be an error
#os.mkdir('newdirectoruy')
os.rename('newdirectoruy','newDirectory02')

# sys module
### command line stuff
### remember some OS have different command line commands
### using this module makes your script
### OS dependent
import sys
sys.stderr.write('a test for err')
sys.stderr.flush()
sys.stdout.write('\nthis is the standard out\n')

### arg
### all the arguments we pass to python
### when making scrpts, this is very important
### scriptName.py <arg0> <arg1>
import sys
print(sys.argv)
if (len(sys.argv)) > 1:
    print(sys.argv[1])

# lesson 36, module urllib
### accessing the Internet
import urllib.request
#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())
### the result of this script retrieves the source HTML
##
##
### now a post request
import urllib.parse
url = 'http://pythonprogramming.net'
### values to append to the end of URL
values = {'s':'basic',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
### makeing the request
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
responseData = response.read()
print(responseData)
##
##
## trying to access a URL as a Python bot
## note the exception
try:
    y = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(y.read())
except Exception as e:
    print(str(e))

## accessing a URL as a web browser
## this time no exception
try:
    y2 = 'https://www.google.com/search?q=test'
    # contains info on my browser
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) " \
                            "Chrome/24.0.1312.27 Safari/537.17"
    request2 = urllib.request.Request(y2, headers = headers)
    response2 = urllib.request.urlopen(request2)
    response2Data = response2.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(response2Data))
    saveFile.close()
except Exception as e:
    print(str(e))

# lesson 37, re or regular expressions
import re
p = re.compile('(H)')
test_str = "HELLO"

print(re.search(p, test_str))
match = re.match(p, test_str)
print(match)
if match:
    # this prints the string 'Hello'
    print(match.string)
    # this prints the regular exzpression passed to the match() method
    print(match.re)
####
import re
p2 = re.compile('(\w)+')
test_str = "HELLO"

match2 = re.search(p2, test_str)
print(match2)