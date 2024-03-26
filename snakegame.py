import pygame,sys

pygame.init()#starts pygame
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()


while True:
    #draw all our elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    pygame.display.update()
    clock.tick(framerate=60)
    
