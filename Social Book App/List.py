myList = [['1', '2', '3'], ['4', '5', '6']]
with open('AllUserRecords.txt', 'w') as file:
    for row in myList:
        file.write(';'.join(row))
        file.write('\n')
        myList2 = list()
with open('AllUserRecords.txt', 'r') as file:
    for row in file.read().splitlines():
        myList2.append(row.split(';'))