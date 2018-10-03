from random import randint

import GameBoard
from Direction import Direction


class Randomizer:
    @staticmethod
    def orientation() -> Direction:
        return Direction(randint(0, 1))

    @staticmethod
    def position(length: int) -> int:
        return randint(0, GameBoard.GameBoard.GRID_SIZE - length)
