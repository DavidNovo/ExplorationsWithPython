import random
import time
import datetime



#saveFile = open('importdata.json', 'a')
# creating timestamp for file names
timestr = time.strftime("%Y%m%d-%H%M%S")

# creating output files one for phone, Active Directory (events), and NMA
saveFileNMA = open('testDataNMA' + timestr + '.txt', 'a')
saveFilePBX = open('testDataPBX' + timestr + '.txt', 'a')
saveFileEvent = open('testDataEvents' + timestr + '.txt', 'a')
saveFileEmployee = open('testDataEmployee' + timestr + '.txt', 'a')

def riskcat():
    cat = ['L', 'M', 'H']
    return cat[(random.randrange(0, 3))]

def high():
    return str(random.randrange(90, 99))

def med():
    return str(random.randrange(70, 89))

def low():
    return str(random.randrange(1, 69))

options = {'H': high,
           'M': med,
           'L': low,
}

def username():
    first_name_seed = [
        'Ben',
        'Jim',
        'Sara',
        'Amber',
        'Amanda',
        'Jessica',
        'Jack',
        'Steve',
        'Greg',
        'Justin',
        'Travis',
        'David',
        'Lucy',
        'Madison',
        'Mike',
        'Jennifer',
        'Josie',
        'Chris',
        'Jason',
        'Crystal',
        'Alora',
        'Christine',
        'Samantha',
        'Mary',
        'Gaby',
        'Diego',
        'Adam',
        'Noel',
        'Yvone',
        'Kevin',
        'Cassandra',
        'Ryan',
        'Randy',
        'Robert',
        'Deann',
        'Xavier',
        'Dolores',
        'Terri',
        'Cindy',
        'Tricia',
        'Roger',
        'Rose',
        'Brian',
        'Caitlin',
        'Carolyn',
        'Dawna',
        'Don',
        'Douglas',
        'Fernando',
        'Gavin',
        'Jimmy',
        'Jodi',
        'Jolene',
        'Joseph',
        'Katy',
        'Kristina',
        'Leslie',
        'Lidia',
        'Lindsey',
        'Nick',
        'Nicole',
        'Patrick',
        'Raul',
        'Tommy',
        'Lauren',
        'Tony',
        'Valarie'
    ]
    last_name_seed = [
        'Brown',
        'Miranda',
        'Escobar',
        'Garza',
        'Garcia',
        'Galindo',
        'Wynn',
        'Donovan',
        'Morales',
        'Martinez',
        'Rodriguez',
        'Davis',
        'Davies',
        'Mello',
        'James',
        'Robinson',
        'Burns',
        'Wright',
        'Larson',
        'Gomez',
        'Alfaro',
        'Ramirez',
        'Foss',
        'Mullin',
        'Stout',
        'Medlock',
        'Nelson',
        'Mills',
        'Green',
        'Duncan',
        'Kidd',
        'Banda',
        'Lopez',
        'Queen',
        'Howard',
        'Perez',
        'Landers',
        'Johnson',
        'Jones',
        'Williams',
        'Tilson',
        'Wilson',
        'Harris',
        'White',
        'Martin',
        'Lee',
        'Lewis',
        'Walker',
        'Hall',
        'Allen',
        'Young',
        'Hernandez',
        'King',
        'Hill',
        'Scott',
        'Mitchell',
        'Roberts',
        'Phillips',
        'Campbell',
        'Reed',
        'Cook',
        'Bell',
        'Cooper'
    ]
    return ((first_name_seed[random.randrange(0, len(first_name_seed) - 1)])[:1]).lower() + (
        last_name_seed[random.randrange(0, len(last_name_seed) - 1)]).lower()

def createEmployeeEntry(pk):
#--------------------------------------------------------------------------------------
# This functions generates a list of employee records for the Employee table
# Desired output looks like this:
# {"fields": {"supervisor": 1, "trend": "N", "risk_category": "L", "on_watchlist": false, "risk_score": "8", "score_date": "2014-12-30", "user_name": "test"},"model": "employees.employee", "pk": 1},
# default supervisor for all employees

    level = riskcat()
#    print("{\"fields\": {\"supervisor\": 1, \"risk_category\": \"" + level + "\", \"on_watchlist\": false, \"risk_score\": \"" + options[level]() + "\", \"score_date\": \"" + str(datetime.date.today()) +"\", \"user_name\": \"" + username() + "\"}, \"model\": \"employees.employee\", \"pk\": " + str(pk) + "},")
    print("1" + "," + level + "," + "false" + "," + options[level]() + "," + str(datetime.date.today()) + "," + username() + "," + "employees.employee" +"," + str(pk) + "\n")
    returnString = "1" + "," + level + "," + "false" + "," + options[level]() + "," + str(datetime.date.today()) + "," + username() + "," + "employees.employee" +"," + str(pk) + "\n"
    return returnString

def duration():
    random_hour = str(random.randrange(0, 1))
    random_minute = str(random.randrange(0, 30))
    random_second = str(random.randrange(0, 59))

    if len(random_hour) == 2:
        elapsed_time = random_hour + ":"
    else:
        elapsed_time = "0" + random_hour + ":"

    if len(random_minute) == 2:
        elapsed_time = elapsed_time + random_minute + ":"
    else:
        elapsed_time = elapsed_time + "0" + random_minute + ":"

    if len(random_second) == 2:
        elapsed_time = elapsed_time + random_second
    else:
        elapsed_time = elapsed_time + "0" + random_second

    return elapsed_time

def random_time():
    random_hour = str(random.randrange(0, 23))
    random_minute = str(random.randrange(0, 59))
    random_second = str(random.randrange(0, 59))

    if len(random_hour) == 2:
        start_time = random_hour + ":"
    else:
        start_time = "0" + random_hour + ":"

    if len(random_minute) == 2:
        start_time = start_time + random_minute + ":"
    else:
        start_time = start_time + "0" + random_minute + ":"

    if len(random_second) == 2:
        start_time = start_time + random_second
    else:
        start_time = start_time + "0" + random_second

    return 'T' + start_time +'Z'

def random_date(makeRandom):
    if makeRandom == True:
        format = '%Y-%m-%d'
        start_date = time.strftime(format,
                         time.localtime(time.mktime(time.strptime("2014-01-01", format)) + random.random() * (
                             time.mktime(time.strptime("2015-01-01", format)) - time.mktime(
                                 time.strptime("2014-01-01", format)))))
        return start_date
    else:
        return str(datetime.date.today())

DEST = 'destPhones.txt'  #file containing a list of phone numbers

def pick_phone(filename):
    myline = ''
    myline = random.choice(open(filename).readlines())
    return myline.replace('\n', '')

def createCallLogEntry(source_phone_number, employee_id, pk):
#--------------------------------------------------------------------------------------
# This functions generates a list of fake outgoing calls using the employee's phone number and logs to the Call table
# Desired output looks like this:
# {"fields": {"employee": 1, "date_time_logged": "2014-12-31T17:46:04Z", "target_phone": "989-999-0012", "source_phone": "123-456-7890", "duration": "12:00"}, "model": "employees.call", "pk": 1},
#--------------------------------------------------------------------------------------

    destination_phone_number = pick_phone(DEST)
    print(str(employee_id) + "," + str(random_date(False)) + "," + str(random_time()) + "," + str(destination_phone_number) + "," + str(source_phone_number) + "," + str(duration()) )
#    print("{\"fields\": {\"employee\": " + str(employee_id) + ", \"date_time_logged\": \"" + random_date(False) + random_time() + "\", \"target_phone\": \"" + destination_phone_number + "\", \"source_phone\": \"" + source_phone_number + "\", \"duration\": \"" + duration() + "\"},\"model\": \"employees.call\", \"pk\":" + str(pk) + "},")
#    return "{\"fields\": {\"employee\": " + str(employee_id) + ", \"date_time_logged\": \"" + random_date(False) + random_time() + "\", \"target_phone\": \"" + destination_phone_number + "\", \"source_phone\": \"" + source_phone_number + "\", \"duration\": \"" + duration() + "\"},\"model\": \"employees.call\", \"pk\":" + str(pk) + "},"
    returnString = str(employee_id) + "," + str(random_date(False)) + "," + str(random_time()) + "," + str(destination_phone_number) + "," + str(source_phone_number) + "," + str(duration()) + "\n"
    return returnString

def createReceiveCallLogEntry(source_phone_number, employee_id, pk):
#--------------------------------------------------------------------------------------
# This functions generates a list of fake incoming calls using random phone numbers and logs to the Call table
# Desired output looks like this:
# {"fields": {"employee": 1, "date_time_logged": "2014-12-31T17:46:04Z", "target_phone": "989-999-0012", "source_phone": "123-456-7890", "duration": "12:00"}, "model": "employees.call", "pk": 1},
#--------------------------------------------------------------------------------------
    destination_phone_number = pick_phone(DEST)
#    print("{\"fields\": {\"employee\": " + str(employee_id) + ", \"date_time_logged\": \"" + random_date(False) + random_time() + "\", \"target_phone\": \"" + source_phone_number + "\", \"source_phone\": \"" + destination_phone_number + "\", \"duration\": \"" + duration() + "\"},\"model\": \"employees.call\", \"pk\":" + str(pk) + "},")
    print(str(employee_id) + "," + random_date(False) + random_time() + "," + source_phone_number + "," + destination_phone_number + "," + duration() + "," + str(pk) + "\n")

#    return "{\"fields\": {\"employee\": " + str(employee_id) + ", \"date_time_logged\": \"" + random_date(False) + random_time() + "\", \"target_phone\": \"" + source_phone_number + "\", \"source_phone\": \"" + destination_phone_number + "\", \"duration\": \"" + duration() + "\"},\"model\": \"employees.call\", \"pk\":" + str(pk) + "},"
    returnString = str(employee_id) + "," + random_date(False) + random_time() + "," + source_phone_number + "," + destination_phone_number + "," + duration() + "," + str(pk) + "\n"
    return returnString


def randIP():

    return str(random.randrange(0,255)) + "." + str(random.randrange(0,255)) + "." + str(random.randrange(0,255)) + "." + str(random.randrange(0,255))

def randDNS():
    pickList = ['microsoft.com', 'amazon.com', 'facebook.com', 'google.com', 'ebay.com', 'wikipedia.com', 'disa.mil', 'af.mil', 'badplace.com']
    return pickList[random.randrange(0,8)]

def randPort(type):
    if type == 'target':
        pickFrom = ['445', '22', '20','21', '23', '443' ]
        return pickFrom[random.randrange(0,5)]
    else:
        return str(random.randrange(24000,35000))

def createMonitorEntry(dns, employee, pk):
#--------------------------------------------------------------------------------------
# This functions generates a list of fake NMA logs for the Monitor table
# Desired output looks like this:
# {"fields": {"source_ip": "123.123.123.123", "date_logged": "2014-12-31", "target_ip": "090.09.0.90", "target_port": "890", "source_port": "123", "employee": 1, "type": "dns"}, "model": "employees.monitor", "pk": 1},

# sample NMA lines in syslog file
# Dec 30 09:04:46 andre_sp3.def-logix.local [] - - - - - - dns,statsfe2.update.microsoft.com
# Dec 30 09:04:46 andre_sp3.def-logix.local [] - - - - - - http,statsfe2.update.microsoft.com,Windows-Update-Agent/7.9.9600.17238 Client-Protocol/1.21,
# Dec 30 09:05:18 andre_sp3.def-logix.local [] - - - - - - 192.168.200.112,55019,192.230.64.4,443,1573
#--------------------------------------------------------------------------------------
    bytes_transmitted = random.randint(200,2000000)
    if (dns == 'yes'):
#        print("{\"fields\": {\"bytes_transmitted\": " + str(bytes_transmitted) + ",\"source_ip\": \"N/A\", \"date_logged\": \"" + random_date(False) + random_time() + "\", \"target_ip\": \"N/A\", \"target_port\": \"N/A\", \"source_port\": \"N/A\", \"employee\": " + str(employee) + ", \"type\": \"" + randDNS() + "\"}, \"model\": \"employees.monitor\", \"pk\": " + str(pk) + "},")
#        return "{\"fields\": {\"bytes_transmitted\": " + str(bytes_transmitted) + ",\"source_ip\": \"N/A\", \"date_logged\": \"" + random_date(False) + random_time() + "\", \"target_ip\": \"N/A\", \"target_port\": \"N/A\", \"source_port\": \"N/A\", \"employee\": " + str(employee) + ", \"type\": \"" + randDNS() + "\"}, \"model\": \"employees.monitor\", \"pk\": " + str(pk) + "},"
        print(str(bytes_transmitted) + "," + "N/A" + "," + random_date(False) + random_time() + "," + "N/A" + "," + "N/A" + "," + "N\A"  + "," + str(employee) + "," + randDNS() + "," + str(pk) + "\n")
        returnString = str(bytes_transmitted) + "," + "N/A" + "," + random_date(False) + random_time() + "," + "N/A" + "," + "N\A" + "," "N/A" + "," + str(employee) + "," + randDNS() + "," + str(pk) + "\n"
        return returnString
    else:
#        print("{\"fields\": {\"bytes_transmitted\": " + str(bytes_transmitted) + ",\"source_ip\": \"" + iPDict[employee] + "\", \"date_logged\": \"" + random_date(False) + random_time() + "\", \"target_ip\": \"" + randIP() + "\", \"target_port\": \"" + randPort('target') + "\", \"source_port\": \"" + randPort('source') + "\", \"employee\": " + str(employee) + ", \"type\": \"http\"}, \"model\": \"employees.monitor\", \"pk\": " + str(pk) + "},")
#        print( str(bytes_transmitted) + "," + iPDict[employee] + "," + random_date(False) + random_time() + "," + randIP() + "," +  randPort('target') + "," + randPort('source') + ",", + str(employee) + ", \"type\": \"http\"}, \"model\": \"employees.monitor\", \"pk\": " + str(pk) + "\n" )
        returnString = str(bytes_transmitted) + "," + iPDict[employee] + "," + random_date(False) + random_time() + "," + str(randIP()) + "," +  str(randPort('target')) + "," + randPort('source') + "," + str(employee) + ", \"type\": \"http\"}, \"model\": \"employees.monitor\", \"pk\": " + str(pk) + "\n"

        return returnString

def createWindowsEventEntry(employee, pk, event_type):
#--------------------------------------------------------------------------------------
# This function generates a list of fake active directory logs for the Events table
# Desired output looks like this:
# {"fields": {"employee": 1, "logged_date_time": "2014-12-31T17:46:42Z", "event_type": "Log on", "flagged_event": true}, "model": "employees.event", "pk": 1},
#--------------------------------------------------------------------------------------
    flagged_event = ['true', 'false']
    print("{\"fields\": {\"employee\":" + str(employee) + ", \"logged_date_time\": \"" + random_date(False)+random_time() + "\", \"event_type\": \"" + event_type + "\", \"flagged_event\": " + flagged_event[random.randint(0,1)] + "}, \"model\": \"employees.event\", \"pk\": " + str(pk) + "},")
    return "{\"fields\": {\"employee\":" + str(employee) + ", \"logged_date_time\": \"" + random_date(False)+random_time() + "\", \"event_type\": \"" + event_type + "\", \"flagged_event\": " + flagged_event[random.randint(0,1)] + "}, \"model\": \"employees.event\", \"pk\": " + str(pk) + "},"

#--------------------------------------------------------------------------------------
# populate employees table
# initialize employeeList to be used in building calls, events, and monitors
#--------------------------------------------------------------------------------------

employeeList = []

for pk in range(1, 101):
    saveFileEmployee.write(createEmployeeEntry(pk))
    employeeList.append(pk)

print("Employee List Created!")

#--------------------------------------------------------------------------------------
# populate Call table
#--------------------------------------------------------------------------------------
ePhoneDict = {}

# create phone dictionary 'employee id':'phone number'
for employee in employeeList:
    phone = [str(random.randrange(200, 999)), str(random.randrange(100, 999)), str(random.randrange(1111, 9999))]
    strPhone = ' '.join(phone)
    ePhoneDict[employee] = strPhone

# verify dictionary was correctly built; for debug only
# print(ePhoneDict)

pk = 1
for employee in employeeList:
    for call in range(1,11):
        saveFilePBX.write(createCallLogEntry(ePhoneDict[employee], employee, pk))
        print(pk, call)
        pk += 1
        saveFilePBX.write(createReceiveCallLogEntry(ePhoneDict[employee], employee, pk))
        print(pk, call)
        pk += 1

print("Call Logs Completed!")

#--------------------------------------------------------------------------------------
# populate Monitor table
#--------------------------------------------------------------------------------------
iPDict = {}

# create IP address dictionary 'employee id':'IP'
for employee in employeeList:
    ip = "192.168.200." + str(employee + 20)
    iPDict[employee] = ip

pk = 1
is_DNS = ['yes','no']
for employee in employeeList:
    for entry in range(1,100):
        saveFileNMA.write(createMonitorEntry(is_DNS[random.randrange(0,2)],employee, pk))
        print(pk, entry)
        pk += 1

print("NMA Process Completed!")

#--------------------------------------------------------------------------------------
# populate Event table
#--------------------------------------------------------------------------------------
pk = 1
for employee in employeeList:
    for loop in range(1,11):
        #generate AD logon entry (limit date/time window to a single day)
        saveFileEvent.write(createWindowsEventEntry(employee, pk, "Logon"))
        pk += 1
        #generate AD logoff entry (limit date/time window to a single day)
        saveFileEvent.write(createWindowsEventEntry(employee, pk, "Logoff"))
        pk += 1
        #randomly create an unsuccessful logon event (1 in 50 chance)
        isUnsuccesfulLogon = random.randint(1,50)
        if isUnsuccesfulLogon == 5:
            #generate unsuccessful logon entry (limit date/time window to a single day)
            saveFileEvent.write(createWindowsEventEntry(employee, pk, "Unsuccessful Logon"))
            pk += 1
        print(pk,employee )


print("Event Process Completed!")

#--------------------------------------------------------------------------------------

saveFileNMA.close()
saveFileEmployee.close()
saveFileEvent.close()
saveFilePBX.close()
