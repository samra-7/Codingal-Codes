# import libraries
import pygame  
  
# Setup Pygame window
pygame.init()  
screen = pygame.display.set_mode((500, 500))  
done = False  
is_blue = True 
# Set initial values of position of rectangle 
x = 30  
y = 30  
  
while not done:
	# check the event type  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
		# check if a key has been pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  
            is_blue = not is_blue  
	
	# Check which key has been pressed and update value of x and y accordingly
    pressed = pygame.key.get_pressed()  
    if pressed[pygame.K_UP]: y -= 3  
    if pressed[pygame.K_DOWN]: y += 3  
    if pressed[pygame.K_LEFT]: x -= 3  
    if pressed[pygame.K_RIGHT]: x += 3  

    if is_blue:  
        color = (0, 128, 255)  
    else:   
        color = (255, 100, 0)  
	# draw rectangle
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))  
  
    pygame.display.flip()  