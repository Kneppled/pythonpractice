import pyodbc
# https://github.com/mkleehammer/pyodbc
import csv



# simple to class to extract list that could be copied and pasted.
class athleteInfo(object):
    def __init__(self, First, Last):
        self.First = First
        self.Last = Last

    def printRoster(self):
        print(athletes.First, athletes.Last)

# uses pyodbc class to connect to the installed driver through my computer
# and the direct path of the file that i am looking to access
conn = pyodbc.connect (r'DRIVER={Microsoft Access Driver (*.mdb)};server=localhost;DBQ=C:\Users\Dan\Documents\csc505\AccessProject\TeamData.mdb;UID=me;PWD=pass')
#cursor allows me to select columns or rows to be iterated
cur = conn.cursor()
# * is the entire column that is labeled below
cur.execute('select * from Athlete')
print('2018-2019 Naugatuck Swimming and Diving Roster')

listRow = []
# create destination file
newFile = ("TeamRoster.csv")
with open(newFile,'w', newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    # set up iterative loop after the csv file is opened to write in
    for row in cur.execute('select inactive, First, Last, Class, Sex, Birth, Age from Athlete'):
        # swimmers that are inactive are labeled -1, active 0
        if row.inactive == 0:
            # label each iteration into seperate variables
            firstName = row.First
            lastName = row.Last
            Grade = row.Class
            Gender = row.Sex
            Birthday = row.Birth
            Age = row.Age
            # call class to print roster to shell
            athletes = athleteInfo(firstName,lastName)
            athletes.printRoster()
            # append each variable to list
            listRow.append(firstName)
            listRow.append(lastName)
            listRow.append(Grade)
            listRow.append(Gender)
            listRow.append(Birthday)
            listRow.append(Age)
            #  write list in excel file
            csvWriter.writerow(listRow)
            # clear row for next loop
            listRow.clear()



