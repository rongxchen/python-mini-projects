from typing import List, Union
from src.landlords.enum.enum import Character
from src.landlords.model.card import Card


def pad(s: str, length: int):
    return " " * (length - len(s)) + s


class Player:
    
    def __init__(self, role: Character, name: str = ""):
        self.role = role
        self.name = name
        self.cards: List[Card] = []
        
        
    def receive_card(self, card: Union[Card, List[Card]]):
        if isinstance(card, list):
            self.cards.extend(card)
        else:
            self.cards.append(card)
        
    
    def play_cards(self, indexes: List[int]):
        cards = [self.cards[i] for i in indexes]
        self.cards = [self.cards[i] for i in range(len(self.cards)) if i not in indexes]
        return cards


    def show_cards(self):
        _cards = [f'[{pad(self.cards[i].__str__(), 3)}]' for i in range(len(self.cards))]
        print(f"{pad(self.name, 10)}", *_cards)


    def count_cards(self):
        return len(self.cards)

    
    def sort_cards(self):
        self.cards.sort(key=lambda x : x.get_value())


class LandLord(Player):

    def __init__(self, name: str = ""):
        super().__init__(Character.LANDLORD, name)
        
        
class Peasant(Player):

    def __init__(self, name: str = ""):
        super().__init__(Character.PEASANT, name)
        