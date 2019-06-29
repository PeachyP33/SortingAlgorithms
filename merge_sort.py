#sorting function

def mergesort(list1, list2):    #define parameter
    mergeList = []
    counter1 = 0
    counter2 = 0
    #print('Inside merSort ...')
    #print(list1)
    #print(list2)

    while (counter1 < len(list1)) and (counter2 < len(list2)):
        if list1[counter1] > list2[counter2]:
            mergeList = mergeList + [list2[counter2]]
            counter2 = counter2 + 1
        else:
            mergeList = mergeList + [list1[counter1]]
            counter1 = counter1 + 1
        
    #print(list1)
    #print(list2)
    #print(mergeList)

    #print('Counter1: ' + str(counter1))
    #print('Counter2: ' + str(counter2))

    #add in leftover numbers
    while counter1 < len(list1):
        mergeList = mergeList + [list1[counter1]]
        counter1 = counter1 + 1

    while counter2 < len(list2):
        mergeList = mergeList + [list2[counter2]]
        counter2 = counter2 + 1

    #print(mergeList)
    #print('Before return ...')    
    return mergeList



#read data from file and put data in list. Display number of elements
fileList = []
with open('/Users/Pracheeti/Documents/Python/file_numbers_list.txt', 'r') as f:
    for line in f:
        fileList = fileList + [int(line)]
        
f.close()
print(fileList)
#print(fileList[3])
print('Your data set has ' + str(len(fileList)) + ' elements.')
values = len(fileList)


#find out number of iterations needed for quantity of elements
import math
iteration = math.log(len(fileList), 2)
iterationCounter = math.ceil(iteration)
print(math.ceil(iteration)) #round up alaways
iterationNum = math.ceil(iteration)

#iterations

#combine and sort two lists
#print('Test mergeSort ...')
#listA = [9, 28, 73, 92]
#listB = [-7, 532]
#sortList = mergesort(listA, listB)
#print(sortList)
#print('Test mergeSort End ...')

iteration = 1
offset = 1
while iteration <= iterationNum:
    #print('Iteration count: ' + str(iteration) + '. Data at the srart ...')
    #print(fileList)
    i = 0
    while i < len(fileList):
        tmp = i + offset
        mgrLst = mergesort(fileList[i:tmp], fileList[tmp:tmp+offset])
        fileList[i:tmp+offset] = mgrLst
        i = tmp+offset
    iteration = iteration + 1
    offset = offset * 2
        
print(fileList)



