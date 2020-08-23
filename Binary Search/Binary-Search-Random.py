import random

lowestElement = int(input("Enter the lowest number that can appear in the list:"))
highestElement = int(input("Enter the highest number that can appear in the list:"))
numberOfElements = int(input("Enter the number of elements you want in the list:"))

dataSet = [] #Initialises the data set.
lastElement = (len(dataSet)-1) #Stores the last element's indec as a variable.
for i in range(numberOfElements): #Loops through the list.
    randomNumber = random.randint(lowestElement,highestElement) #Generates a random number for each index position.
    dataSet.append(randomNumber) #Adds the random number to the list.
dataSet.sort()
print(dataSet)
target = int(input("What number do you want to look for?"))

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

#Main Program:
print(binarySearch(dataSet,target,first,last))

'''
This algorithm searches through the list however it doesn't append the size of it.
It manages to retrieve the correct answer still.
'''