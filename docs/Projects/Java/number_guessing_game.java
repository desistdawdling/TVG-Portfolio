
/*
Online Java - IDE, Code Editor, Compiler

Online Java is a quick and easy tool that helps you to build, compile, test your programs online.
*/
import java.lang.Math;
import java.util.Scanner;

public class Main{

    public static void main (String [] numberGuessingGame){
        Scanner sc = new Scanner(System.in);
        int K = 5;
        int startScore = 0;
        int newScore = 0;
        int playAgain = 0;
        boolean willPlayAgain = true;
        if (playAgain != 0){
            willPlayAgain = false;
        }
        else
            while (willPlayAgain) {
                startScore = (K+1) * 10;
                newScore+=newScore;
                // Generate the numbers
                int number = 1 + (int)(50 * Math.random());
                // Number of guesses allowed 
                int i = 0;
                int guess;
                // Score tracking
     
                System.out.println("A number is chosen between 1 and 50. Guess the number within 5 trials.");
     
                // Loop over number of trials (int K)
                for (i = 0; i < K; i++) {
                    startScore -= 10;
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
                newScore += (startScore);
                
         
                if (i == K) {
                    System.out.println("You have no more tries left.");
                    System.out.println("The number was " + number);
                    newScore-=10;
                    
                System.out.println("Your Score is: " + newScore);
                        
                System.out.println("Do you want to play again? 0 for Yes or 1 for No: ");
                playAgain = sc.nextInt();
                    continue;
                }
                else break;
            }
        }
<<<<<<< HEAD
    }
=======
    }


>>>>>>> 123b7b20f7fea03182ecdc68958f32b6251a8c76
