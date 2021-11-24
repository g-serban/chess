# main driver file
# responsible for handling user input and displaying the current GameState object

import pygame as p
import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8  # dimension of a chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


# initialize a global dictionary of images. Called one time in main.
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


# draw the squares on the board
def draw_board(screen):
    colors = [p.Color('White'), p.Color('Grey')]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[(row + column) % 2]
            p.draw.rect(screen, color, p.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


# draw the pieces on board using the current GameState.board
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != '--':  # not empty space
                screen.blit(IMAGES[piece], p.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


# responsible for all the graphics within a current game state. The top left square is always light
def draw_game_state(screen, game_state):
    draw_board(screen)  # draw squares on the board
    draw_pieces(screen, game_state.board)  # draw pieces on top of those squares


def position_highlighter(player_clicks, screen, board):
    if len(player_clicks) == 1:
        p.draw.rect(screen, p.Color('LightBlue'), p.Rect(player_clicks[0][1] * SQ_SIZE,
                                                         player_clicks[0][0] * SQ_SIZE, SQ_SIZE, SQ_SIZE))

        if board[player_clicks[0][0]][player_clicks[0][1]] != '--':
            screen.blit(IMAGES[board[player_clicks[0][0]][player_clicks[0][1]]],
                        p.Rect(player_clicks[0][1] * SQ_SIZE, player_clicks[0][0] * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# the main driver for our code
# this will handle user input and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode(size=(HEIGHT, WIDTH))
    clock = p.time.Clock()
    game_state = ChessEngine.GameState()
    load_images()
    running = True
    sq_selected = ()  # no square is selected initially, keep track of the last click of the user  (row, col)
    player_clicks = []  # keep track of the player clicks  ex. [(6, 4), (4, 4)]  [0] being first click [1] being 2nd one

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # x, y location of the mouse

                row = location[1] // SQ_SIZE
                col = location[0] // SQ_SIZE

                if sq_selected == (row, col):
                    sq_selected = ()  # deselect
                    player_clicks = []  # clear player clicks

                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)

                if len(player_clicks) == 2:  # after 2nd click
                    move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
                    game_state.make_move(move)

                    if game_state.board[player_clicks[1][0]][player_clicks[1][1]] != '--':
                        print(move.get_chess_notation())

                    sq_selected = ()
                    player_clicks = []

        draw_game_state(screen, game_state)
        position_highlighter(player_clicks, screen, game_state.board)
        clock.tick(MAX_FPS)
        p.display.flip()


if __name__ == '__main__':
    main()

















