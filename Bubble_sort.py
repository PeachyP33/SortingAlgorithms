#bubble sort!!!!

print('How many numbers will you enter?')
values = input()

myList = []
counter = 0

while counter < int(values):
    print('Please enter your ' + str(counter + 1) + 'the element: ')
    myList = myList + [int(input())]
    counter = counter + 1

print('Here is your list:')
print(myList)
#myList.sort()
#print(myList)
    
#( myList : of sortable items )
print('Here is your numerically sorted list:')

counter2 = 0
compareCount = 0
while counter2 < (int(values) - 1):
    counter = 0
    swapCount = 0
    while counter < (int(values) - 1):
        compareCount = compareCount + 1
        if myList[counter] > myList[counter + 1]:
            tmpValue = myList[counter]
            myList[counter] = myList[counter + 1]
            myList[counter + 1] = tmpValue
            swapCount = swapCount + 1
        counter = counter + 1
    if swapCount == 0:
        break
    counter2 = counter2 + 1
    

print(myList)
print(compareCount)


        
