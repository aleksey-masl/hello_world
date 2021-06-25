import pygame

MAX_X = 1280
MAX_Y = 1024
bg_color = (0, 0, 0)

pygame.init()
screen  = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First PyGame Game! :)")

myimage = pygame.image.load("processor_i7.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

game_over = False

x = 500
y = 100
#------------MAIN GAME LOOP ------------------
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_DOWN:
                y += 20
            if event.key == pygame.K_UP:
                y -= 20
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos


    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()