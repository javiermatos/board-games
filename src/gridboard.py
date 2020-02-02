from .symbol import Character


class GridBoard(object):

    def __init__(self, rows, columns=None, default_value=None):
        if columns is None:
            columns = rows

        self.rows = rows
        self.columns = columns
        self.default_value = default_value
        self.grid = [
            [default_value for c in range(columns)]
            for r in range(rows)
        ]

    # def get(self, r, c):
    #     return self.grid[r][c]
    #
    # def set(self, r, c, value):
    #     self.grid[r][c] = value

    def get_rows(self):
        for row in self.grid:
            yield row

    def get_columns(self):
        for c in range(self.columns):
            column = []
            for r in range(self.rows):
                column.append(self.grid[r][c])
            yield column

    def get_backward_diagonals(self):
        b = [None] * (len(self.grid) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate(self.get_rows())]
        return [[c for c in r if c is not None] for r in zip(*grid)]

    def get_forward_diagonals(self):
        b = [None] * (len(self.grid) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate(self.get_rows())]
        return [[c for c in r if c is not None] for r in zip(*grid)]

    def get_diagonals(self):
        return self.get_backward_diagonals() + self.get_forward_diagonals()

    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell != self.default_value:
                    return False
        return True

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == self.default_value:
                    return False
        return True

    def __getitem__(self, key):
        r, c = key
        return self.grid[r][c]

    def __setitem__(self, key, value):
        r, c = key
        self.grid[r][c] = value

    def __str__(self):
        newline = '\n'
        space = ' '
        empty = ''
        return newline.join([
            empty.join([str(c) if c is not self.default_value else space for c in r])
            for r in self.grid
        ])


class GridBoardPretty(GridBoard):

    def __str__(self):
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
            str(i) + lin_v + lin_v.join([str(c) if c is not None else space for c in r]) + lin_v + newline
            for i, r in enumerate(self.grid)
        ]
        return row_head + row_top + row_mid.join(rows) + row_bot
