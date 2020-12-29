import random


class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.value = value

    def getimg(self):
        return "./cards/" + self.colour + "/" + str(self.value) + ".png"

    def __repr__(self):
        translation = {
            10: "Skip",
            11: "Switch",
            12: "TakeTwo",
            13: "Wild",
            14: "TakeFour"
        }
        if self.value in translation.keys():
            return self.colour + "-" + translation[self.value]
        return self.colour + "-" + str(self.value)


class Stack:
    def __init__(self):
        self.stack = self.__create()
        self.pile = []

    def draw(self, n=1):
        draws = []
        for i in range(n):
            if self.stack is None:
                self.__reshuffle()
            draws.append(self.stack.pop(0))
        return draws

    def __reshuffle(self):
        pile = self.pile.pop()
        for i, card in enumerate(self.pile):
            if card.value >= 13:
                card.colour = "black"
                self.pile[i] = card
        random.shuffle(self.pile)
        self.stack = self.pile
        self.pile = [pile]

    def play(self, card):
        self.pile.append(card)

    def __create(self):
        stack = []
        for c in ["red", "blue", "green", "yellow"]:
            for i in range(1, 13):
                for j in range(2):
                    stack.append(Card(c, i))
            stack.append(Card(c, 0))
            stack.append(Card("black", 13))
            stack.append(Card("black", 14))
        random.shuffle(stack)
        return stack

    def draw_start(self):
        draw = self.draw()[0]
        while draw.colour == "black":
            self.play(draw)
            draw = self.draw()[0]
        self.play(draw)
