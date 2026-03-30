import pygame

pygame.init()

screen=pygame.display.set_mode((648,488))

pygame.display.set_caption("Hello World")

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,255,100), (100,100,100,100))
    pygame.display.update()
pygame.quit()