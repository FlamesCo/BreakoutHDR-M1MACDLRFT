# Importing the required Pygame library
import pygame
import sys

# Initializing Pygame
pygame.init()

# Defining constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_SIZE = 10
BLOCK_WIDTH, BLOCK_HEIGHT = 50, 20
PADDLE_MOVE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 5, -5
FPS = 60

# Setting up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Breakout Game')

# Defining colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Defining the paddle
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Defining the ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y

# Defining the blocks
blocks = [pygame.Rect(x * BLOCK_WIDTH, y * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT) for x in range(SCREEN_WIDTH // BLOCK_WIDTH) for y in range(3)]

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)  # Fill the background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_MOVE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.x += PADDLE_MOVE_SPEED
    
    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.colliderect(paddle):
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1

    # Ball collision with blocks
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y *= -1
            break
    
    # Ball out of bounds
    if ball.top > SCREEN_HEIGHT:
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y

    # Drawing
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, GREEN, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    
    # Refresh the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(FPS)
