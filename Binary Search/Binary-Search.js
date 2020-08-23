dataSet = [5,13,16,19,26,35,37,57,86,90,93,98];

first = 0
last = dataSet.length; //Index position stored in a variable.
target = 37;

function binarySearch(dataSet,target,first,last){
    if (last<first){
        return -1;
    }
    else{
        var midpoint = int((first+last)/2);
        if(dataSet[midpoint] > target){
            return binarySearch(dataSet,target,first,midpoint-1)
        }
        else if(dataSet[midpoint] < target){
            return binarySearch(dataSe,target,midpoint+1,last)
        }
        else{
            return(dataSet[midpoint])
        }
    }
}