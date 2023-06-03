import pygame, sys
pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Juego")

width, height = 800, 600
speed = [1,1]
white = 255, 255, 255 

img = pygame.image.load("bola.png")
imgrect = img.get_rect()

bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

baterect.move_ip(100,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        baterect = baterect.move(0,-1)
    if keys[pygame.K_DOWN]:
        baterect = baterect.move(0,1)
    if baterect.colliderect(imgrect):
        speed[0] = -speed[0]
    imgrect = imgrect.move(speed)
    if imgrect.left < 0 or imgrect.right > width:
        speed[0] = -speed[0]
    if imgrect.top < 0 or imgrect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(white)
    screen.blit(img, imgrect)
    screen.blit(bate, baterect)
    pygame.display.flip()
    
pygame.quit()
        
