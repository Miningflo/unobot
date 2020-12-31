from stack import Stack
from player import Player


class Game:
    def __init__(self, n):
        self.stack = Stack()
        self.direction = 1
        self.turn = 0
        self.players = []
        for i in range(n):
            self.players.append(Player(i, self, self.stack.draw(7)))
        self.stack.draw_start()
        self.game()

    def game(self):
        iteration = 0
        while 0 not in list(map(lambda x: len(x.hand), self.players)):
            iteration += 1
            self.players[self.turn].play()
            self.turn = self.get_next()
        print("finish", iteration)
        print("Player " + str([player.id for player in self.players if not player.hand][0]) + " won")

    def get_next(self):
        return (self.turn + self.direction) % (len(self.players))


game = Game(6)
