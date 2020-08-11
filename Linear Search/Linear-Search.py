import random #Allows the data set to be randomly generated, rather than hardcoding.
#Linear search implementations:

#*** This solution doesn't exactly follow the pseudocode of using variables for index position but it's still efficient.***

lowestElement = int(input("Enter the lowest number that can appear in the list:"))
highestElement = int(input("Enter the highest number that can appear in the list:"))
numberOfElements = int(input("Enter the number of elements you want in the list:"))

dataSet = [] #Initialises the data set.
lastElement = (len(dataSet)-1) #Stores the last element's indec as a variable.
for i in range(numberOfElements): #Loops through the list.
    randomNumber = random.randint(lowestElement,highestElement) #Generates a random number for each index position.
    dataSet.append(randomNumber) #Adds the random number to the list.
print(dataSet) #Outputs the end list.

target = int(input("Enter a number to search for")) #The number we're looking for.
for number in dataSet: #Loops through all the numbers in the dataSet.
    if number == target: #If the current number is the one we want.
        print(number," Found in list. The index position is:",dataSet.index(target)) #Inform the user. Shows the index position.
        found = True
        break #Stops the loop because we don't need to look any further.
    elif number != target:
        print(number ," is not", target) #Indicates the number hasn't yet been found.
        #number += 1 #Increments to look at the next number.
    elif (number == dataSet[lastElement]) & (found != True):
        print("-1, Number IS NOT in the list")
    
    
