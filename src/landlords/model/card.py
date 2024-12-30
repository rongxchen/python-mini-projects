from src.landlords.enum.enum import Suit


class Card:
    
    def __init__(self, str_value: str, value: int, suit: Suit):
        self.str_value = str_value
        self.value = value
        self.suit = suit
    
    
    def __str__(self):
        return f"{self.str_value}{self.suit.value}"
    
    
    def __repr__(self):
        return self.__str__()
    
    
    def get_value(self):
        return self.value
