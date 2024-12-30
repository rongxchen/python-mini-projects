from enum import Enum


class Character(Enum):
    LANDLORD = 1
    PEASANT = 2
    
    
class Suit(Enum):
    Spades = "♠"
    Hearts = "♥"
    Diamonds = "♦"
    Clubs = "♣"
    sJoker = "Small Joker"
    bJoker = "Big Joker"
