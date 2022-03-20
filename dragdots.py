import pygame
pygame.init()
screen = pygame.display.set_mode([1000,1000])
pygame.display.set_caption("Click and drag to draw")
keep_going = True
color1 = (230, 67, 67)
color2 = (158, 252, 114)
cc = color1

radius = 7
mousedown = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
            cc = color1 if cc == color2 else color2            
    if mousedown:
        spot = pygame.mouse.get_pos()
        print(cc)
        pygame.draw.circle(screen, cc, spot, radius)
    pygame.display.update()

pygame.quit()