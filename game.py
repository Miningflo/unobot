from stack import Stack
from player import Player


class Game:
    def __init__(self, n):
        self.stack = Stack()
        self.direction = 1
        self.players = []
        for i in range(n):
            self.players.append(Player(i, self, self.stack.draw(7)))
        self.stack.draw_start()
        self.game()

    def game(self):
        turn = 0
        while 0 not in list(map(lambda x: len(x.hand), self.players)):
            top_card = self.stack.pile[-1].value
            if top_card > 9:
                if top_card == 10:
                    pass
                elif top_card == 11:
                    self.direction *= -1
                elif top_card == 12:
                    self.players[turn].hand.extend(self.stack.draw(2))
                elif top_card == 13:
                    self.players[turn].play()
                elif top_card == 14:
                    self.players[turn].hand.extend(self.stack.draw(4))
            else:
                self.players[turn].play()
            turn = (turn + self.direction) % (len(self.players))


game = Game(6)
