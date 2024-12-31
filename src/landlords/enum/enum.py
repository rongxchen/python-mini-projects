from enum import Enum


class Character(Enum):
    LANDLORD = 1
    PEASANT = 2
    
    
class Suit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    BLACK_JOKER = "BJ"
    RED_JOKER = "RJ"


class Rank(Enum):
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    TWO = 15
    BLACK_JOKER = 16
    RED_JOKER = 17
    

CARD_ENUM_STR_MAP = {
    Rank.THREE: "3",
    Rank.FOUR: "4",
    Rank.FIVE: "5",
    Rank.SIX: "6",
    Rank.SEVEN: "7",
    Rank.EIGHT: "8",
    Rank.NINE: "9",
    Rank.TEN: "10",
    Rank.JACK: "J",
    Rank.QUEEN: "Q",
    Rank.KING: "K",
    Rank.ACE: "A",
    Rank.TWO: "2",
    Rank.BLACK_JOKER: "",
    Rank.RED_JOKER: "",
}

def get_card_name(rank: Rank):
    return CARD_ENUM_STR_MAP[rank]


class Pattern(Enum):
    SINGLE = [1]
    PAIR = [2]
    TRIPLE_WITH_SINGLE = [3, 1]
    TRIPLE_WITH_PAIR = [3, 2]
    FOUR_WITH_TWO_SINGLE = [4, 1, 1]
    FOUR_WITH_TWO_PAIR = [4, 2, 2]
    STRAIGHT = [1, 1, 1, 1, 1]
    BOMB = [4]
    ROCKET = [1, 1]
    INVALID = []
