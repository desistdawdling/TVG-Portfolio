import java.lang.Math;
import java.util.Scanner;

/*    If the guessed number is bigger than the actual number, the program will respond with the message that the guessed number is higher than the actual number.
    If the guessed number is smaller than the actual number, the program will respond with the message that the guessed number is lower than the actual number.
    If the guessed number is equal to the actual number or if the K trials are exhausted, the program will end with a suitable message.

Approach: Below are the steps:  

    The approach is to generate a random number using Math.random() method in Java.
    Now using a loop, take K input from the user and for each input print whether the number is smaller or larger than the actual number.
    If within K trials the user guessed the number correctly, print that the user won.
    Else print that he was not able to guess and then print the actual number.
    */

public static void main (String[] args){
 
    // Function that implements the
    // number guessing game

    public static void numberGuessingGame(){
        Scanner sc = new Scanner(System.in);
 
        // Generate the numbers
        int number = 1 + (int)(100 * Math.random());
        int K = 5;
        int i, guess;
        int newScore += (i * 10);
 
        System.out.println("A number is chosen between 1 to 100. Guess the number within 5 trials.");
 
        // Loop over number of trials (int K)
        for (i = 0; i < K; i++) {
 
            System.out.println("Guess the number:");
 
            // Take input for guessing
            guess = sc.nextInt();
 
            // If the number is guessed
            if (number == guess) {
                System.out.println(
                    "Congratulations! You guessed the number.");
                break;
            }
            // If number too high
            else if (number > guess && (i != (K - 1))) {
                System.out.println(
                    "The number is greater than " + guess);
            }
            // If number too low
            else if (number < guess && (i != (K - 1))) {
                System.out.println(
                    "The number is less than " + guess);
            }
        }
        newScore += (i * 10);
        System.out.println("Your Score is: " + newScore)
 
        if (i == K) {
            System.out.println(
                "You have no more tries left.");
 
            System.out.println(
                "The number was " + number);
        }
    }
 
    // Driver Code
    public static void
    main(String arg[])
    {
 
        // Function Call
        guessingNumberGame();
    }
}
    


