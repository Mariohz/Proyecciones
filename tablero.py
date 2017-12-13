import pygame
from math import pi
pygame.init()
pf=(300,300)#reales

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
#def trasladar(x,y)
###
# x=x+300
# y=300-y
###
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
o=(x,y,z)#(x,y,z)
#pf=(300,50)
c=[100,100]
supi=[0,0]
supd=[0,0]
supizq=[-100,100]
supder=[100,200]

#cubo
#v1=(-100,100,0)
#v2=(100,100,0)
#v3=(100,-100,0)
#v4=(-100,-100,0)
#v5=(-100,100,100)
#v6=(100,100,100)
#v7=(100,-100,100)
#v8=(-100,-100,100)


#cubo
while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(24)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    screen.fill([10,10,10])    
    #Rectangulo
    #supi=conversion(supizq[0],supizq[1],z)
    #supd=conversion(supder[0],supder[1],z)
    #pygame.draw.rect(screen,BLACK,[supi[0],supi[1],abs(supi[0]-supd[0]),abs(supi[1]-supd[1])])
    #z=z+2
    #if z>=600:
    #    z=0   
    #Rectangulo
    #pygame.display.flip()#volcar memoria al monitor.
    #Cubo
    #p1=(conversion(v1[0],v1[1],v1[2]))
    #p2=(conversion(v2[0],v2[1],v2[2]))
    #p3=(conversion(v3[0],v3[1],v3[2]))
    #p4=(conversion(v4[0],v4[1],v4[2]))
    #p5=(conversion(v5[0],v5[1],v5[2]))
    #p6=(conversion(v6[0],v6[1],v6[2]))
    #p7=(conversion(v7[0],v7[1],v7[2]))
    #p8=(conversion(v8[0],v8[1],v8[2]))
    
    #pygame.draw.polygon(screen,BLACK,[p5,p6,p7,p8],0)
    #pygame.draw.polygon(screen,BLACK,[p2,p6,p7,p3],0)
    #pygame.draw.polygon(screen,BLUE,[p1,p5,p8,p4],0)
    #pygame.draw.polygon(screen,BLACK,[p8,p7,p3,p4],0)
    #pygame.draw.polygon(screen,RED,[p1,p5,p6,p2],0)
    #pygame.draw.polygon(screen,BLACK,[p1,p2,p3,p4],0)
    #Cubo    
    #Tablero
    x=-200
    y=-200
    z=0
    for j in range(0,8):    
        for i in range(0,8):
            v1=(x,y,z)
            v2=(x,y,z+50)
            v3=(x+50,y,z+50)
            v4=(x+50,y,z)
            v5=(x,y-25,z)
            v6=(x+50,y-25,z) 
            #QQQcara superior (esq inf izq, sup izq)
            p1=(conversion(v1[0],v1[1],v1[2])) 
            p2=(conversion(v2[0],v2[1],v2[2]))
            p3=(conversion(v3[0],v3[1],v3[2]))
            p4=(conversion(v4[0],v4[1],v4[2]))
            p5=(conversion(v5[0],v5[1],v5[2]))
            p6=(conversion(v6[0],v6[1],v6[2])) 
            #QQQ
            #pygame.draw.polygon(screen,BLACK,[p1,p4,p5,p6],0) 
            if (i+j)%2==0:
                pygame.draw.polygon(screen,BLACK,[p1,p2,p3,p4],0)
            else:
                pygame.draw.polygon(screen,WHITE,[p1,p2,p3,p4],0)
            if j<1:
                pygame.draw.polygon(screen,[230,230,230],[p1,p4,p6,p5],0)  
            x=x+50
        x=-200
        z=z+50
    #Tablero

    pygame.display.flip()
# Be IDLE friendly
pygame.quit()
