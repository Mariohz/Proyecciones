import pygame
from math import pi
pygame.init()
pf=(300,10)#reales

def conversion(x,y,z): 
    x=x+300
    if(y>=0):
        y=300-y
    else:
        y=-y+300
    ##punto incrementando z
    ##
    x=x+((pf[0]-x)*z/300)
    y=y+((pf[1]-y)*z/300)
    c=[x,y] 
    return c
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

done = False
clock = pygame.time.Clock()
x=0
y=0
z=0
c=[100,100]
supi=[0,0]
supd=[0,0]
supizq=[-100,100]
supder=[100,200]

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(24)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    screen.fill(WHITE)    
    #Rectangulo
    supi=conversion(supizq[0],supizq[1],z)
    supd=conversion(supder[0],supder[1],z)
    pygame.draw.rect(screen,BLACK,[supi[0],supi[1],abs(supi[0]-supd[0]),abs(supi[1]-supd[1])])
    z=z+2
    if z>=300:
        z=0   
    #Rectangulo

    pygame.display.flip()
# Be IDLE friendly
pygame.quit()
