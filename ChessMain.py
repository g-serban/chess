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


# the main driver for our code
# this will handle user input and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode(size=(HEIGHT, WIDTH))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    game_state = ChessEngine.GameState()
    load_images()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()


# responsible for all the graphics within a current game state. The top left square is always light
def draw_game_state(screen, game_state):
    draw_board(screen)  # draw squares on the board
    draw_pieces(screen, game_state.board)  # draw pieces on top of those squares


# draw the squares on the board
def draw_board(screen):
    colors = [p.Color('White'), p.Color('LightBlue')]
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



if __name__ == '__main__':
    main()

















