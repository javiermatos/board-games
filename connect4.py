from src.gridboard import GridBoard, GridBoardWithBorder
from src.symbol import Symbol, Color


board = GridBoardWithBorder(6, 7)
winner_length = 4

symbols = (
    Symbol('X', Color.RED),
    Symbol('O', Color.GREEN),
)


def get_symbol_max_length(board: GridBoard, l):
    current_symbol = None
    current_length = 0
    max_symbol = current_symbol
    max_length = current_length

    for cell in l:
        if cell is board.default_value:
            if current_symbol is not None and current_length > max_length:
                max_symbol = current_symbol
                max_length = current_length
            current_symbol = None
            current_length = 0
        elif cell == current_symbol:
            current_length += 1
        elif cell != current_symbol:
            if current_symbol is not None and current_length > max_length:
                max_symbol = current_symbol
                max_length = current_length
            current_symbol = cell
            current_length = 1

    return max_symbol, max_length


def get_winner(board: GridBoard):
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


def game_is_over(board: GridBoard):
    return board.is_full()


step = 0
winner_symbol = None
while not game_is_over(board):
    print(board)

    # Get symbol for player
    symbol = symbols[step % len(symbols)]

    # Action
    c = int(input('Column: '))
    while not (0 <= c < board.columns) or board[0, c] is not board.default_value:
        print('You have to choose a valid position')
        c = int(input('Column: '))
    r = max([r for r in range(board.rows) if board[r, c] == board.default_value])
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
