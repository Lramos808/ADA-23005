from card import Card
# from hand import Hand
import csv

with open('poker.txt', 'r') as f:
    hands = list(csv.reader(f, delimiter=' '))
    
player_hands = []
opponent_hands = []

for hand in hands:
    for card in hand[0:5]:
        new_card = Card(*card)
        new_card.calculate_card_value()
        player_hands.append(new_card)
    
    for card in hand[5:10]:
        new_card = Card(*card)
        new_card.calculate_card_value()
        opponent_hands.append(new_card)
        

print(opponent_hands)