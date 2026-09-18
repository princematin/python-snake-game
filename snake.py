import consts


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
        sx = self.get_head()[0]
        sy = self.get_head()[1]

        if self.direction == "RIGHT":
            sx = self.val(sx + 1)
        elif self.direction == "LEFT":
            sx = self.val(sx - 1)
        elif self.direction == "DOWN":
            sy = self.val(sy + 1)
        elif self.direction == "UP":
            sy = self.val(sy - 1)

        if self.game.get_cell((sx, sy)).color == consts.back_color:
            self.cells.append((sx, sy))
            old_tail = self.cells[0]
            self.cells.remove(self.cells[0])
            self.game.get_cell(old_tail).set_color(consts.back_color)
            self.game.get_cell((sx, sy)).set_color(self.color)

        elif self.game.get_cell((sx, sy)).color == consts.fruit_color:
            self.cells.append((sx, sy))
            self.game.get_cell((sx, sy)).set_color(self.color)

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