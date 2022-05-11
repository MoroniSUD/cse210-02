#W03 Teach: Designer & W04 Prove: Developer
#Autor: Carrasco Dario
#Instructor: Brad Lythgoe

'''Rules: Hilo is played according to the following rules.
    The player starts the game with 300 points. Individual cards are represented as a number from 1 to 13.
    The current card is displayed. The player guesses if the next one will be higher or lower.
    The the next card is displayed. The player earns 100 points if they guessed correctly.
    The player loses 75 points if they guessed incorrectly. If a player reaches 0 points the game is over.
    If a player has more than 0 points they decide if they want to keep playing.
    If a player decides not to play again the game is over.
'''

#I call the random library for the random values of the cards.
import  random


class Card:
    """Card class to play
    Card's responsibility is to develop the game in all its stages.
    Attributes:
        score: the points with which the player starts and achieves.
        first_card: the first random value of the game.
        second_card: the first random value of the game.
        name: name of the person playing the game.
    """        
    def __init__(self, name):
        """Constructs a new Card.
        
        Args:
            self (Card): an instance of Card.
        """
        self.score = 300
        self.first_card = 0
        self.second_card = 0
        self.name = name


    def Play(self):
        """Starts the game by running the main game.
        
        Args:
            self (Card): an instance of Card.

        """
        choose = 'y'
        
        #evaluate the option to continue playing
        while choose.lower() == 'y':

            #Randomly assigning values to the cards
            first_card = random.randint(1,13)
            second_card = random.randint(1,13)
            
            print(f'\nThe first card is: {first_card}')
            option = input(f'{self.name}, la proxima carta es mas alta o baja (h o l): ')
            print(f'The next card is: {second_card}')

            # Depending on the option entered by the user, the comparison of the two charts is evaluated as high or low.
            if first_card < second_card and option.lower() == 'h':
                self.score += 100
                print(f'Won. Your score {self.name} is {self.score}')
            elif first_card > second_card and option.lower() == 'l':
                self.score += 100
                print(f'Won. Your score is {self.score}')
            elif first_card == second_card:
                print(f'Cards are the same. Your score is {self.score}')
            else:
                self.score -= 75 
                print(f'Lost. Your score is {self.score}')   
            if self.score <= 0:
                print(f'You lost. The end. Your score is {self.score}')
                choose = 'n'
            else:    
                choose = input(f'{self.name} want play again (y/n): ')
                if choose.lower() != 'y':
                    print(f'Thank you for playing. The final score is {self.score}\n.')

def main():
    #I call the classes and their methods. I request the player's name
    name = input("Please enter your name: ")
    tarjeta = Card(name)
    tarjeta.Play()

# Call main to start this program.
if __name__ == "__main__":
    main()

