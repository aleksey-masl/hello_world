import pygame

MAX_X = 1280
MAX_Y = 1024
bg_color = (0, 0, 0)
logo_size = 100


#pygame.init()
screen  = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First PyGame Game! :)")

myimage = pygame.image.load("processor_i7.png").convert()
myimage = pygame.transform.scale(myimage, (logo_size, logo_size))

game_over = True

x = 500
y = 100
move_left = False
move_right = False
move_up = False
move_down = False

#------------MAIN GAME LOOP ------------------
while game_over == True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x > MAX_X - logo_size:
                x = MAX_X - logo_size
            if y > MAX_Y - logo_size:
                y = MAX_Y - logo_size
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = False
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_UP:
                move_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False

    if move_left == True:
        x -= 1
        if x < 0:
            x = 0
    if move_right == True:
        x += 1
        if x > MAX_X - logo_size:
            x = MAX_X - logo_size
    if move_up == True:
        y -= 1
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        if y > MAX_Y - logo_size:
            y = MAX_Y - logo_size


    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()