# This class is responsible for storing all the information about the current state of the chess game
# also responsible for determining the valid moves at the current state
# also keep a move log


class GameState:

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
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.white_to_move = True
        self.move_log = []

    def make_move(self, move):
        if self.board[move.start_row][move.start_col] != '--':
            self.board[move.start_row][move.start_col] = '--'
            self.board[move.end_row][move.end_col] = move.piece_moved
            self.move_log.append(move)  # log the move
            self.white_to_move = not self.white_to_move  # swap players


class Move:

    # maps keys to values
    # key: value
    ranks_to_rows = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}  # reversing the ranks_to_row dict
    files_to_cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}  # reversing the files_to_cols dict

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):  # e.g. a1 - d4
        return self.get_rank_file(self.start_row, self.start_col) + '-' + self.get_rank_file(self.end_row, self.end_col)
        # TODO they are inversed

    def get_rank_file(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]

