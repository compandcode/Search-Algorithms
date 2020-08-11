import java.util.Scanner; //Allows user input to be taken.
import java.util.Random; //Allows random numbers to be generated.
import java.util.ArrayList; //Allows the array to resize depending on the number of elements.

public class LinearSearch {
    public static void main(String[] args) {

        Random rand = new Random(); //Creates an instance of the Random class.

        Scanner scanner = new Scanner(System.in); //Constructs a scanner object.
        System.out.println("Enter the lowest number that could appear in the list:");
        int lowestNumber = scanner.nextInt(); //Stores the input in the variable.
        System.out.println("Enter the highest number that could appear in the list:");
        int highestNumber = scanner.nextInt(); //Stores the input in the variable.
        System.out.println("Enter the number of elements that will appear in the list:");
        int numberOfElements = scanner.nextInt(); //Stores the input in the variable.
        System.out.println("Enter the number you want to find:"); //Asks the user to input a value to search for.
        int target = scanner.nextInt(); //Stores the value in the target variable.

        ArrayList<Integer> dataSet = new ArrayList<>() ; //Creates a dynamic list (to adjust depending on the number of elements).
        boolean found = false; //Initially the number hasn't yet been found.

        for (int i = 0; i < numberOfElements; i++) { //Loops through each element in list, incrementing index by 1 each time.
            int randomNumber = rand.nextInt(highestNumber+1); //Each random number is stored in a variable, must be smaller than the largest number
            if (randomNumber < lowestNumber) { //If the randomly generated number is too small (less than what the user asked for).
                randomNumber = rand.nextInt(highestNumber); //Regenerate it.
            } else {
                dataSet.add(randomNumber); //Otherwise add it to the list. This repeats as many times as numberOfElements.
            }
        }
        System.out.println(dataSet); //Outputs the data set before the search is carried out.


        int lastElement = (numberOfElements-1); //Avoids hardcoding.

        for (int j : dataSet) { //Loops through the dataset. (FOR EACH LOOP).
            if (j == target) { //If the current value matches the target.
                System.out.println(target+" Was found"); //Inform the user.
                break; //Stops looking since the number has been found.
            } else if (j != target) { //If the current value != target.
                System.out.println(j+" Is not "+ target); //Inform the user.
            }
            if (j == (dataSet.get(lastElement)) && found == false) { //If the dataset has been looped through and the value still isn't found:
                System.out.println("Value not in list. -1"); //Informs that the value isn't in the list.
            }
        }
    }
}