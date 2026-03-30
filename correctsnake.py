
import pygame
import random

#Initialize Pygame
pygame.init()

#Set up display
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Game variables
cell_size = 20
snake_speed = 10
clock = pygame.time.Clock()

#Snake and food
snake = [(width // 2, height // 2)]
snake_direction = "RIGHT"
food_position = (
    random.randint(0, (width - cell_size) // cell_size) * cell_size,
    random.randint(0, (height - cell_size) // cell_size) * cell_size
)
score = 0

#Font for score display
font = pygame.font.SysFont(None, 36)

#Game loop
running = True
while running:
    clock.tick(snake_speed)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

# Move the snake
    snake_head = list(snake[0])
    if snake_direction == "UP":
        snake_head[1] -= cell_size
    elif snake_direction == "DOWN":
        snake_head[1] += cell_size
    elif snake_direction == "LEFT":
        snake_head[0] -= cell_size
    elif snake_direction == "RIGHT":
        snake_head[0] += cell_size

    snake.insert(0, tuple(snake_head))

# Check for collision with food
    if snake[0] == food_position:
        score += 1
        food_position = (
            random.randint(0, (width - cell_size) // cell_size) * cell_size,
            random.randint(0, (height - cell_size) // cell_size) * cell_size
        )
    else:
        snake.pop()

# Check collision with self
    if snake[0] in snake[1:]:
        running = False
# Check collision with walls
    if (snake[0][0] < 0 or snake[0][0] >= width or
            snake[0][1] < 0 or snake[0][1] >= height):
        running = False

    # Drawing
    window.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(window, GREEN, (pos[0], pos[1], cell_size, cell_size))
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], cell_size, cell_size))

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
