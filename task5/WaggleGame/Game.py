class Game:
    def __init__(self, level):
        self.level = level
        self.board = self.load_level(level)
        self.size = len(self.board)
        self.selected = None

    def load_level(self, level):
        with open(f'levels/level_{level}.txt', 'r') as file:
            board = [list(map(int, line.strip().split())) for line in file]
        return board

    def is_valid_move(self, x1, y1, x2, y2):
        if self.board[x2][y2] != 0 or self.board[x1][y1] != 1:
            return False
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx == 2 and dy == 0 and self.board[(x1 + x2) // 2][y1] == 1:
            return True
        if dy == 2 and dx == 0 and self.board[x1][(y1 + y2) // 2] == 1:
            return True
        return False

    def move(self, x1, y1, x2, y2):
        if self.is_valid_move(x1, y1, x2, y2):
            self.board[x1][y1] = 0
            self.board[(x1 + x2) // 2][(y1 + y2) // 2] = 0
            self.board[x2][y2] = 1
            self.selected = (x2, y2)

    def check_win(self):
        count = sum(row.count(1) for row in self.board)
        return count == 1
