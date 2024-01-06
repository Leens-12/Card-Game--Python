# War Card Game

## **Overview** 
This is a modified version of the classic card game "War." The program is a simple implementation of the game where players draw cards in turns, and the player with the higher card wins. In case of a tie, a "War" scenario is triggered, leading to additional rounds.

## **Project Information** 
- Program Name: War Card Game
- Last Modified: 1/5/2024
- Author: Alina

## **How to Play**
1. Run the program.
2. Choose the game mode:
   - Single Player Mode (against the computer)
   - Two Player Mode
3. Enter player names and the number of cards to play with (1 to 26).
4. The game progresses in rounds, with players drawing cards in turns.
5. If a player's card is higher, they gain points; if lower, they lose points.
6. In the event of a tie, a "War" scenario occurs, leading to additional rounds.
7. The game continues until one player runs out of cards or until the player decides to end the game.
8. The player with the highest score at the end is declared the winner.
  
## **Future Improvements**
- Add more features such as a graphical user interface (GUI) for a better gaming experience.
- Implement additional game modes or variations.
- Optimize and refactor the code for better readability and maintainability.

## **Sample Output**
```
Hello, welcome to the game WAR!

Choose Game Mode:
1. Single Player Mode
2. Two Player Mode
Enter your choice: 1

Player 1, Enter your name: Leens
Enter the number of cards that you want to play with (1 to 26): 2

Leens's Turn: 
Press enter to intitiate the dealing:
The cards are being dealt...
Please wait...
+----------------+
|4  		 |
|                |
|                |
|                |
|     Spades	 |
|                |
|                |
|                |
|              4 |
+----------------+

Computer's Turn: 
+----------------+
|A  		 |
|                |
|                |
|                |
|     Clubs	 |
|                |
|                |
|                |
|              A |
+----------------+

Leens : 1

Computer : 3

Leens's Turn: 
Press enter to intitiate the dealing:
The cards are being dealt...
Please wait...
+----------------+
|3  		 |
|                |
|                |
|                |
|     Spades	 |
|                |
|                |
|                |
|              3 |
+----------------+

Computer's Turn: 
+----------------+
|A  		 |
|                |
|                |
|                |
|     Clubs	 |
|                |
|                |
|                |
|              A |
+----------------+

Leens : 0

Computer : 4

Computer is the winner: 4
The game ended
Enter 1 to play another game: 0
Bye!
```
