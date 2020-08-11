//Values are hardocoded because otherwise an HTML GUI interface would be required.

var dataSet = [6,3,2,1,19,58,27,36];  //Dataset to be searched.
var target = 100; //The number we're looking for, in this case 1.
var length = dataSet.length; //Stores the length in a variable.
var lastElement = (dataSet.length-1); //Stores the last element as a variable.
var found = false; //Changes to true when found.

for (i=0; i < dataSet.length; i++){ //Loops through the list.
    if (dataSet[i] == target){ //If the value is found.
        console.log("Target value has been found") //Inform the user.
        break; //Stops looking through the list because the value has been found.
        found = true; //Change found to true.
    }
    else if (dataSet[i] != target){ //If the value doesn't equal target.
        console.log("Target value not found") //Inform the user.
    }
    else if ((dataSet[i] == lastElement) && (found == false)) { //If we reach the end of the list and the value still isn't found.
        console.log("Target value is not in the list.") //Inform the user that the value isn't in the list.

    }
}