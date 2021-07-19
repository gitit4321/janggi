import pygame

from janggi.board import Board
from janggi.constants import WIDTH, HEIGHT, SQUARE_SIZE, FPS, BLACK, WOOD
from janggi.game_pieces import * 
from janggi.janggiGame import JanggiGame

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT+90))   # WIDTH and HEIGHT are board dimensions. The +90 is to create room for game state at the bottom of the board
pygame.display.set_caption('Janggi')

def get_mouse_pos(pos):
    """
    Returns the x and y coordnates of the current mouse position in tuple.
    """
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return col, row

def main():
    run = True
    clock = pygame.time.Clock()
    game = JanggiGame(WIN)
    
    # main game loop
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:               # check for window closure and end game if True
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:    # check for mouse clicks 
                pos = pygame.mouse.get_pos()            # get mouse position in game window
                col, row = get_mouse_pos(pos)
                if col <= 8 and row <= 9:               # prevents error being thrown from clicking outside of board limits
                    game.select((col, row))
            
        game.update()                   
        pygame.display.update()
        
    pygame.quit()

main()
