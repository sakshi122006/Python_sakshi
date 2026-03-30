import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
    pygame.draw.rect(screen,red, pygame.Rect(100,30,60,60))
    pygame.draw.polygon(screen, blue,((25,90),(76,125),(375,100),(150,25),(60,150)))
    pygame.draw.circle(screen ,white,(170,180),60)
    pygame.draw.line (screen, red ,(10,175),(300,10),4)
    pygame.draw.ellipse(screen,green ,(275,150,130,180))
    pygame.display.update()