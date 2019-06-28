
#functions

import time

#merge sort:

#within Mergesort function1
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

#merge sort body:

def mergesortprogram(fileList):
    
    values = len(fileList)


    #find out number of iterations needed for quantity of elements
    import math
    iteration = math.log(len(fileList), 2)
    iterationCounter = math.ceil(iteration)
    #print(math.ceil(iteration)) #round up alaways
    iterationNum = math.ceil(iteration)
    
        #iterations
    iteration = 1
    offset = 1
    while iteration <= iterationNum:
        i = 0
        while i < len(fileList):
            tmp = i + offset
            mgrLst = mergesort(fileList[i:tmp], fileList[tmp:tmp+offset])
            fileList[i:tmp+offset] = mgrLst
            i = tmp+offset
        iteration = iteration + 1
        offset = offset * 2
        
    return(fileList)


#Bubble sort:
def bubblesort(myList):
    
    counter = 0

    counter2 = 0
    compareCount = 0
    while counter2 < (int(len(myList)) - 1):
        counter = 0
        swapCount = 0
        while counter < (int(len(myList)) - 1):
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
    
    return(myList)

#selection sort
def selectionsort(myList):
    
    counter = 0

    #starting sorting
    counter1 = 0
    while counter1 < len(myList):
        counter2 = counter1 + 1
        var1 = myList[counter1] 
        while counter2 < len(myList):
            if myList[counter2] < var1:
                tmpVariable = myList[counter2]
                myList[counter2] = var1
                var1 = tmpVariable
            counter2 = counter2 + 1
        myList[counter1] = var1
        counter1 = counter1 + 1
    

    return(myList)

#bucket sort

#bucketsort function 1:

def bucketsort(maxim, minim):
    import math
    rangeNum = maxim - minim
    bucketNum = math.ceil(rangeNum / 5) + 1
    bucket1 = []
    bucket2 = []
    bucket3 = []
    bucket4 = []
    bucket5 = []
    bucket1 = range(minim, minim + bucketNum)
    bucket2 = range(bucketNum + 1, bucketNum + 1 + bucketNum)
    bucketNum2 = bucketNum + 1 + bucketNum
    bucket3 = range(bucketNum2 + 1, bucketNum2 + 1 + bucketNum)
    bucketNum3 = bucketNum2 + 1 + bucketNum
    bucket4 = range(bucketNum3 + 1, bucketNum3 + 1 + bucketNum)
    bucketNum4 = bucketNum3 + 1 + bucketNum
    bucket5 = range(bucketNum4 + 1, bucketNum4 + 1 + bucketNum)
    
    return (min(bucket1), max(bucket1), min(bucket2), max(bucket2), min(bucket3))


#bucketsort body
def bucketsortprogram(fileList):

           
    rangeNum = (max(fileList) - min(fileList))
    maximum = max(fileList)
    minimum = (min(fileList))
    hello = bucketsort(maximum, minimum)
    

    #reidentify
    import math
    bucketNum = math.ceil(rangeNum / 5) + 1

    bucket1 = []
    bucket2 = []
    bucket3 = []
    bucket4 = []
    bucket5 = []
    bucket1 = range(minimum, minimum + bucketNum)
    bucket2 = range(bucketNum + 1, bucketNum + 1 + bucketNum)
    bucketNum2 = bucketNum + 1 + bucketNum
    bucket3 = range(bucketNum2 + 1, bucketNum2 + 1 + bucketNum)
    bucketNum3 = bucketNum2 + 1 + bucketNum
    bucket4 = range(bucketNum3 + 1, bucketNum3 + 1 + bucketNum)
    bucketNum4 = bucketNum3 + 1 + bucketNum
    bucket5 = range(bucketNum4 + 1, bucketNum4 + 1 + bucketNum)

    
    #next
    counter = 0
    Bucket1 = []
    Bucket2 = []
    Bucket3 = []
    Bucket4 = []
    Bucket5 = []
    while counter < len(fileList):
        if min(bucket1) <= fileList[counter] <= max(bucket1):
            Bucket1 = Bucket1 + [fileList[counter]]
        
        if min(bucket2) <= fileList[counter] <= max(bucket2):
            Bucket2 = Bucket2 + [fileList[counter]]
       
        if min(bucket3) <= fileList[counter] <= max(bucket3):
            Bucket3 = Bucket3 + [fileList[counter]]
        
        if min(bucket4) <= fileList[counter] <= max(bucket4):
            Bucket4 = Bucket4 + [fileList[counter]]
       
        if min(bucket5) <= fileList[counter] <= max(bucket5):
            Bucket5 = Bucket5 + [fileList[counter]]
    
        counter = counter + 1
    
    selectionsort(Bucket1)
    selectionsort(Bucket2)
    selectionsort(Bucket3)
    selectionsort(Bucket4)
    selectionsort(Bucket5)

    sortedList = Bucket1 + Bucket2 + Bucket3 + Bucket4 + Bucket5
    return(sortedList)






#Begin actual program
fileFound = 0
while fileFound < 3:
    FileList = []
    try:
        print('Hello! Please enter the file name including the absolute path of the file you want your numerical data to be read from.')
        fileName = input()
        with open(fileName, 'r') as f:
            for line in f:
                FileList = FileList + [int(line)]
        
        f.close()
        print('Here is your data set ... ')
        print(FileList)
        print('Your data set has ' + str(len(FileList)) + ' elements.')
        
        print('Success.')

        print('Which algorithm would you like to use to sort the data?')
        print('If you would like to use bubble sort, type: 1')
        print('If you would like to use selection sort, type: 2')
        print('If you would like to use bucket sort, type: 3')
        print('If you would like to use merge sort, type: 4')
        algInp = input()

        
        #print(start_time)

       
        start_time = time.time()
        sortList = bubblesort(FileList)
        bubbleSortTime = time.time() - start_time
        

          
        start_time = time.time()
        sortList = selectionsort(FileList)
        selectionSortTime = time.time() - start_time
       

        
        start_time = time.time()
        sortList = bucketsortprogram(FileList)
        bucketSortTime = time.time() - start_time
        

       
        start_time = time.time()
        sortList = mergesortprogram(FileList)
        mergeSortTime = time.time() - start_time
        

        print('Here is the sorted list which has been sorted by your desired sorting algorithm:')
        print(sortList)

        
        print('Here are the processing times for each algorithm using your data set:')
        print('Bubble Sort:\t' + str(bubbleSortTime) + ' seconds')
        print('Selection Sort:\t' + str(selectionSortTime) + ' seconds')
        print('Bucket Sort:\t' + str(bucketSortTime) + ' seconds')
        print('Merge Sort:\t' + str(mergeSortTime) + ' seconds')

        timeBub =(bubbleSortTime)
        timeSel = (selectionSortTime)
        timeBuc = (bucketSortTime)
        timeMer = (mergeSortTime)

        timeList = []
        timeList = timeList + [timeBub]
        timeList = timeList + [timeSel]
        timeList = timeList + [timeBuc]
        timeList = timeList + [timeMer]

         #check which one took least time

        if min(timeList) == timeList[0]:
            print('The most efficient sorting algorithm for this data set is bubble sort')

        if min(timeList) == timeList[1]:
            print('The most efficient sorting algorithm for this data set is selection sort')

        if min(timeList) == timeList[2]:
            print('The most efficient sorting algorithm for this data set is bucket sort')

        if min(timeList) == timeList[3]:
            print('The most efficient sorting algorithm for this data set is merge sort')


        fileFound = 3
        

        
    except:
        fileFound = fileFound + 1
        print('Invalid answer. Please reenter')


