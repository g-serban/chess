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

    def make_move(self, move):  # takes a Move as parameter and executes it (doesn't work for castling, en peasant and promoting)
        if self.board[move.start_row][move.start_col] != '--':
            self.board[move.start_row][move.start_col] = '--'
            self.board[move.end_row][move.end_col] = move.piece_moved
            self.move_log.append(move)  # log the move
            self.white_to_move = not self.white_to_move  # swap players

    def undo_move(self):  # undo the last move made
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move  # switch turns back

    def get_valid_moves(self):  # all moves considering checks
        return self.get_all_possible_moves()  # for now, we will not worry about checks at all

    def get_all_possible_moves(self):  # all moves without considering checks
        # moves = []
        moves = [Move((6, 4), (4, 4), self.board)]  # for testing purposes only
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]  # accessing the first character of the square: w, b or -
                if (turn == 'w' and self.white_to_move) and (turn == 'b' and not self.white_to_move):
                    piece = self.board[row][col][1]  # accessing the second character of the square: piece or -

                    if piece == 'p':
                        self.get_pawn_moves(row, col, moves)

                    elif piece == 'R':
                        self.get_rock_moves(row, col, moves)

        return moves

    def get_pawn_moves(self, row, col, moves):  # get all the pawn moves for the pawn located at row, col
        pass                                    # and add these moves to the list

    def get_rock_moves(self, row, col, moves):
        pass


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
        self.piece_captured = board[self.end_row][self.end_col]  # if no piece captured, '--'
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.move_id, '--> move id')

    def get_chess_notation(self):  # e.g. a1 - d4
        return self.get_rank_file(self.start_row, self.start_col) + '-' + self.get_rank_file(self.end_row, self.end_col)
        # TODO they are inversed

    def get_rank_file(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]

    # overriding the equals method  || we need this to use the Move class in the get all possible moves method
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id


