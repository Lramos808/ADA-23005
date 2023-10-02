from dataclasses import dataclass

@dataclass
class Card:
    card: str
    face: str
    suit: str
    card_value: int = 0
    
    def calculate_card_value(self):
        value_convert = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 
                       'Q':12, 'K':13, 'A':14}
        self.card_value = value_convert[self.face]
        
     
    def __str__(self):
        return(self.face + self.suit + ' worth ' + str(self.card_value) + ' points')
    
    
    def __gt__(self, other):
        return self.card_value > other.card_value

    
if __name__ == "__main__":
    new_card = Card( 'A', 'C')
    new_card.calculate_card_value()
    print(new_card)
    
    
