import pygame
from math import pi
pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Example code for the draw module")

done = False
clock = pygame.time.Clock()
x=5
y=5
radio=10
flag=0
flagx=0
while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    screen.fill(WHITE)

    ######
    pygame.draw.circle(screen, BLUE, [x, y], radio)
    if flag==0:
        if y+radio<size[1]:
            y=y+5
        else:
            flag=1  
    else:
        if y-radio>0:
            y=y-5
        else:
            flag=0
    if flagx==0:
        if x+radio<size[0]:
            x=x+1
        else:
            flagx=1
    else:
        if x-radio>0:
            x=x-1
        else:
            flagx=0
    #####
    pygame.display.flip()#volcar memoria al monitor.

# Be IDLE friendly
pygame.quit()

