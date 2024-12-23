import java.util.ArrayList;
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;

public class Hangman {

    public static void main(String[] args) {
        // Retrieve hangman art and word list from separate classes
        String[] stages = GameArt.getStages();
        ArrayList<String> wordList = WordList.getWords();
        // Display the logo
        System.out.println(GameArt.getLogo()); // Print the logo from GameArt class
        System.out.println("Welcome to Hangman!");

        // Game setup
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        String chosenWord = wordList.get(random.nextInt(wordList.size()));
        int lives = stages.length - 1;

        System.out.println(stages[lives]);

        // Placeholder for the word
        StringBuilder display = new StringBuilder("_ ".repeat(chosenWord.length()));
        System.out.println("Word to guess: " + display);

        // Track guessed letters and correct guesses
        HashSet<Character> guessedLetters = new HashSet<>();
        ArrayList<Character> correctLetters = new ArrayList<>();
        boolean gameOver = false;

        // Game loop
        while (!gameOver) {
            System.out.println("\n**************************** " + lives + "/" + (stages.length - 1) + " LIVES LEFT ****************************");
            System.out.print("Guess a letter: ");
            char guess = scanner.nextLine().toLowerCase().charAt(0);

            if (guessedLetters.contains(guess)) {
                System.out.println("You've already guessed '" + guess + "'. Try a different letter!");
                continue;
            }

            guessedLetters.add(guess);

            // Check if the guess is in the word
            boolean correctGuess = false;
            for (int i = 0; i < chosenWord.length(); i++) {
                if (chosenWord.charAt(i) == guess) {
                    correctGuess = true;
                    correctLetters.add(guess);
                }
            }

            // Update display
            display = new StringBuilder();
            for (int i = 0; i < chosenWord.length(); i++) {
                char letter = chosenWord.charAt(i);
                if (correctLetters.contains(letter)) {
                    display.append(letter);
                } else {
                    display.append("_ ");
                }
            }

            System.out.println("Word to guess: " + display);

            // If incorrect, reduce lives
            if (!correctGuess) {
                lives--;
                System.out.println("You guessed '" + guess + "' which is not in the word. You lose a life.");
            }

            // Check win/loss conditions
            if (lives == 0) {
                gameOver = true;
                System.out.println("*********************** YOU LOSE ***********************");
                System.out.println("The word was: " + chosenWord);
            } else if (!display.toString().contains("_")) {
                gameOver = true;
                System.out.println("**************************** YOU WIN ****************************");
            }

            System.out.println(stages[stages.length - 1 - lives]);
        }

        scanner.close();
    }
}
