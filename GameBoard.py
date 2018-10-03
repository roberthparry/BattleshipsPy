from typing import List

from Cell import Cell
from CellStatus import CellStatus
from Direction import Direction
from FiringResult import FiringResult
from Randomizer import Randomizer
from Ship import Destroyer, Battleship, Ship, NullShip

column_headers = "abcdefghij"


class GameBoard:
    cell_grid: List[List[Cell]]
    GRID_SIZE = 10

    def __init__(self):
        self.cell_grid = []
        self.destroyer1 = Destroyer()
        self.destroyer2 = Destroyer()
        self.battleship = Battleship()
        self.null_ship = NullShip()

    def set_up(self):
        for row in range(GameBoard.GRID_SIZE):
            self.cell_grid.append([])
            for column in range(GameBoard.GRID_SIZE):
                self.cell_grid[row].append(Cell(self.null_ship, CellStatus.UN_SHELLED))
        self.__place_ship(self.battleship)
        self.__place_ship(self.destroyer1)
        self.__place_ship(self.destroyer2)

    def __place_ship(self, ship: Ship):
        while True:
            direction = Randomizer.orientation()
            position1 = Randomizer.position(ship.length)
            position2 = Randomizer.position(1)
            if self.__can_place_ship(ship, position1, position2, direction):
                break
        self.__do_place_ship(ship, position1, position2, direction)

    def __can_place_ship(self, ship: Ship, position1: int, position2: int, direction: Direction) -> bool:
        if direction == Direction.DOWN:
            for i in range(ship.length):
                if not self.cell_grid[position1 + i][position2].ship.is_null:
                    return False
        else:
            for i in range(ship.length):
                if not self.cell_grid[position2][position1 + i].ship.is_null:
                    return False
        return True

    def __do_place_ship(self, ship: Ship, position1: int, position2: int, direction: Direction):
        if direction == Direction.DOWN:
            for i in range(ship.length):
                self.cell_grid[position1 + i][position2].ship = ship
        else:
            for i in range(ship.length):
                self.cell_grid[position2][position1 + i].ship = ship

    def print(self):
        print("     ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
        print("     ║ A │ B │ C │ D │ E │ F │ G │ H │ I │ J ║")
        print("╔════╬═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╣")
        for row in range(GameBoard.GRID_SIZE):
            self.__print_row(row)

    def __print_row(self, row: int):
        if row == GameBoard.GRID_SIZE - 1:
            print("║ ", row + 1, " ║", sep="", end="")
        else:
            print("║  ", row + 1, " ║", sep="", end="")
        for column in range(GameBoard.GRID_SIZE):
            print(" ", self.cell_grid[row][column].symbol(), " ", sep="", end="")
            if column == GameBoard.GRID_SIZE - 1:
                print("║")
            else:
                print("│", sep="", end="")
        if row == GameBoard.GRID_SIZE - 1:
            print("╚════╩═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")
        else:
            print("╟────╫───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢")

    def fire_missile(self, row: int, column: int):
        cell = self.cell_grid[row][column]
        if cell.cell_status == CellStatus.SHELLED:
            return FiringResult.REPEAT
        cell.cell_status = CellStatus.SHELLED
        if cell.ship.is_null:
            return FiringResult.MISSED
        cell.ship.hits = cell.ship.hits + 1
        return FiringResult.HIT

    @staticmethod
    def translate_cell_reference(cell_reference: str) -> (int, int):
        if cell_reference == "":
            return -1, -1
        reference = cell_reference.lower()
        try:
            index = column_headers.index(reference[0])
        except ValueError:
            return -1, -1
        column = index
        try:
            number = int(reference[1:len(reference)])
        except ValueError:
            return -1, -1
        row = number - 1
        if row < 0 or row >= GameBoard.GRID_SIZE:
            return -1, -1
        return row, column

    @property
    def game_is_won(self):
        return self.battleship.is_destroyed and self.destroyer1.is_destroyed and self.destroyer2.is_destroyed
