# Program: War Card Game
# Last Modifided: 1/5/2024
# Name: Alina 
# Despriction: modified version of the card game WAR!

import random

# The function prints out the cards
def cardDie(x, deckName):
    print("+----------------+")
    print("|"  +str(x) + "  \t" + "\t |")
    print("|"  + "                " + "|")
    print("|"  + "                " + "|")
    print("|"  + "                " + "|")
    print("|"  + "     " +deckName+"" + "\t |")
    print("|"  + "                " + "|")
    print("|"  + "                " + "|")
    print("|"  + "                " + "|")
    print("|"  + "             ", str(x) + " |")
    print("+" + "----------------" + "+")

# The function prints out the card suit
def generateDeckName(deckNumber):
    if deckNumber == 1:
        return "Spades"
    elif deckNumber == 2:
        return "Diamonds"
    elif deckNumber == 3:
        return "Clubs"
    else:
        return "Hearts"

# The function prints out the war card
def warCard(word):
    print("+" + "------------------" + "+"       "+" + "------------------" + "+"       "+" + "------------------" + "+")
    print("|" + "                  " + "|"       "|" + "                  " + "|"       "|" + "                  " + "|")
    print("|" + "                  " + "|"       "|" + "                  " + "|"       "|" + "                  " + "|")
    print("|" + "                  " + "|"       "|" + "                  " + "|"       "|" + "                  " + "|")
    print("|" +"     " + str(word)+ "        " "  |"  +"|"  + "  " + "     " + str(word)+ "     " + "   |""|"  + "  " + "     " + str(word)+ "     " + "   |")
    print("|" + "                  " + "|"      "|" + "                  " + "|"      "|" + "                  " + "|")
    print("|" + "                  " + "|"       "|" + "                  " + "|"      "|" + "                  " + "|")
    print("|" + "                  " + "|"       "|" + "                  " + "|"       "|" + "                  " + "|")
    print("+" + "------------------" + "+"       "+" + "------------------" + "+"       "+" + "------------------" + "+")
    
# The function prints out (J, Q, K, A) variables (numbers)
def cardValue (cardNumber):
    if cardNumber == 10:
        return "J"
    elif cardNumber == 11:
        return "Q"
    elif cardNumber == 12:
        return "K"
    elif cardNumber == 13:
        return "A"
    else:
        return str(1+cardNumber)

# start of game
playAgain = 1
while playAgain == 1:
    print("Hello, welcome to the game WAR!")

    # user is able to choose the game mode
    print("\nChoose Game Mode:")
    print("1. Single Player Mode")
    print("2. Two Player Mode")
    gameMode = int(input("Enter your choice: "))

    # Input validation
    while gameMode < 1 or gameMode > 2:
        print("Wrong Input! Try again!")
        gameMode = int(input('Enter your choice (1 or 2): '))

    player1Name = input("\nPlayer 1, Enter your name: ")

    if gameMode == 2:
        player2Name = input("Player 2, Enter your name: ")
    else:
        player2Name = "Computer"

    numCards = int(input("Enter the number of cards that you want to play with (1 to 26): "))

    # Input validation
    while numCards < 1 or numCards > 26:
        print("Wrong Input! Try again!")
        numCards = int(input("Enter the number of cards that you want to play with (1 to 26): "))

    player1Score = numCards
    player2Score = numCards

    # the while loop, have many rounds until the any of the players have 0 points or won
    while player1Score > 0 and player2Score > 0:

        print("\n" + player1Name + "'s Turn: ")
        x = input("Press enter to intitiate the dealing:")
        if len(x) > 0:  # it checks if player one entered any other number,character, letter, it would exit the game
            print('Exit!')
            break

        print("The cards are being dealt...\nPlease wait...")
        player1Card = random.randint(1, 13)
        player1DeckNumber = random.randint(1, 4)
        player1DeckName = generateDeckName(player1DeckNumber)
        cardNumber = cardValue(player1Card)
        cardDie(cardNumber, player1DeckName) # calls the card

        print("\n" + player2Name + "'s Turn: ")
        if gameMode == 2: # only occurs when the user chooses multiplayer mode
            x = input("Press enter to intitiate the dealing:")
            if len(x) > 0: # it checks if player one entered any other number,character, letter, it would exit the game
                print('Exit!')
                break

        player2Card = random.randint(1, 13)
        player2DeckNumber = random.randint(1, 4)
        player2DeckName = generateDeckName(player2DeckNumber)
        cardNumber = cardValue(player2Card)
        cardDie(cardNumber, player2DeckName) # calls the card

        if player1Card > player2Card: #if the player 1 card is higher than player 2
            player1Score = player1Score + 1
            player2Score = player2Score - 1
        elif player2Card > player1Card: #if the player 2 card is higher than player 1
            player2Score = player2Score + 1
            player1Score = player1Score - 1
        else: #if both statements above are false then War is declared
            print("\nWar!")
            print("\n" + player1Name + ": ")
            print("The cards are bring dealt....")
            warCard("war")
            player1Card = random.randint(1, 13)
            player1DeckNumber = random.randint(1, 4)
            player1DeckName = generateDeckName(player1DeckNumber)
            cardNumber = cardValue(player1Card)
            cardDie(cardNumber, player1DeckName)

            print("\n" + player2Name + ": ")
            print("The cards are bring dealt....")
            warCard("war")
            player2Card = random.randint(1, 13)
            player2DeckNumber = random.randint(1, 4)
            cardNumber = cardValue(player2Card)
            cardDie(cardNumber, player2DeckName)

            if player1Card > player2Card: #player 1 card is higher than player 2 then they gain 5 points
                player1Score = player1Score + 5
                player2Score = player2Score - 5
            elif player2Card > player1Card: #player 2 card is higher than player 1 then they gain 5 points
                player2Score = player2Score + 5
                player1Score = player1Score - 5
            else: #if both statements above are false then second War is declared
                print("\nWar 2")
                print("\n" + player1Name + ": ")
                print("The cards are bring dealt....")
                warCard("war")
                player1Card = random.randint(1, 13)
                player1DeckNumber = random.randint(1, 4)
                player1DeckName = generateDeckName(player1DeckNumber)
                cardNumber = cardValue(player1Card)
                cardDie(cardNumber, player1DeckName)

                print("\n" + player2Name + ": ")
                print("The cards are bring dealt....")
                warCard("war")
                player2Card = random.randint(1, 13)
                player2DeckNumber = random.randint(1, 4)
                cardNumber = cardValue(player2Card)
                cardDie(cardNumber, player2DeckName)

                if player1Card > player2Card: # player 1's card is higher than player 2's card
                    player1Score = player1Score + 9
                    player2Score = player2Score - 9
                elif player2Card > player1Card: # player 2's card is higher than player 1's card
                    player2Score = player2Score + 9
                    player1Score = player1Score - 9
                else: # if both statemnts are false then neither one gain or lose points
                    print("Tie!")

        # Check score for correctness
        if player1Score < 0:
            player1Score = 0
        if player1Score > 2 * numCards:
            player1Score = 2 * numCards

        if player2Score < 0:
            player2Score = 0
        if player2Score > 2 * numCards:
            player2Score = 2 * numCards

        print("\n" + player1Name + " : " + str(player1Score))
        print("\n" + player2Name + " : " + str(player2Score))


    if player1Score > player2Score: # player 1 has more points than player 2
        print("\n" + player1Name + " is the winner: " + str(player1Score))
    elif player2Score > player1Score: # player 2 has more points than player 2
        print("\n" + player2Name + " is the winner: " + str(player2Score))
    else: # if the above statements are false then it's a tie
        print("It's a tie: Scores are " + str(player2Score) + ", " + str(player1Score))

    #game ends
    print("The game ended")

    playAgain = int(input("Enter 1 to play another game: "))
print("Bye!")
