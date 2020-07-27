#import modules
import random
#import Card class
from card import Card

#define function to print blank lines
def blank_lines(lines):
    for line in range(lines):
        print("\n")


#deck of cards list
deck = []

#set up nested for loops to create a deck of cards
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        deck.append(Card(suit_id, rank_id))

#define Player class
class Player:
    def __init__(self, number, name):
        self.turn_order = number
        self.name = name
        self.hand_total = 0
        self.is_comp = False
    
    def deal_hand(self, deck):
        self.hand = []

        for x in range(2):
            random.shuffle(deck)
            self.hand.append(deck.pop(0))
            self.hand_total += self.hand[x].value

    def hit(self, deck):
        self.hand.append(deck.pop(0))

        self.hand_total = 0
        for card in range(len(self.hand)):
            self.hand_total += self.hand[card].value

    def calc_hand_total(self):
        self.hand_total = 0
        for card in self.hand:
            self.hand_total += card.value  

    def __str__(self):
        return f"Player {self.turn_order}: {self.name}"


#define a kind of Player — the computer
class Computer(Player):
    def __init__(self):
        self.turn_order = 2
        self.name = "Computer"
        self.hand_total = 0
        self.is_comp = True

    def comp_hit(self, deck):
        if 4 <= self.hand_total <= 11:
            self.hit(deck)

        elif 12 <= self.hand_total <= 15:
            #give a 50-50 chance of hitting
            chance = random.random()
            if chance > 0.5:
                self.hit(deck)
            else:
                hitting = False
                hit_or_stand = 's'
        
        elif 16 <= self.hand_total <= 18:
            hitting = False
            hit_or_stand = 's'


#start game loop
while True:

    #define list of players
    players = []

    #select mode/number of players
    while True:
        num_players_input = input("Enter the number of players (2, 3, or 4). Or, to just play against the computer, enter 1: \n")

        if num_players_input in "1234":

            if (int(num_players_input)) in (1, 2, 3, 4):
                num_players = int(num_players_input)
                break
            else:
                print(f"You entered \'{num_players_input}\', which is not a valid input.")

        else:
            print(f"You entered \'{num_players_input}\', which is not a valid input.")

    #create players
    if num_players == 1:
        Comp = Computer()
        player_name = input(f"What is your name? \n")
        while True:
            if player_name != '':
                break
            else:
                print("You did not enter a name.")
                player_name = input(f"What is your name? \n")
      
        players.append(Player(1, player_name))
        players.append(Comp)

    else:
        for num in range(1, num_players + 1):
            player_name = input(f"Enter Player {num}'s name: \n")
            while True:
                if player_name != '':
                    break
                else:
                    print("You did not enter a name.")
                    player_name = input(f"Enter Player {num}'s name: \n")

            players.append(Player(num, player_name))
    
    #deal cards
    for player in players:
        player.deal_hand(deck)


    #iterate over each player, show them their hand, and see whether they want to hit or stand

    for player in players:
        if player.is_comp == False:
            blank_lines(500)

            ready = input(f"{player.name}, are you ready for your turn? Press enter to continue. \n")

            hitting = True

            while hitting:

                print(f"{player.name}'s Hand (value {player.hand_total}): \n")

                for card in player.hand:
                    print(card.short_name)
                
                print()

                while True:

                    if player.hand_total == 21:
                        print("Wow! A natural 21! Press enter to move to the next player's turn. ")
                        hitting = False
                        hit_or_stand = 's'
                        input()
                        break

                    else:
                        hit_or_stand = input("Would you like to hit or stand? Enter 'h' for hit or 's' for stand: \n")
                        if hit_or_stand in ('h', 's'):
                            break
                        else:
                            print("You did not enter a valid value")

                if hit_or_stand == 'h':
                    player.hit(deck)

                    #deals with the 1/11 value problem of the ace
                    aces = [card for card in player.hand if card.rank_id == 1]

                    #calculate 3 values, see which one is closest to 21 and save that value of the hand

                    if len(aces) != 0:

                        with_1_value = 0
                        for card in player.hand:
                            if card.rank_id == 1:
                                with_1_value += 1
                            else:
                                with_1_value += card.value
                        with_1_value = 21 - with_1_value

                        with_all_value = 0
                        for card in aces:
                            if card is aces[0]:
                                with_all_value += 11
                            else:
                                with_all_value += 1
                        for card in player.hand:
                            if card not in aces:
                                with_all_value += card.value
                        with_all_value = 21 - with_all_value

                        with_11_value = 21 - player.hand_total
                        
                        if with_11_value < 0:
                            with_11_value = 21
                        if with_1_value < 0:
                            with_1_value = 21
                        if with_all_value < 0:
                            with_all_value = 21
                        
                        max_hand_value = min([with_1_value, with_11_value, with_all_value])
                        if max_hand_value == with_1_value:
                            for card in player.hand:
                                if card.rank_id == 1:
                                    card.value = 1
                        elif max_hand_value == with_11_value:
                            for card in player.hand:
                                if card.rank_id == 1:
                                    card.value = 11
                        else:
                            for card in player.hand:
                                if card in aces:
                                    if card == aces[0]:
                                        card.value = 11
                                    else:
                                        card.value = 1

                    player.calc_hand_total()
                    if player.hand_total > 21:
                        
                        print(f"{player.name}'s Hand (value {player.hand_total}): \n")
                        for card in player.hand:
                            print(card.short_name)
                        print("\n")

                        if player.turn_order == num_players:
                            print("Oh no! You busted and are out of the game. Better luck next time! Press enter to proceed to results.")
                        else:
                            print("Oh no! You busted and are out of the game. Better luck next time! Press enter to continue to the next player.")
                            
                        input()
                        hitting = False
                        break

                    elif player.hand_total == 21:
                        
                        print(f"{player.name}'s Hand (value {player.hand_total}): \n")
                        for card in player.hand:
                            print(card.short_name)
                        print("\n")
                        
                        if player.turn_order == num_players:
                            print("Your hand total is 21! Press enter to proceed to results.")
                        else:
                            print("Your hand total is 21! Press enter to move to the next player's turn.")

                        input()
                        hitting = False
                        break
                    
                else:
                    hitting = False
                    break
            else:
                #set up while hitting loop like human (copy most of human code, like aces; exclude display values) 
                hitting = True

                while hitting:

                    hit_or_stand = 'h'

                    if hit_or_stand == 'h':
                        player.comp_hit(deck)

                        #deals with the 1/11 value problem of the ace
                        aces = [card for card in player.hand if card.rank_id == 1]

                        #calculate 3 values, see which one is closest to 21 and save that value of the hand

                        if len(aces) != 0:

                            with_1_value = 0
                            for card in player.hand:
                                if card.rank_id == 1:
                                    with_1_value += 1
                                else:
                                    with_1_value += card.value
                            with_1_value = 21 - with_1_value

                            with_all_value = 0
                            for card in aces:
                                if card is aces[0]:
                                    with_all_value += 11
                                else:
                                    with_all_value += 1
                            for card in player.hand:
                                if card not in aces:
                                    with_all_value += card.value
                            with_all_value = 21 - with_all_value

                            with_11_value = 21 - player.hand_total
                            
                            if with_11_value < 0:
                                with_11_value = 21
                            if with_1_value < 0:
                                with_1_value = 21
                            if with_all_value < 0:
                                with_all_value = 21
                            
                            max_hand_value = max([with_1_value, with_11_value, with_all_value])
                            if max_hand_value == with_1_value:
                                for card in player.hand:
                                    if card.rank_id == 1:
                                        card.value = 1
                            elif max_hand_value == with_11_value:
                                for card in player.hand:
                                    if card.rank_id == 1:
                                        card.value = 11
                            else:
                                for card in player.hand:
                                    if card in aces:
                                        if card == aces[0]:
                                            card.value = 11
                                        else:
                                            card.value = 1


                        if player.hand_total > 21:
                            
                            hit_or_stand = 's'
                            hitting = False
                            break

                        elif player.hand_total == 21:

                            hit_or_stand = 's'
                            hitting = False
                            break
                        
                    else:
                        hitting = False
                        break
      
    #show results
    blank_lines(500)

    print("Results:")
    for player in players:
        print(f"{player.name}'s Final Hand (value {player.hand_total}): \n")
        if 21 - player.hand_total >= 0:
            player.far_from_21 = 21 - player.hand_total
        else:
            player.far_from_21 = 21

        for card in player.hand:
            print(card.short_name)

    winning_score = 21
    winners = []
    for player in players:
        if player.far_from_21 < winning_score:
            winning_score = player.far_from_21
    
    for player in players:
        if player.far_from_21 == winning_score:
            winners.append(player)

    if len(winners) < 2:
        print(f"The winner is: {winners[0].name}")
    else:
        print("There was a tie! The winners are:")
        for winner in winners:
            print(winner.name)

    #ask to play again
    while True:
        again = input("Would you like to play again? Enter 'y' for yes or 'n' for no. \n")
        if again in ('y', 'n'):
            break
        else:
            print("You did not enter a valid input.")

    if again == 'n':
        break
    else:
        blank_lines(500)