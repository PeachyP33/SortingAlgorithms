#sort numbers using new method (selection sort)

print('Hello! How many numbers will you enter?')
myValue = int(input())

myList = []
counter = 0
#Reading the input: Give ceratin numeric values
while counter < myValue:
    print('Please enter value ' + str(counter + 1))
    myList = myList + [int(input())]
    counter = counter + 1

#Print input list
print('Here is your list')
print(myList)

#starting sorting
counter1 = 0
while counter1 < myValue:
    counter2 = counter1 + 1
    var1 = myList[counter1] 
    while counter2 < myValue:
        if myList[counter2] < var1:
            tmpVariable = myList[counter2]
            myList[counter2] = var1
            var1 = tmpVariable
        counter2 = counter2 + 1
    myList[counter1] = var1
    counter1 = counter1 + 1
    
#print sorted list
print('Here is your numerically sorted list:')
print(myList)
