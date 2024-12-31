import random
from typing import List
from src.landlords.model.card import Card
from src.landlords.enum.enum import Suit, Rank, get_card_name


class Deck:
    
    value_card_map = {rank.value: get_card_name(rank) for rank in Rank}
    
    def __init__(self):
        self.cards: List[Card] = []
        self.__initialize_deck()
        self.deal_count = 0
        
    
    def __initialize_deck(self):
        for i in range(3, 16):
            for suit in [_suit for _suit in Suit if _suit not in [Suit.BLACK_JOKER, Suit.RED_JOKER]]:
                self.cards.append(Card(self.value_card_map[i], i, suit))
        self.cards.append(Card("", Rank.BLACK_JOKER.value, Suit.BLACK_JOKER))
        self.cards.append(Card("", Rank.RED_JOKER.value, Suit.RED_JOKER))
        
    
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
