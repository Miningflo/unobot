class Player:
    def __init__(self, pid, game, hand):
        self.id = pid
        self.game = game
        self.hand = hand

    def __repr__(self):
        return repr(self.hand)

    def is_legal(self, pile, play):
        if play.colour != "black":
            return play.colour == pile.colour or play.value == pile.value
        else:
            if play.value == 13:
                return True
            else:
                hand_colours = set(map(lambda x: x.colour, self.hand))
                return pile.colour not in hand_colours

    def play(self):
        top_card = self.game.stack.pile[-1]
        handsizes = list(map(lambda x: len(x.hand), self.game.players))
        hand_next = handsizes[(self.id + self.game.direction) % (len(self.game.players))]
        hand_prev = handsizes[(self.id - self.game.direction) % (len(self.game.players))]
        print({
            "Top card": top_card,
            "Hand size next player": hand_next,
            "Hand size previous player": hand_prev,
            "My hand": self.hand
        })
