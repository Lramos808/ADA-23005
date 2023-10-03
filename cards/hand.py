from dataclasses import dataclass

@dataclass
class Hand:
    
    card_objects:list
    high_card = 0
    hand_type_one = None
    card_values = []
    card_suites = []

    def hand_type(self, list_of_card_obj):
        hand_dic = {"one_pair":0,
                    "two_pair":1,
                    "three_of_a_kind":2,
                    "straight":3,
                    "flush":4,
                    "full_house":5,
                    "four_of_a_kind":6,
                    "straight_flush":7,
                    "royal_flush":8}

        for card_obj in list_of_card_obj:

            self.card_values.append(card_obj.get_card_value())

            if card_obj.get_suit() not in self.card_suites:
                self.card_suites.append(card_obj.get_suit())
                continue

        if max(self.card_values) - min(self.card_values) == 4 and len(self.card_suites) == 1:

            if max(self.card_values) == 14:
                self.hand_type_one = hand_dic.get('royal_flush')
                self.high_card = 14

            if self.card_values.sort() == [2,3,4,5,14]:
                self.hand_type_one = hand_dic.get('staight_flush')
                self.high_card = 5


            self.hand_type_one = hand_dic.get('staight_flush')
            self.high_card = max(self.card_values)


        elif len(set(self.card_values)) == 2:
            for values in self.card_values:
                card_count = self.card_values.count(values)

                if card_count == 4:
                    self.hand_type_one = hand_dic.get('four_of_a_kind')
                    self.high_card = value

                elif card_count == 2 or card_count == 3:
                        self.hand_type_one = hand_dic.get('full_house')
                        self.high_card = max(values)

        elif len(self.card_suites) == 1:
            self.hand_type_one = hand_dic.get('flush')
            self.high_card = max(values)

        elif len(set(self.card_values)) == 3:
                for values in self.card_values:
                    card_count = self.card_values.count(values)
                    if card_count == 3:
                        self.hand_type_one = hand_dic.get('three_of_a_kind')
                        self.high_card = value

        elif len(set(self.card_values)) == 3:
            for values in self.card_values:
                card_count = self.card_values.count(values)
                if card_count == 1:
                    self.card_values.pop(values)
            self.hand_type_one = hand_dic.get('two_pair')
            self.high_card = max(self.card_values)

        elif len(set(self.card_values)) == 4:
            for values in self.card_values:
                card_count = self.card_values.count(values)
                if card_count == 2:
                    self.hand_type_one = hand_dic.get('one_pair')
                    self.high_card = values

        elif len(set(self.card_values)) == 5:
            self.high_card = max(self.card_values)
            
        def get_hand_type_one(self):
            return self.hand_type_one
        
        def get_high_card(self):
            return self.high_card
