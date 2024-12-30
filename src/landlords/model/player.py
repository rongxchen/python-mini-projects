from typing import List
from src.landlords.enum.enum import Character, Suit
from src.landlords.model.card import Card


class Player:
    
    def __init__(self, role: Character, name: str = ""):
        self.role = role
        self.name = name
        self.cards: List[Card] = []
        
        
    def receive_card(self, card: Card):
        self.cards.append(card)


    def show_cards(self):
        print(f"{self.name}:\t{self.cards}")


    def count_cards(self):
        return len(self.cards)

    
    def sort_cards(self):
        self.cards.sort(key=lambda x: x.get_value())


class LandLord(Player):

    def __init__(self, name: str = ""):
        super().__init__(Character.LANDLORD, name)
        
        
class Peasant(Player):

    def __init__(self, name: str = ""):
        super().__init__(Character.PEASANT, name)
        