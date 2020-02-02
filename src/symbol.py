
class Character(object):
    PERSON = '웃'
    FULL_BLOCK = '█'
    SNOWMAN = '☃'
    SKULL_AND_CROSSBONES = '☠'
    RADIOACTIVE_SIGN = '☢'
    YIN_YANG = '☯'
    WHITE_SMILING_FACE = '☺'
    WHITE_CHESS_KING = '♔'
    WHITE_CHESS_QUEEN = '♕'
    WHITE_CHESS_ROOK = '♖'
    WHITE_CHESS_BISHOP = '♗'
    WHITE_CHESS_KNIGHT = '♘'
    WHITE_CHESS_PAWN = '♙'
    BLACK_CHESS_KING = '♚'
    BLACK_CHESS_QUEEN = '♛'
    BLACK_CHESS_ROOK = '♜'
    BLACK_CHESS_BISHOP = '♝'
    BLACK_CHESS_KNIGHT = '♞'
    BLACK_CHESS_PAWN = '♟'
    WHEELCHAIR_MAN = '♿'
    DICE_FACE_1 = '⚀'
    DICE_FACE_2 = '⚁'
    DICE_FACE_3 = '⚂'
    DICE_FACE_4 = '⚃'
    DICE_FACE_5 = '⚄'
    DICE_FACE_6 = '⚅'

    BOX_DRAWINGS_HEAVY_HORIZONTAL = '━'
    BOX_DRAWINGS_HEAVY_VERTICAL = '┃'
    BOX_DRAWINGS_HEAVY_DOWN_AND_RIGHT = '┏'
    BOX_DRAWINGS_HEAVY_DOWN_AND_LEFT = '┓'
    BOX_DRAWINGS_HEAVY_UP_AND_RIGHT = '┗'
    BOX_DRAWINGS_HEAVY_UP_AND_LEFT = '┛'
    BOX_DRAWINGS_HEAVY_VERTICAL_AND_RIGHT = '┣'
    BOX_DRAWINGS_HEAVY_VERTICAL_AND_LEFT = '┫'
    BOX_DRAWINGS_HEAVY_DOWN_AND_HORIZONTAL = '┳'
    BOX_DRAWINGS_HEAVY_UP_AND_HORIZONTAL = '┻'
    BOX_DRAWINGS_HEAVY_VERTICAL_AND_HORIZONTAL = '╋'


class Color(object):
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Symbol(object):

    def __init__(self, character: str, color: str) -> None:
        self.character = character
        self.color = color

    def __str__(self) -> str:
        return self.color + self.character + Color.END

    def __repr__(self) -> str:
        return self.__str__()
