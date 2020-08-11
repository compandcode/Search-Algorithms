#include <stdio.h>
//Linear Search implementation:
int main(void) {
  //Hardcodes a dataSet of 8 elements.
  int dataSet[8] = {6,3,2,1,19,58,27,36};
  int i;//Initialised for the loop.
  int target = 2;
  int number; //Current number (i)
  for (i=0; i<8;i++){
    number = dataSet[i]; //Stores the current number in a variable.
    //printf("%d, ",number); //Outputs the number.
    if (number == target){ //If number matches the one we're looking for.
      printf(" %d, has been found", number); //Inform the user.
      break; //Stop searching.
    }
    else { //Otherwise
      printf(" not found"); //Inform the user it's not found. Carry on searching.
    }
  }
  
  return 0;
}