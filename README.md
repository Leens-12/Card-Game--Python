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
   
## **Code Structure**
**Functions:**
- cardDie(x, deckName): Prints the visual representation of a card.
- generateDeckName(deckNumber): Returns the suit name based on the deck number.
- warCard(word): Prints the visual representation of a war card.
- cardValue(cardNumber): Returns the corresponding value (J, Q, K, A) for numeric card values.
  
**Game Loop:**
- The program runs in a loop until the player decides not to play again.
- Allows for both single and two-player modes.
- Implements card drawing, scoring, and "War" scenarios.

## **Usage**
- Ensure you have a Python environment installed.
- Run the code.
- Follow the on-screen prompts to set up the game and make your moves.
  
## **Future Improvements**
- Add more features such as a graphical user interface (GUI) for a better gaming experience.
- Implement additional game modes or variations.
- Optimize and refactor the code for better readability and maintainability.
