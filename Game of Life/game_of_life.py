import pygame
from time import sleep
from sys import exit
from copy import deepcopy

from pygame.constants import KEYDOWN

def change_state(cell_row, cell_column):   #every 'if' will check a different neighbour separately
    alive_neighbours = 0
    if cell_row - 1 >= 0 and cell_column - 1 >= 0:
        alive_neighbours += board[cell_row - 1][cell_column - 1] #upper left
        print(board[cell_row - 1][cell_column - 1])
    if cell_row - 1 >= 0:
        alive_neighbours += board[cell_row - 1][cell_column] #upper center
        print(board[cell_row - 1][cell_column])
    if cell_row - 1 >= 0 and cell_column + 1 <= 9:
        alive_neighbours += board[cell_row - 1][cell_column + 1] #upper right
        print(board[cell_row - 1][cell_column + 1])
    if cell_column - 1 >= 0:
        alive_neighbours += board[cell_row][cell_column - 1] #center left
        print(board[cell_row][cell_column - 1])
    if cell_column + 1 <= 9:
        alive_neighbours += board[cell_row][cell_column + 1] #center right
        print(board[cell_row][cell_column + 1])
    if cell_row + 1 <= 9 and cell_column - 1 >= 0:
        alive_neighbours += board[cell_row + 1][cell_column - 1] #lower left
        print(board[cell_row + 1][cell_column - 1])
    if cell_row + 1 <= 9:
        alive_neighbours += board[cell_row + 1][cell_column] #lower center
        print(board[cell_row + 1][cell_column])
    if cell_row + 1 <= 9 and cell_column + 1 <= 9:
        alive_neighbours += board[cell_row + 1][cell_column + 1] #lower right
        print(board[cell_row + 1][cell_column + 1])
    
    print("Komórka", cell_row, cell_column, "Ma", alive_neighbours, "Żywych Sąsiadów" )
    if alive_neighbours == 3 and board[cell_row][cell_column] == 0:
        new_board[cell_row][cell_column] = 1
        print("Komórka", cell_row, cell_column, "Się rodzi")
    elif (alive_neighbours < 2 or alive_neighbours > 3) and board[cell_row][cell_column] == 1:
        new_board[cell_row][cell_column] = 0
        print("Komórka", cell_row, cell_column, "Umiera")
    
board = [[0 for i in range(10)] for i in range(10)]
menu = 1

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill("Black")
pygame.display.set_caption("Game of Life")
alive_cell = pygame.Surface((60,60))
alive_cell.fill("White")
dead_cell = pygame.Surface((60,60))
dead_cell.fill("Black")

while True:
    if menu == 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (width, height) = pygame.mouse.get_pos()
                if board[height // 60][width // 60] == 0:
                    board[height // 60][width // 60] = 1
                    screen.blit(alive_cell,((width // 60) * 60, (height // 60) * 60))
                else:
                    board[height // 60][width // 60] = 0
                    screen.blit(dead_cell,((width // 60) * 60, (height // 60) * 60))
            if event.type == KEYDOWN:
                if event.key == pygame.K_s:
                    new_board = deepcopy(board)
                    menu = 0
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
    else:
        screen.fill("Black")
        for i in range(10):
            for j in range(10):
                if board[i][j] == 1:
                    screen.blit(alive_cell,(60 * j, 60 * i))
                change_state(i,j)
        board = deepcopy(new_board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        pygame.display.update()
        sleep(0.1)


    

