import random
from typing import Optional, Tuple

from src.gridboard import GridBoard, GridBoardPretty
from src.symbol import Symbol, Color


board = GridBoardPretty(3)


class Player(object):

    def __init__(self, symbol: Symbol) -> None:
        self.symbol = symbol

    def next(self, board: GridBoard) -> Tuple[int, int]:
        raise NotImplementedError()


class PlayerHuman(Player):

    def next(self, board: GridBoard) -> Tuple[int, int]:
        r, c = map(int, input('Row and column: ').split())
        while not (0 <= r < board.rows) or not (0 <= c < board.columns) or board[r, c] is not board.default_value:
            print('You have to choose a valid position')
            r, c = map(int, input('Row and column: ').split())
        return r, c


class PlayerComputerRandom(Player):

    def next(self, board: GridBoard) -> Tuple[int, int]:
        (r, c), = random.choices(list(board.get_empty_rows_columns()))
        return r, c


players = (
    PlayerHuman(Symbol('X', Color.RED)),
    PlayerComputerRandom(Symbol('O', Color.GREEN)),
)


def game_is_over(board: GridBoard) -> bool:
    return board.is_full()


def get_winner(board: GridBoard) -> Optional[Symbol]:
    for row in board.get_rows():
        if all([(cell != board.default_value and cell == row[0]) for cell in row]):
            return row[0]
    for column in board.get_columns():
        if all([(cell != board.default_value and cell == column[0]) for cell in column]):
            return column[0]
    for diagonal in [d for d in board.get_diagonals() if len(d) == board.rows]:
        if all([(cell != board.default_value and cell == diagonal[0]) for cell in diagonal]):
            return diagonal[0]
    return None


step = 0
winner_symbol = None
print(board)
while not game_is_over(board):

    # Get player
    player = players[step % len(players)]

    # Action
    r, c = player.next(board)
    board[r, c] = player.symbol

    print(board)

    step += 1
    winner_symbol = get_winner(board)
    if winner_symbol is not None:
        print('Ha ganado el jugador que utiliza la ficha {}.'.format(winner_symbol))
        break

else:
    print('Ha habido empate.')
