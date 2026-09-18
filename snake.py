import consts

from game_manager import GameManager

class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size
        if x >= self.game.size:
            x -= self.game.size
        return x

    def next_move(self):
        if self.direction == "RIGHT":
            consts.sx = self.val(self.get_head()[0] + 1)
            consts.sy = self.get_head()[1]
        elif self.direction == "LEFT":
            consts.sx = self.val(self.get_head()[0] - 1)
            consts.sy = self.get_head()[1]
        elif self.direction == "DOWN":
            consts.sy = self.val(self.get_head()[1] + 1)
            consts.sx = self.get_head()[0]
        elif self.direction == "UP":
            consts.sy = self.val(self.get_head()[1] - 1)
            consts.sx = self.get_head()[0]

        if self.game.get_cell((consts.sy, consts.sx)).color == consts.back_color:
            self.cells.append((consts.sx, consts.sy))
            old_tail = self.cells[0]
            self.cells.remove(self.cells[0])
            self.game.get_cell(old_tail).set_color(consts.back_color)
            self.game.get_cell((consts.sy, consts.sx)).set_color(self.color)

        elif self.game.get_cell((consts.sy, consts.sx)).color == consts.fruit_color:
            self.cells.append((consts.sx, consts.sy))
            self.game.get_cell((consts.sy, consts.sx)).set_color(self.color)

        else:
            self.game.kill(self)

    def handle(self, keys):
        for item in keys:
            if item in self.keys:
                if self.keys[item] != self.direction:
                    if not ((self.direction == "UP" and self.keys[item] == "DOWN") or
                            (self.direction == "DOWN" and self.keys[item] == "UP") or
                            (self.direction == "LEFT" and self.keys[item] == "RIGHT") or
                            (self.direction == "RIGHT" and self.keys[item] == "LEFT")):
                        self.direction = self.keys[item]
                        break
            continue