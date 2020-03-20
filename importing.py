import csv
import Person
import Table


employee_List = []

with open('schedule.csv', 'r') as Schedule:
    reader = csv.reader(Schedule)
    for row in reader:
        employee_List.append(Person.Person(row[0],row[1],row[2],row[3]))
for i in range(len(employee_List)):
    print(employee_List[i])

assignList = employee_List

blackJackOne = Table.Table("BJ", True, 1, 1, employee_List)

#for i in range(len(blackJackOne.dealerName)):
#    print(blackJackOne.dealerName[i].name, blackJackOne.dealerName[i].endTime)



def canDeal(parEmployeeList):
    for i in range(len(parEmployeeList)):
        if 'BJ' in parEmployeeList[i].gamesKnown:
            return parEmployeeList[i].name


table_List = []

with open('gameList.csv', 'r') as GameList:
    reader = csv.reader(GameList)
    for row in reader:
        table_List.append(Table.Table(row[0], row[1]))

for i in range(len(table_List)):
    print(table_List[i])

def assignDealer(parTableList, parEmployeeList):
    for i in range(len(parTableList)):
        for x in range(len(parEmployeeList)):
            if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                parTableList[i].dealerName = parEmployeeList[x].name
                parEmployeeList.pop(x)
                break
            else:
                pass

assignDealer(table_List, assignList)

for i in range(len(table_List)):
    print(table_List[i])
