import random
from typing import List
from src.landlords.model.card import Card
from src.landlords.enum.enum import Suit


class Deck:
    
    card_value_map = {"3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14, "2": 15, "Joker": 16}
    value_card_map = {3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A", 15: "2", 16: "Joker"}
    
    
    def __init__(self):
        self.cards: List[Card] = []
        self.__initialize_deck()
        self.deal_count = 0
        
    
    def __initialize_deck(self):
        for i in range(3, 16):
            for suit in [_suit for _suit in Suit if _suit not in [Suit.sJoker, Suit.bJoker]]:
                self.cards.append(Card(self.value_card_map[i], i, suit))
        self.cards.append(Card("Joker", 18, Suit.bJoker))
        self.cards.append(Card("Joker", 17, Suit.sJoker))
        
    
    def shuffle(self):
        random.shuffle(self.cards)
    
        
    def has_next(self):
        return self.deal_count < len(self.cards)
    
    
    def deal(self):
        self.deal_count += 1
        return self.cards[self.deal_count-1]
    
    
    def show(self):
        for card in self.cards:
            print(card)

    
