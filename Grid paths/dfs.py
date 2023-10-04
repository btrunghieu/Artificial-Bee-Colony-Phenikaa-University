import pygame
import numpy as np
import random
from collections import deque

WIDTH, HEIGHT = 600, 600
NUM_COLS, NUM_ROWS = 120, 120

CELL_WIDTH = WIDTH // NUM_COLS
CELL_HEIGHT = HEIGHT // NUM_ROWS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  

clock = pygame.time.Clock()  

with open('main\map\level2.txt', 'r') as f:
    maze = [[int(num) for num in line.split(',')] for line in f]

player_row, player_col = 0, 0

path = {}
path[(player_row, player_col)] = [(player_col * CELL_WIDTH + CELL_WIDTH // 2, player_row * CELL_HEIGHT + CELL_HEIGHT // 2)]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

stack = [(player_row, player_col)]
visit = set((player_row, player_col))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #BFS
    if ((len(stack)>0) and player_row !=NUM_ROWS-1):
        x, y = stack[len(stack)-1] 
        stack.remove(stack[len(stack) - 1])
        player_row, player_col = x,y
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]: #[(x, y-1), (x + 1, y), (x, y + 1), (x-1, y)]
            if 0 <= nx < NUM_COLS and 0 <= ny < NUM_ROWS and maze[nx][ny] != 1:
                coord = nx, ny
                if coord not in visit:
                    if (x, y) in path: 
                        new_path = path[(x, y)].copy()
                        new_path.append((ny * CELL_WIDTH + CELL_WIDTH // 2, nx * CELL_HEIGHT + CELL_HEIGHT // 2))
                        path[coord] = new_path
                    else:  
                        path[coord] = [(y * CELL_WIDTH + CELL_WIDTH // 2, x * CELL_HEIGHT + CELL_HEIGHT // 2)]
                    visit.add(coord)
                    stack.append(coord)

    screen.fill(WHITE)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

    if len(path[(player_row, player_col)]) > 1:
        pygame.draw.lines(screen, BLUE, False, path[(player_row, player_col)], 2)

    pygame.draw.circle(screen, RED, (player_col * CELL_WIDTH + CELL_WIDTH // 2, player_row * CELL_HEIGHT + CELL_HEIGHT // 2), CELL_WIDTH // 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
