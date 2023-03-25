class Position:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.busy = False
        self.poss1 = None
        self.poss2 = None
        self.poss3 = None
        self.value = None

    def set_busy(self, busy_value):
        self.busy = busy_value

    def possible_moves(self, poss1, poss2, poss3):
        self.poss1 = poss1
        self.poss2 = poss2
        self.poss3 = poss3

    def get_position(self):
        return self.x, self.y
    
    def get_value(self):
        return self.value