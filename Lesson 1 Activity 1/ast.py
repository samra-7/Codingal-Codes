import pygame
import random

# --- Game initialization ---
pygame.init()

# --- Screen setup ---
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# --- Colors ---
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# --- Player class ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 40])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed = 5

    def update(self):
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Keep player within screen bounds
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


# --- Bullet class ---
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 15])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # Remove if it moves off screen
        if self.rect.bottom < 0:
            self.kill()


# --- Asteroid class ---
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height:
            self.rect.x = random.randrange(0, screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randint(3, 8)


# --- Sprite Groups ---
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(5):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# --- Scorekeeping ---
score = 0
font_name = pygame.font.match_font('arial')

def draw_text(surface, text, size, x, y):
    """Utility function to draw text on the screen."""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


# --- Game loop ---
running = True
clock = pygame.time.Clock()

while running:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # --- Game logic updates ---
    all_sprites.update()

    # Check for collisions: bullet hits asteroid
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    for hit in hits:
        score += 10
        new_asteroid = Asteroid()
        all_sprites.add(new_asteroid)
        asteroids.add(new_asteroid)

    # Check for collisions: player hits asteroid
    hits = pygame.sprite.spritecollide(player, asteroids, False)
    if hits:
        running = False  # Game over

    # --- Drawing and rendering ---
    screen.fill(black)
    all_sprites.draw(screen)
    draw_text(screen, f"Score: {score}", 18, screen_width // 2, 10)

    # Flip the display to show the new frame
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# --- End of game ---
pygame.quit()
