from typing import Any, Callable, Generator, List, Tuple

from .symbol import Character


class EmptyCell(object):

    def __str__(self) -> str:
        return ' '

    def __repr__(self) -> str:
        return ' '


EMPTY_CELL = EmptyCell()


class GridBoard(object):

    def __init__(self, rows: int, columns: int = None, default_value: Any = EMPTY_CELL) -> None:
        if columns is None:
            columns = rows

        self.rows = rows
        self.columns = columns
        self.default_value = default_value
        self.grid = [
            [default_value for c in range(columns)]
            for r in range(rows)
        ]

    # def get(self, r: int, c: int) -> Any:
    #     return self.grid[r][c]
    #
    # def set(self, r: int, c: int, value: Any) -> None:
    #     self.grid[r][c] = value

    def get_rows(self) -> Generator[List[Any], None, None]:
        for row in self.grid:
            yield row

    def get_columns(self) -> Generator[List[Any], None, None]:
        for c in range(self.columns):
            column = []
            for r in range(self.rows):
                column.append(self.grid[r][c])
            yield column

    def get_backward_diagonals(self) -> Generator[List[Any], None, None]:
        b = [None] * (len(self.grid) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate(self.get_rows())]
        yield from ([c for c in r if c is not None] for r in zip(*grid))

    def get_forward_diagonals(self) -> Generator[List[Any], None, None]:
        b = [None] * (len(self.grid) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate(self.get_rows())]
        yield from ([c for c in r if c is not None] for r in zip(*grid))

    def get_diagonals(self) -> Generator[List[Any], None, None]:
        yield from self.get_backward_diagonals()
        yield from self.get_forward_diagonals()

    def is_empty(self) -> bool:
        for row in self.grid:
            for cell in row:
                if cell != self.default_value:
                    return False
        return True

    def is_full(self) -> bool:
        for row in self.grid:
            for cell in row:
                if cell == self.default_value:
                    return False
        return True

    def get_filter_rows_columns(self, f: Callable) -> Generator[Tuple[int, int], None, None]:
        for r in range(self.rows):
            for c in range(self.columns):
                if f(self.grid[r][c]):
                    yield r, c

    def get_empty_rows_columns(self) -> Generator[Tuple[int, int], None, None]:
        yield from self.get_filter_rows_columns(lambda cell: cell == self.default_value)

    def get_non_empty_rows_columns(self) -> Generator[Tuple[int, int], None, None]:
        yield from self.get_filter_rows_columns(lambda cell: cell != self.default_value)

    def __getitem__(self, key: Tuple[int, int]) -> Any:
        r, c = key
        return self.grid[r][c]

    def __setitem__(self, key: Tuple[int, int], value: Any) -> None:
        r, c = key
        self.grid[r][c] = value

    def __str__(self) -> str:
        newline = '\n'
        space = ' '
        empty = ''
        return newline.join([
            empty.join([str(c) for c in r])
            for r in self.grid
        ])


class GridBoardPretty(GridBoard):

    def __str__(self) -> str:
        edge_tl = Character.BOX_DRAWINGS_HEAVY_DOWN_AND_RIGHT
        edge_tr = Character.BOX_DRAWINGS_HEAVY_DOWN_AND_LEFT
        edge_bl = Character.BOX_DRAWINGS_HEAVY_UP_AND_RIGHT
        edge_br = Character.BOX_DRAWINGS_HEAVY_UP_AND_LEFT
        mid_l = Character.BOX_DRAWINGS_HEAVY_VERTICAL_AND_RIGHT
        mid_c = Character.BOX_DRAWINGS_HEAVY_VERTICAL_AND_HORIZONTAL
        mid_r = Character.BOX_DRAWINGS_HEAVY_VERTICAL_AND_LEFT
        mid_t = Character.BOX_DRAWINGS_HEAVY_DOWN_AND_HORIZONTAL
        mid_b = Character.BOX_DRAWINGS_HEAVY_UP_AND_HORIZONTAL
        lin_h = Character.BOX_DRAWINGS_HEAVY_HORIZONTAL
        lin_v = Character.BOX_DRAWINGS_HEAVY_VERTICAL
        newline = '\n'
        space = ' '

        row_head = space + ''.join([space + str(i) for i in range(self.columns)]) + space + newline
        row_top = space + edge_tl + lin_h + ((mid_t + lin_h) * (self.columns - 1)) + edge_tr + newline
        row_mid = space + mid_l + lin_h + ((mid_c + lin_h) * (self.columns - 1)) + mid_r + newline
        row_bot = space + edge_bl + lin_h + ((mid_b + lin_h) * (self.columns - 1)) + edge_br
        rows = [
            str(i) + lin_v + lin_v.join([str(c) for c in r]) + lin_v + newline
            for i, r in enumerate(self.grid)
        ]
        return row_head + row_top + row_mid.join(rows) + row_bot
