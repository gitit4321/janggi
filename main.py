import pygame

from janggi.board import Board
from janggi.constants import WIDTH, HEIGHT, SQUARE_SIZE, FPS
from janggi.game_pieces import * 
from janggi.janggiGame import JanggiGame

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Janggi')

def get_mouse_pos(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return col, row

def main():
    run = True
    clock = pygame.time.Clock()
    game = JanggiGame(WIN)

    while run:
        clock.tick(FPS)

        if game.get_game_state() != 'UNFINISHED':
            print(game.get_game_state())
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = get_mouse_pos(pos)
                game.select((col, row))
            
        game.update()


    pygame.quit()

main()
