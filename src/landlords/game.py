from src.landlords.model.deck import Deck
from src.landlords.model.player import Player, LandLord, Peasant
from src.landlords.enum.enum import Pattern
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


    def show_header(self, n: int = 18):
        nums = [f'[{pad(str(i), 3)}]' for i in range(n)]
        print(pad("Starts!", 10), *nums)
        print("=" * 115)

            
    def start(self):
        self.deal_cards()
        
        curr_player = 0
        prev_card = {
            "pattern": Pattern.INVALID,
            "cards": [],
            "player": Player(None),
        }
        
        while True:
            # reset prev if all other players pass
            if prev_card["player"].name == self.players[curr_player].name:
                prev_card["pattern"] = Pattern.INVALID
                prev_card["cards"] = []
                prev_card["player"] = Player(None)
                continue
            
            # show header and player cards
            print(f"{self.players[curr_player].name}'s turn")
            self.show_header(n=len(self.players[curr_player].cards))
            self.players[curr_player].show_cards()
            
            # let player choose cards
            line = input("Choose cards: ")
            if line.strip() == "":
                print("Pass")
                print("-" * 115)
                print()
                curr_player += 1
                if curr_player == 3:
                    curr_player = 0
                continue
            card_indexes = [int(item.strip()) for item in line.split(",")]
            cards = self.players[curr_player].play_cards(card_indexes)
            
            # check if anyone wins
            if self.players[curr_player].count_cards() == 0:
                print("Game over!")
                print(f"{self.players[curr_player].role} wins!")
                print("=" * 115)
                break
            
            # identify, compare and store pattern
            pattern = CardComparator.get_pattern(cards)
            
            if pattern == Pattern.INVALID:
                print("Invalid pattern")
                print("-" * 115)
                print()
                self.players[curr_player].receive_card(cards)
                self.players[curr_player].sort_cards()
                continue
            
            if prev_card["pattern"] == Pattern.INVALID:
                prev_card["pattern"] = pattern
                prev_card["cards"] = cards
                prev_card["player"] = self.players[curr_player]
                print(f"cards played: {cards}\tpattern: {pattern}")
            else:
                is_greater = CardComparator.compare(
                    pattern1=pattern,
                    cards1=cards,
                    pattern2=prev_card["pattern"],
                    cards2=prev_card["cards"],
                )
                if not is_greater:
                    print("Invalid cards")
                    print("-" * 115)
                    print()
                    self.players[curr_player].receive_card(cards)
                    self.players[curr_player].sort_cards()
                    continue
                prev_card["pattern"] = pattern
                prev_card["cards"] = cards
                prev_card["player"] = self.players[curr_player]
                print("cards played:", cards)
            
            print("-" * 115)
            print()
            curr_player += 1
            if curr_player == 3:
                curr_player = 0

def main():
    game = Game()
    game.start()
