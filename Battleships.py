from FiringResult import FiringResult
from GameBoard import GameBoard


def main() -> int:
    board = GameBoard()
    board.set_up()
    while True:
        board.print()
        cell_reference = input(
            "Enter cell to fire at (e.g. A1, B1, ...) or q to quit: ")
        if cell_reference == "q" or cell_reference == "Q":
            print("Bye!")
            return 0
        (row, column) = GameBoard.translate_cell_reference(cell_reference)
        if row == -1:
            print("'", cell_reference, "' is not a valid cell.", sep="")
            continue
        result = board.fire_missile(row, column)
        if result == FiringResult.HIT:
            print("Hit!")
        elif result == FiringResult.MISSED:
            print("Missed!")
        else:
            print("You've already been there!")
        if board.game_is_won:
            break
    board.print()
    print("Congratulations, you Won!")
    return 0


if __name__ == '__main__':
    main()
