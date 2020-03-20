import csv
import Person
import Table

employee_List = []

with open('schedule.csv', 'r') as Schedule:
    reader = csv.reader(Schedule)
    for row in reader:
        employee_List.append(Person.Person(row[0], row[1], row[2], row[3]))


# for i in range(len(employee_List)):
#    print(employee_List[i])


# blackJackOne = Table.Table("BJ", True, 1, 1, employee_List)

# for i in range(len(blackJackOne.dealerName)):
#    print(blackJackOne.dealerName[i].name, blackJackOne.dealerName[i].endTime)


#def canDeal(employee_List):
#    for i in range(len(employee_List)):
#        if 'BJ' in employee_List[i].gamesKnown:
#            return employee_List[i].name


table_List = []

with open('gameList.csv', 'r') as GameList:
    reader = csv.reader(GameList)
    for row in reader:
        table_List.append(Table.Table(row[0], row[1]))


# for i in range(len(table_List)):
# print(table_List[i])

def assignDealer(table_List, employee_List):
    for i in range(len(table_List)):
        for x in range(len(employee_List)):
            if table_List[i].gameCode in employee_List[x].gamesKnown:
                table_List[i].dealerName = employee_List[x].name
                employee_List[x] = Person.Person()
                break
            else:
                pass


# assignDealer(table_List, employee_List)

# for i in range(len(table_List)):
#    pass
#    print(table_List[i])

# for i in range(len(employee_List)):
#    pass
#    print(employee_List[i])

print('remaining employees')


# for i in range(len(employee_List)):
#    pass
# print(employee_List[i])


# outList = employee_List
# nextEmployee = assignList
# employee_List_two = employee_List.copy()

def click():
    for i in range(len(employee_List)):
        for x in range(len(employee_List)):
            if int(employee_List[i].startTime) == int(employee_List[x].endTime):
                # print(employee_List[x])
                # print(employee_List[i])
                assignDealer(table_List, employee_List)
                employee_List[x] = employee_List[i]
                employee_List[i] = Person.Person()
            break

        else:
            pass


click()
print("")
print("")
for i in range(len(table_List)):
    print(table_List[i])
click()
print("")
print("")
for i in range(len(table_List)):
    print(table_List[i])
click()
print("")
print("")
for i in range(len(table_List)):
    print(table_List[i])
