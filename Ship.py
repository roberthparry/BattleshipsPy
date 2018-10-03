class Ship:
    length: int

    def __init__(self):
        self.hits = 0

    @property
    def is_destroyed(self) -> bool:
        return self.hits == self.length

    @property
    def is_null(self):
        return self.length == 0


class Destroyer(Ship):
    def __init__(self):
        super(Destroyer, self).__init__()
        self.length = 4


class Battleship(Ship):
    def __init__(self):
        super(Battleship, self).__init__()
        self.length = 5


class NullShip(Ship):
    def __init__(self):
        super(NullShip, self).__init__()
        self.length = 0
