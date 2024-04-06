import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5

class Food:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Bouncing Ball")

# Create a ball object
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, WHITE)

# Create some food objects
foods = []
for i in range(10):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    radius = 5
    color = (255, 0, 0)
    food = Food(x, y, radius, color)
    foods.append(food)

# Create a clock object
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Handle keyboard input to move the ball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ball.move(0, -5)
    if keys[pygame.K_a]:
        ball.move(-5, 0)
    if keys[pygame.K_s]:
        ball.move(0, 5)
    if keys[pygame.K_d]:
        ball.move(5, 0)

    # Bounce the ball off the walls
    if ball.x < ball.radius or ball.x > SCREEN_WIDTH - ball.radius:
        ball.move(-ball.dx, 0)
    if ball.y < ball.radius or ball.y > SCREEN_HEIGHT - ball.radius:
        ball.move(0, -ball.dy)

    # Check for collision with food
    for food in foods:
        if ball.radius >= ball.distance_to(food):
            foods.remove(food)

    # --- Drawing code should go here
    screen.fill(BLACK)
    ball.draw(screen)
    for food in foods:
        food.draw(screen)

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
d