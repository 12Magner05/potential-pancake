
#Running this file will make a window with the size of the 'WIDTH and HEIGHT' variables(in pixels).
#Feel free to play with the #Settings and Constants
#Have fun! ~12Mag
#Inputs are w,a,d,shift,space

#IMPORTS AND INITIATION
import math
import os
from sys import exit

import pygame

pygame.init()

#Settings and Constants
WIDTH, HEIGHT = 900, 500
GRAVITY = 1
BOUNCE = -.90
FPS = 60
#SCALE changes size of field compared to screen size
SCALE = 2
#POWER changes added velocity with player input
POWER = 10
#CAMERA_SPEED changes how fast camera chases ball
CAMERA_SPEED = 1 / 3

#Window Caption display code
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIDTHSTR, HEIGHTSTR = str(WIDTH), str(HEIGHT)
Name_wxh = 'Bouncy Ball Game  (' + WIDTHSTR + 'x' + HEIGHTSTR + ')'
pygame.display.set_caption(Name_wxh)

count = 0
camera_x_pos = 0
camera_y_pos = 0
origin_x = 0
origin_y = 0
velocity_x = 0
velocity_y = 0
text_x_pos = WIDTH/2
text_y_pos = HEIGHT/2
topspeed = 0

#IMAGES/FONTS/SURFACES
background_surface = pygame.transform.scale(pygame.image.load('Assets/space2.png'),(WIDTH, HEIGHT)).convert()
object_surface = pygame.transform.scale(pygame.image.load('Assets/Soccerfield.png'),(WIDTH * SCALE, HEIGHT * SCALE)).convert()
arimakoshimediumfont = pygame.font.Font('Assets/ArimaKoshi-Medium.otf', 30)
text_surface = arimakoshimediumfont.render(str(count), True, 'Black')
space_ship = pygame.transform.scale(pygame.image.load('Assets/ball.png'), (50, 50)).convert_alpha()


#Where to render stuff on screen
def render_x(pos_x):
    ren_x = pos_x - camera_x_pos
    return ren_x
def render_y(pos_y):
    ren_y = pos_y - camera_y_pos
    return ren_y


clock = pygame.time.Clock()
run = True
while run:
    if count >= 1000: run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #PLAYER INPUT
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity_y += -POWER * 2.5
                elif event.key == pygame.K_w:
                    velocity_y += -POWER * 2.5
                elif event.key == pygame.K_LSHIFT:
                    velocity_y += 2 * POWER
                elif event.key == pygame.K_LSHIFT:
                    velocity_y += POWER
                elif event.key == pygame.K_a:
                    velocity_x += -POWER
                elif event.key == pygame.K_d:
                    velocity_x += POWER
                

#MOVEMENT STUFF
    text_x_pos += velocity_x
    text_y_pos += velocity_y
    velocity_y += GRAVITY
#SPEED CALCULATION
    speedsquared = velocity_y * velocity_y + velocity_x * velocity_x
    speed = int(math.sqrt(speedsquared))


#BORDERS
    if text_x_pos >=WIDTH * SCALE - 8:
        text_x_pos =(WIDTH * SCALE) -9
        velocity_x *= BOUNCE
        count += 1
    if text_y_pos >= HEIGHT * SCALE-8:
        text_y_pos = (HEIGHT * SCALE) - 9
        velocity_y *= BOUNCE
        count += 1
    if text_x_pos <= 0:
        text_x_pos =  1
        velocity_x *= BOUNCE 
        count += 1
    if text_y_pos <= 0:
        text_y_pos = 1
        velocity_y *= BOUNCE
        count += 1
    
#CAMERA STUFF (very proud of figuring this out :D )
    camera_x_vel = (text_x_pos - camera_x_pos - WIDTH / 2) * CAMERA_SPEED
    camera_y_vel = (text_y_pos - camera_y_pos - HEIGHT / 2) * CAMERA_SPEED
    camera_x_pos += camera_x_vel
    camera_y_pos += camera_y_vel

#TOP SPEED COUNTER
    if speed > topspeed:
        topspeed = speed


#RENDERING STUFF AND CLOCK
    text_surface = arimakoshimediumfont.render(('Bounces: ' + str(count) + '|Top Speed: ' + str(topspeed) + '|Current Speed: ' + str(speed)), True, 'Black')
    WIN.blit(background_surface,(0, 0))
    WIN.blit(object_surface,(render_x(0),render_y(0)))
    WIN.blit(space_ship, (render_x(text_x_pos), render_y(text_y_pos)))
    WIN.blit(text_surface, (10, 10))

    pygame.display.update()

    clock.tick(FPS)




pygame.quit()
exit()