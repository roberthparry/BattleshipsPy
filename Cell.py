from CellStatus import CellStatus
from Ship import Ship


class Cell:
    def __init__(self, ship: Ship, cell_status: CellStatus):
        self.ship = ship
        self.cell_status = cell_status

    def symbol(self) -> str:
        if self.cell_status is not CellStatus.SHELLED:
            return " "
        if not self.ship.is_null:
            return "#"
        return "x"
