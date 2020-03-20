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

blackJackOne = Table.Table("BJ", True, 1, 1, employee_List)

for i in range(len(blackJackOne.dealerName)):
    print(blackJackOne.dealerName[i].name, blackJackOne.dealerName[i].endTime)



def canDeal(parEmployeeList):
    for i in range(len(parEmployeeList)):
        if 'BJ' in parEmployeeList[i].gamesKnown:
            return parEmployeeList[i].name


blackJackTwo = Table.Table("BJ", True, 1, 1, canDeal(employee_List))

print(blackJackTwo.dealerName)