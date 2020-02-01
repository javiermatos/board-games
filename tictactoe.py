from src.gridboard import GridBoard, GridBoardWithBorder
from src.symbol import Symbol, Color


board = GridBoardWithBorder(3)

symbols = (
    Symbol('X', Color.RED),
    Symbol('O', Color.GREEN),
)


def get_winner(board: GridBoard):
    for row in board.get_rows():
        if any(row) and all([row[0] == cell for cell in row]):
            return row[0]
    for column in board.get_columns():
        if any(column) and all([column[0] == cell for cell in column]):
            return column[0]
    for diagonal in [d for d in board.get_diagonals() if len(d) == board.rows]:
        if any(diagonal) and all([diagonal[0] == cell for cell in diagonal]):
            return diagonal[0]
    return None


def game_is_over(board: GridBoard):
    return board.is_full()


step = 0
winner_symbol = None
while not game_is_over(board):
    print(board)

    # Get symbol for player
    symbol = symbols[step % len(symbols)]

    # Action
    r = int(input('Row: '))
    c = int(input('Column: '))
    while not (0 <= r < board.rows) or not (0 <= c < board.columns) or board[r, c] is not board.default_value:
        print('You have to choose a valid position')
        r = int(input('Row: '))
        c = int(input('Column: '))
    board[r, c] = symbol

    step += 1
    winner_symbol = get_winner(board)
    if winner_symbol is not None:
        print(board)
        break


if winner_symbol is not None:
    print('Ha ganado el jugador que utiliza la ficha {}.'.format(winner_symbol))
else:
    print('Ha habido empate.')
