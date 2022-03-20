import pygame

# setup
pygame.init()
screen = pygame.display.set_mode([600, 600])
keep_going = True
#pic = pygame.image.load('crazy_smile.jpg')
pic = pygame.image.load('ratpopp.png')
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()  # timer for animation
speed = 6

while keep_going:  # game loop
    # exit
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            keep_going = False

    # move the picture
    picx +=speed
    picy +=speed

    # bounce
    if picx <= 0 or picx + pic.get_width() >= 600:
        speed = -speed

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60)

# exit
pygame.quit()
