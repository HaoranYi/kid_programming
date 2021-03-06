import pygame
pygame.init()
screen = pygame.display.set_mode([800,800])
keep_going = True
pic = pygame.image.load("ratpopp.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
speed = 5

while keep_going:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speed
    picy += speed

    if picx <= 0 or picx + pic.get_width() >= 800:
        speed = -speed
    
    screen.fill(BLACK)
    screen.blit(pic,(picx,picy))
    pygame.display.update()
    timer.tick(60)

pygame.quit()