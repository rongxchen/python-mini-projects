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
    def __get_card_value_by_count(count_map: dict, count: int):
        for k, v in count_map.items():
            if v == count:
                return k
        return None
    
    
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
    
    
    @staticmethod
    def compare(pattern1: Pattern,
                cards1: List[Card],
                pattern2: Pattern,
                cards2: List[Card]):
        """ compare two card patterns 
        
        Args:
            pattern1 (Pattern): new pattern
            cards1 (List[Card]): new cards
            pattern2 (Pattern): old pattern
            cards2 (List[Card]): old cards
        
        Returns:
            bool: True if cards1 can beat cards2, False otherwise
        """
        if pattern1 == Pattern.INVALID or pattern2 == Pattern.INVALID:
            return False
        if pattern1 != pattern2:
            if pattern1 == Pattern.ROCKET:
                return True
            if pattern1 == Pattern.BOMB and pattern2 != Pattern.ROCKET:
                return True
            return False
        else:
            pattern = pattern1
            if pattern == Pattern.SINGLE:
                return cards1[0].value > cards2[0].value
            count_map1 = CardComparator.__get_count_map(cards1)
            count_map2 = CardComparator.__get_count_map(cards2)
            if pattern == Pattern.PAIR:
                return CardComparator.__get_card_value_by_count(count_map1, 2) > CardComparator.__get_card_value_by_count(count_map2, 2)
            if pattern == Pattern.TRIPLE_WITH_SINGLE or pattern == Pattern.TRIPLE_WITH_PAIR:
                return CardComparator.__get_card_value_by_count(count_map1, 3) > CardComparator.__get_card_value_by_count(count_map2, 3)
            if pattern == Pattern.FOUR_WITH_TWO_SINGLE or pattern == Pattern.FOUR_WITH_TWO_PAIR or pattern == Pattern.BOMB:
                return CardComparator.__get_card_value_by_count(count_map1, 4) > CardComparator.__get_card_value_by_count(count_map2, 4)
            return False            
