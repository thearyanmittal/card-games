#Card class to be imported by every program in repository

#Ace value initialized to 11, can be changed to 1 in-game
class Card:
    def __init__(self, suit_id, rank_id):
        self.suit_id = suit_id
        self.rank_id = rank_id

        if self.rank_id == 1:
            self.rank = "Ace"
            self.value = 11
        elif self.rank_id == 11:
            self.rank = "Jack"
            self.value = 10
        elif self.rank_id == 12:
            self.rank = "Queen"
            self.value = 10
        elif self.rank_id == 13:
            self.rank = "King"
            self.value = 10
        elif 2 <= self.rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        else:
            self.rank = "RankError"
            self.value = -1


        if self.suit_id == 1:
            self.suit = "Hearts"
            self.symbol = "\u2665"
        elif self.suit_id == 2:
            self.suit = "Clubs"
            self.symbol = "\u2663"
        elif self.suit_id == 3:
            self.suit = "Spades"
            self.symbol = "\u2660"
        elif self.suit_id == 4:
            self.suit = "Diamonds"
            self.symbol = "\u2666"
        else:
            self.suit = "SuitError"
        
        self.full_name = f"{self.rank} of {self.suit}"

        if self.rank_id in (1, 11, 12, 13):
            self.short_name = self.rank[0] + self.symbol
        else:
            self.short_name = self.rank + self.symbol

    def __str__(self):
        return self.full_name
