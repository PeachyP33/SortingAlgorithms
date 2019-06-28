#Bucket sort
#read data, find min and max, create 5 buckets and put data into buckets based on range
#use bubble sort in each bucket


#read data from file and put data in list. Display number of elements
fileList = []
with open('/Users/Pracheeti/Documents/Python/file_numbers_list.txt', 'r') as f:
    for line in f:
        fileList = fileList + [int(line)]
        
f.close()
print(fileList)
print(fileList[3])
print('Your data set has ' + str(len(fileList)) + ' elements.')

#function
def bucketsort(maxim, minim):
    import math
    rangeNum = maxim - minim
    print(math.ceil(rangeNum / 5) + 1)
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
    
    return (min(bucket1), max(bucket1), min(bucket2), max(bucket2), min(bucket3), max(bucket3), min(bucket4), max(bucket4), min(bucket5), max(bucket5))

#sorting function
def selectionSort(myList) :
    #myList = []
    print(len(myList))
   
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

    return (myList)


    
rangeNum = (max(fileList) - min(fileList))
print(max(fileList))
maximum = max(fileList)
print(min(fileList))
minimum = (min(fileList))
hello = bucketsort(maximum, minimum)
print(hello)

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
    
print(Bucket1)
print(Bucket2)
print(Bucket3)
print(Bucket4)
print(Bucket5)

print(len(Bucket1))

print(selectionSort(Bucket1))
selectionSort(Bucket2)
selectionSort(Bucket3)
selectionSort(Bucket4)
selectionSort(Bucket5)

sortedList = Bucket1 + Bucket2 + Bucket3 + Bucket4 + Bucket5
print(sortedList)

    
    

      

