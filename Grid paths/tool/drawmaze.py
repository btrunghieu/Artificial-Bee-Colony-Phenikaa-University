import pygame

# Kích thước cửa sổ và ô
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 5

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Drawing Tool")

# Khởi tạo ma trận mê cung
maze = [[0] * (WIDTH // CELL_SIZE) for _ in range(HEIGHT // CELL_SIZE)]

drawing = False  # Trạng thái vẽ (đang vẽ hay không)
start_col = -1  # Cột bắt đầu của đoạn đường đang vẽ

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
            elif event.button == 3:
                start_col, start_row = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
                maze[start_row][start_col] = 0
        elif event.type == pygame.MOUSEMOTION and drawing:
            col, row = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
            if start_col >= 0 and 0 <= col < len(maze[0]) and 0 <= row < len(maze):
                if start_col == col:
                    for r in range(min(start_row, row), max(start_row, row) + 1):
                        maze[r][col] = 1
                else:
                    for c in range(min(start_col, col), max(start_col, col) + 1):
                        maze[row][c] = 1
            start_col, start_row = col, row
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                start_col = -1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                with open("maze.txt", "w") as f:
                    for row in maze:
                        f.write(",".join(map(str, row)) + "\n")

    # Vẽ mê cung
    screen.fill(BLACK)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

# Kết thúc chương trình khi thoát
pygame.quit()
