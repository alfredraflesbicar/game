
import pygame

# Inisialisasi Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

clock = pygame.time.Clock()

# Player
player_size = 20
player_color = (255, 0, 0)
player = pygame.Rect(40, 40, player_size, player_size)
speed = 5

# Maze Walls
walls = [
    pygame.Rect(0, 0, WIDTH, 20),
    pygame.Rect(0, 0, 20, HEIGHT),
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    pygame.Rect(WIDTH - 20, 0, 20, HEIGHT),
    pygame.Rect(100, 0, 20, 380),
    pygame.Rect(200, 100, 300, 20),
    pygame.Rect(300, 200, 20, 200),
    pygame.Rect(100, 400, 400, 20),
    pygame.Rect(500, 250, 20, 230)
]

# Tujuan
goal = pygame.Rect(580, 420, 40, 40)

running = True
while running:
    clock.tick(30)
    win.fill((255, 255, 255))

    keys = pygame.key.get_pressed()
    move_x = move_y = 0

    if keys[pygame.K_LEFT]:
        move_x = -speed
    if keys[pygame.K_RIGHT]:
        move_x = speed
    if keys[pygame.K_UP]:
        move_y = -speed
    if keys[pygame.K_DOWN]:
        move_y = speed

    new_player = player.move(move_x, move_y)
    if not any(new_player.colliderect(w) for w in walls):
        player = new_player

    # Gambar tembok
    for wall in walls:
        pygame.draw.rect(win, (0, 0, 0), wall)

    # Gambar player dan goal
    pygame.draw.rect(win, player_color, player)
    pygame.draw.rect(win, (0, 255, 0), goal)

    if player.colliderect(goal):
        font = pygame.font.SysFont(None, 60)
        text = font.render('You Win!', True, (0, 128, 0))
        win.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 30))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()

pygame.quit()
