import random
from typing import Any, List, Optional, Tuple

from src.gridboard import GridBoard, GridBoardPretty
from src.symbol import Symbol, Color


board = GridBoardPretty(6, 7)
winner_length = 4


class Player(object):

    def __init__(self, symbol: Symbol) -> None:
        self.symbol = symbol

    def next(self, board: GridBoard) -> int:
        raise NotImplementedError()


class PlayerHuman(Player):

    def next(self, board: GridBoard) -> int:
        c = int(input('Column: '))
        while not (0 <= c < board.columns) or board[0, c] is not board.default_value:
            print('You have to choose a valid position')
            c = int(input('Column: '))
        return c


class PlayerComputerRandom(Player):

    def next(self, board: GridBoard) -> int:
        row = next(board.get_rows())
        c, = random.choices([c for c in range(len(row)) if row[c] == board.default_value])
        return c


players = (
    PlayerHuman(Symbol('X', Color.RED)),
    PlayerComputerRandom(Symbol('O', Color.GREEN)),
)


def game_is_over(board: GridBoard) -> bool:
    return board.is_full()


def get_symbol_max_length(board: GridBoard, line: List[Any]) -> Tuple[Optional[Symbol], int]:
    current_symbol = None
    current_length = 0
    max_symbol = current_symbol
    max_length = current_length

    for cell in line:
        if cell is board.default_value:
            current_symbol = None
            current_length = 0
        elif cell == current_symbol:
            current_length += 1
        elif cell != current_symbol:
            current_symbol = cell
            current_length = 1
        if current_length > max_length:
            max_symbol = current_symbol
            max_length = current_length

    return max_symbol, max_length


def get_winner(board: GridBoard) -> Optional[Symbol]:
    for row in board.get_rows():
        symbol, length = get_symbol_max_length(board, row)
        if length >= winner_length:
            return symbol
    for column in board.get_columns():
        symbol, length = get_symbol_max_length(board, column)
        if length >= winner_length:
            return symbol
    for diagonal in [d for d in board.get_diagonals() if len(d) == board.rows]:
        symbol, length = get_symbol_max_length(board, diagonal)
        if length >= winner_length:
            return symbol
    return None


step = 0
winner_symbol = None
while not game_is_over(board):
    print(board)

    # Get player
    player = players[step % len(players)]

    # Action
    c = player.next(board)
    r = max([r for r in range(board.rows) if board[r, c] == board.default_value])
    board[r, c] = player.symbol

    step += 1
    winner_symbol = get_winner(board)
    if winner_symbol is not None:
        print(board)
        break


if winner_symbol is not None:
    print('Ha ganado el jugador que utiliza la ficha {}.'.format(winner_symbol))
else:
    print('Ha habido empate.')
