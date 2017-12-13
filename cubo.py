import pygame
from math import pi
pygame.init()
pf=(100,10)#reales

def conversion(x,y,z): 
    x=x+300
    if(y>=0):
        y=300-y
    else:
        y=-y+300
    ##punto incrementando z
    ##
    x=x+((pf[0]-x)*z/800)
    y=y+((pf[1]-y)*z/800)
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
#cubo
v1=(-100,100,0)
v2=(100,100,0)
v3=(100,-100,0)
v4=(-100,-100,0)
v5=(-100,100,100)
v6=(100,100,100)
v7=(100,-100,100)
v8=(-100,-100,100)
#cubo
while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(24)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    screen.fill(WHITE)    
    #Cubo
    p1=(conversion(v1[0],v1[1],v1[2]))
    p2=(conversion(v2[0],v2[1],v2[2]))
    p3=(conversion(v3[0],v3[1],v3[2]))
    p4=(conversion(v4[0],v4[1],v4[2]))
    p5=(conversion(v5[0],v5[1],v5[2]))
    p6=(conversion(v6[0],v6[1],v6[2]))
    p7=(conversion(v7[0],v7[1],v7[2]))
    p8=(conversion(v8[0],v8[1],v8[2]))
    
    pygame.draw.polygon(screen,BLACK,[p5,p6,p7,p8],0)
    pygame.draw.polygon(screen,[10,10,10],[p2,p6,p7,p3],0)
    pygame.draw.polygon(screen,BLUE,[p8,p7,p3,p4],0)
    pygame.draw.polygon(screen,[50,50,50],[p1,p5,p8,p4],0)
    pygame.draw.polygon(screen,RED,[p1,p5,p6,p2],0)
    pygame.draw.polygon(screen,BLACK,[p1,p2,p3,p4],0)
    #Cubo    
    
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()
