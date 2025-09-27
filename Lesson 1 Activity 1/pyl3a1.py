# Import Libraries
import pygame
import random

# Initialize RGB of colours to be used
surf_color = (0, 142, 204)
color = (0, 0, 0)

# Object class for Sprites
class Sprite(pygame.sprite.Sprite):
	# Constructor
    def __init__(self, color, height, width):
        super().__init__()
		# Set the surface
        self.image = pygame.Surface([width, height])
		# Fill the color in surface
        self.image.fill(surf_color)
		# Draw a rectangle on this surface/background
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
		# Get rect object from image/background
        self.rect = self.image.get_rect()
  
pygame.init()

# Set the Pygame screen and title
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Creating Sprite")

# Creating a Sprite Group
all_sprites_list = pygame.sprite.Group()

# Create 1st Sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
# Add a sprite in the Sprite Group
all_sprites_list.add(sp1)

# Add 2nd sprite
# sp2 = Sprite((255,0,0), 20, 30)
# sp2.rect.x = random.randint(0,480)
# sp2.rect.y = random.randint(0,370)
# all_sprites_list.add(sp2)

exit = True
clock = pygame.time.Clock()
  
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
  
	# Update Sprite Group
    all_sprites_list.update()
	# Screen Set up
    screen.fill(surf_color)
	# Displaying Sprites
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()
