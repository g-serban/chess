# This class is responsible for storing all the information about the current state of the chess game
# also responsible for determining the valid moves at the current state
# also keep a move log

class GameState():
    def __init__(self):
        # board is an 8x8 2d list, each element of the list has 2 characters
        # the 1st ch represents the color of the piece 'b' or 'w'
        # the 2nd ch represents the type of the piece (king, queen, rook, bishop, knight, pawn)
        # the -- string represents an empty space with no piece
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.white_to_move = True
        self.move_log = []
