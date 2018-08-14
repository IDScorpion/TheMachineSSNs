##The Machine SSN Generator by u/id_scorpion##
import sqlite3 as lite
import os
import random

homeFile = 'TheMachine\\names_numbers.db'#included in zip
homeDirectory = 'TheMachine\\'

if os.path.exists(homeDirectory) is False: #Checks to see if path exists; if it doesn't it is then created
    print('Done')
    os.mkdir(homeDirectory)

con = lite.connect(homeFile) #connection to database
names = []
def generateNumber(): #Generates social security numbers
    global field_one
    field_one = random.randint(100,999)
    global field_two
    field_two = random.randint(10,99)
    global field_three
    field_three = random.randint(1000, 9999)
    return '{0}-{1}-{2}'.format(field_one, field_two, field_three)
def generateName():#pulls names from Names_SSNs
    with con:
        cur = con.cursor()
        search = cur.execute("SELECT * FROM Names_SSNs")
        for row in search:
            names.append(row[0])#adds all names to list

def addSSN(name):#Ties a  SSN to a name in the names_and_ssns table
    with con:
        cur = con.cursor()
        ssn = generateNumber()
        cur.execute('insert into names_and_ssns values("{0}","{1}")'.format(name,ssn))

generateName()#runs the generateName function
ssns = []#sets list to blank
with con:
    cur = con.cursor()
    try:#checks if table exists just to be safe
        cur.execute("CREATE TABLE names_and_ssns(Name TEXT, field2 TEXT)")
    except lite.OperationalError:
        pass#needed syntax
    search = cur.execute("SELECT * FROM names_and_ssns")
    for row in search:
        ssns.append(row)#appends results from search; allows program to know if SSNs have been added already
if not ssns:#checks if its blank
    for item in names:
        addSSN(item)#if list is blank ties a random SSN to every name
def irrelevantProtocol():#main protocol
    print('Irrelevant protocol running.')#provides confirmation program is still running :)
    while True:
        ssn = generateNumber()#runs generateNumber and saves the return as sss
        with con:
            cur = con.cursor()
            search = cur.execute('SELECT * from names_and_ssns where field2 like "{0}"'.format(ssn))#checks for SSN
            for row in search:
                if row:#if anything is returned print
                    namenumber ='{0} - {1}'.format(row[0], row[1])#formats namenumber variable
                    print('Number identified: {0}'.format(namenumber))#print
irrelevantProtocol()#runs Irrelevant Protocol
