from src.landlords.model.deck import Deck
from src.landlords.model.player import Player, LandLord, Peasant
from typing import List
     
        
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

            
    def start(self):
        self.deal_cards()
        for player in self.players:
            player.show_cards()


def main():
    game = Game()
    game.start()
