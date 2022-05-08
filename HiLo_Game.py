import  random

class Card:
        
    def __init__(self, name):
        self.score = 300
        self.first_card = 0
        self.second_card = 0
        self.name = name


    def Play(self):
        choose = 'y'
        
        while choose.lower() == 'y':

            first_card = random.randint(1,13)
            second_card = random.randint(1,13)
            
            print(f'\nThe first card is: {first_card}')
            option = input(f'{self.name}, la proxima carta es mas alta o baja (h o l): ')
            print(f'The next card is: {second_card}')
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

    name = input("Please enter your name: ")
    tarjeta = Card(name)
    tarjeta.Play()

# Call main to start this program.
if __name__ == "__main__":
    main()

