from typing import List
from src.landlords.model.card import Card
from src.landlords.enum.enum import Pattern, Rank


class CardComparator:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def __get_count_map(cards: List[Card]):
        count_map = {}
        for card in cards:
            if card.value not in count_map:
                count_map[card.value] = 0
            count_map[card.value] += 1
        return count_map
    
    
    @staticmethod
    def get_pattern(cards: List[Card]):
        if not cards or len(cards) == 0:
            return Pattern.INVALID
        length = len(cards)
        cards.sort(key=lambda x : x.value)
        if length == 1:
            return Pattern.SINGLE
        if length == 2:
            if cards[0].value == Rank.BLACK_JOKER.value and cards[1].value == Rank.RED_JOKER.value:
                return Pattern.ROCKET
            if cards[0].value == cards[1].value:
                return Pattern.PAIR
            return Pattern.INVALID
        if length == 4:
            count_map = CardComparator.__get_count_map(cards)
            if len(count_map) == 1:
                return Pattern.BOMB
            if len(count_map) == 2 and 3 in count_map.values():
                return Pattern.TRIPLE_WITH_SINGLE
            return Pattern.INVALID
        if length == 5:
            count_map = CardComparator.__get_count_map(cards)
            if len(count_map) == 2 and 3 in count_map.values():
                return Pattern.TRIPLE_WITH_PAIR
            return Pattern.INVALID
        if length == 6:
            count_map = CardComparator.__get_count_map(cards)
            if 4 in count_map.values():
                return Pattern.FOUR_WITH_TWO_SINGLE
            return Pattern.INVALID
        return Pattern.INVALID
