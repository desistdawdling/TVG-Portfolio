
/*
Online Java - IDE, Code Editor, Compiler

Online Java is a quick and easy tool that helps you to build, compile, test your programs online.
*/
import java.lang.Math;
import java.util.Scanner;

public class Main{

    public static void main (String [] numberGuessingGame){
        Scanner sc = new Scanner(System.in);
        int newScore = 0;
        int playAgain = 0;
        boolean willPlayAgain = true;
        if (playAgain != 0){
            willPlayAgain = false;
        }
        else
            while (willPlayAgain) {
                newScore+=newScore;
                // Generate the numbers
                int number = 1 + (int)(100 * Math.random());
                // Number of guesses allowed 
                int K = 5;
                int i = 0;
                int guess;
                // Score tracking
     
                System.out.println("A number is chosen between 1 and 100. Guess the number within 5 trials.");
     
                // Loop over number of trials (int K)
                for (i = 0; i < K; i++) {
     
                    System.out.println("Guess the number:");
     
                    // Take input for guessing
                    guess = sc.nextInt();
     
                    // If the number is guessed
                    if (number == guess) {
                        System.out.println("Congratulations! You guessed the number.");
                        break;
                    }
                    // If number too high
                    else if (number > guess && (i != (K - 1))) {
                        System.out.println("The number is greater than " + guess);
                    }
                    // If number too low
                    else if (number < guess && (i != (K - 1))) {
                        System.out.println("The number is less than " + guess);
                    }
                }
                newScore += (i * 10);
                System.out.println("Your Score is: " + newScore);
         
                if (i == K) {
                    System.out.println(
                        "You have no more tries left.");
         
                    System.out.println("The number was " + number);
                        
                System.out.println("Do you want to play again? 0 for Yes or 1 for No: ");
                playAgain = sc.nextInt();
                    continue;
                }
                else break;
            }
        }
    }
