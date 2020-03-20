import csv
import Person
import Table


employee_List = []

with open('schedule.csv', 'r') as Schedule:
    reader = csv.reader(Schedule)
    for row in reader:
        employee_List.append(Person.Person(row[0],row[1],row[2],row[3]))

table_List = []

with open('gameList.csv', 'r') as GameList:
    reader = csv.reader(GameList)
    for row in reader:
        table_List.append(Table.Table(row[0], row[1]))

def assignDealer(parTableList, parEmployeeList):
    for i in range(len(parTableList)):
        for x in range(len(parEmployeeList)):
            if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                parTableList[i].dealerName = parEmployeeList[x].name
                parTableList[i].dealerOut = parEmployeeList[x].endTime
                parEmployeeList[x] = Person.Person()
                break
            else:
                pass


myOutList = table_List

myNextEmployee = employee_List


def click(nextEmployee, outList):

    for i in range(len(nextEmployee)):
        for x in range(len(outList)):
            if int(nextEmployee[i].startTime) >= int(outList[x].dealerOut):
                if (int(nextEmployee[i].startTime) - int(outList[x].dealerOut)) >= 100:
                    assignDealer(outList, nextEmployee)
                    nextEmployee[i] = Person.Person()

                    break
                else:
                    break

            else:
                break


def displayTable():
    print("")
    print("")
    for i in range(len(table_List)):
        print(table_List[i])
    print("")
    print("")


assignDealer(table_List, employee_List)

displayTable()

click(myNextEmployee,myOutList)

displayTable()

click(myNextEmployee,myOutList)

displayTable()

click(myNextEmployee,myOutList)

displayTable()

click(myNextEmployee,myOutList)

displayTable()
