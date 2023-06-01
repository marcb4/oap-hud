# https://www.geeksforgeeks.org/python-display-images-with-pygame/
# https://www.askpython.com/python-modules/pygame-looping-background

# importing required library
import pygame

# activate the pygame library .
pygame.init()
X = 600
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
imp = ""
nav = "turn_left"
# Using blit to copy content from one surface to other

status = True
while (status):
    if nav == "turn_left":
        imp = pygame.image.load('D:\Code\pygame_example\\turn_left.png').convert()
        scrn.blit(imp,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    pygame.display.update()
# deactivates the pygame library
pygame.quit()
