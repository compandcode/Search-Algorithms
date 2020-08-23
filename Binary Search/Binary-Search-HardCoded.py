#Binary Search Implementation
dataSet = [5,13,16,19,26,35,37,57,86,90,93,98]
#target
first = 0
last = (len(dataSet)-1) #Index position stored in a variable.

def binarySearch(dataSet,target,first,last):
    if last < first:
        return -1
    else:
        midpoint = int((first+last)/2)
        if dataSet[midpoint] > target:
            return binarySearch(dataSet,target,first,midpoint-1)
        elif dataSet[midpoint] < target:
            return binarySearch(dataSet,target,midpoint+1,last)
        else:
            return(dataSet[midpoint])
            
'''
Test Cases:
print(binarySearch(dataSet,5,first,last))
print(binarySearch(dataSet,13,first,last))
print(binarySearch(dataSet,16,first,last))
print(binarySearch(dataSet,19,first,last))
print(binarySearch(dataSet,26,first,last))
print(binarySearch(dataSet,35,first,last))
print(binarySearch(dataSet,37,first,last))
print(binarySearch(dataSet,57,first,last))
print(binarySearch(dataSet,86,first,last))
print(binarySearch(dataSet,90,first,last))
print(binarySearch(dataSet,93,first,last))
print(binarySearch(dataSet,98,first,last))
'''


