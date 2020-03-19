import csv
import Person

employee_List = []


with open('schedule.csv', 'r') as Schedule:
    reader = csv.reader(Schedule)
    for row in reader:
        employee_List.append(Person.Person(row[0],row[1],row[2]))
print(employee_List)