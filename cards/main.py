from card import Card
from hand import Hand
import csv

with open('poker.txt', 'r') as f:
    hands = list(csv.reader(f, delimiter=' '))
    
player_hands = [Card(card) for card in hand[0:5] for hand in hands]

opponent_hands = [Card(card) for card in hand[5:10] for hand in hands]

print(player_hands)