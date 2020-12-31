from pprint import pprint


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
        playable = [card for card in self.hand if self.is_legal(top_card, card)]
        info = {
            "top": top_card,
            "size_next": hand_next,
            "size_prev": hand_prev,
            "hand": self.hand,
            "playable": playable
        }
        if not playable:
            self.hand.extend(self.game.stack.draw())
            info["hand"] = self.hand
            info["playable"] = [card for card in self.hand if self.is_legal(top_card, card)]
        self.logic(info)

    def logic(self, info):
        if info["playable"]:
            self.play_card(info["playable"][0])

    def play_card(self, card, colour="red"):
        self.hand.remove(card)
        if card.colour == "black":
            card.colour = colour
        value = card.value
        if value == 10:  # skip
            self.game.turn = self.game.get_next()
        elif value == 11:  # reverse
            self.game.direction *= -1
        elif value == 12:  # take 2
            self.game.players[self.game.get_next()].hand.extend(self.game.stack.draw(2))
        elif value == 14:  # take 4
            self.game.players[self.game.get_next()].hand.extend(self.game.stack.draw(4))
        self.game.stack.play(card)
