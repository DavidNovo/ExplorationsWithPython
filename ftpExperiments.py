__author__ = 'davidnovogrodsky_wrk'
from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')

ftp.cwd('/specific domain or location/location of files/')

# getting a file
def grabFile:
    #name off file we want to grab
    fileName= 'fileName.txt'
    # opening a local file
    localfile = open(fileName, 'wb')
    # retrieve a file
    ftp.retrbinary('RETR ' + fileName, localfile.write,
                   1024)
    ftp.quit()
    localfile.close()

#send a file to remote server
def placeFile():
    #define local file to send
    fileName= 'nameoflocalffile.txt'
    # use ftp commands to send file
    # open remote file
    ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))
    # close ftp connection
    ftp.quit()
    # close local file


