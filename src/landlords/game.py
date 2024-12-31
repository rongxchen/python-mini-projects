from src.landlords.model.deck import Deck
from src.landlords.model.player import Player, LandLord, Peasant
from src.landlords.comparator.card_comparator import CardComparator
from typing import List
     
    
def pad(s: str, length: int):
    return " " * (length - len(s)) + s

        
class Game:
    
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players: List[Player] = [LandLord("landlord"), Peasant("peasant 1"), Peasant("peasant 2")]
    
    
    def deal_cards(self):
        curr_index = 0
        while self.deck.has_next():
            self.players[curr_index].receive_card(self.deck.deal())
            curr_index += 1
            if curr_index == 3:
                curr_index = 0
                
        for player in self.players:
            player.sort_cards()


    def show_header(self):
        nums = [f'[{pad(str(i), 3)}]' for i in range(18)]
        print(pad("Starts!", 10), *nums)
        print("=" * 115)

            
    def start(self):
        self.deal_cards()
        curr_player = 0
        while True:
            print(f"{self.players[curr_player].name}'s turn")
            self.show_header()
            self.players[curr_player].show_cards()
            card_indexes = [int(item.strip()) for item in input("Choose cards: ").split(",")]
            cards = self.players[curr_player].play_cards(card_indexes)
            pattern = CardComparator.get_pattern(cards)
            print(pattern.name)
            print("-" * 115)
            curr_player += 1
            if curr_player == 3:
                curr_player = 0

def main():
    game = Game()
    game.start()
