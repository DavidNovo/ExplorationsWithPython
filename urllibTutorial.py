__author__ = 'dnovogrodsky'

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