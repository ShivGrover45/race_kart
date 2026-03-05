import random
import time

import pygame
pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
race_car=pygame.image.load('racecar.png')
d_width=800
d_height=600
car_width=73
g_display=pygame.display.set_mode((d_width,d_height))

pygame.display.set_caption('Race Game')

clock=pygame.time.Clock()

def test_object(t,font):
    textSurface=font.render(t,True,black)
    return textSurface,textSurface.get_rect()

def things(thing_x,thing_y,thing_w,thing_h,color):
    pygame.draw.rect(g_display,color,[thing_x,thing_y,thing_w,thing_h])



def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=test_object(text,largeText)
    TextRect.center=((d_width/2),(d_height/2))
    g_display.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()



def game(x,y):
    g_display.blit(race_car,(x,y))

def crash():
    message_display("You crashed")






def game_loop():
    game_exit= False
    x = d_width*0.45
    y = d_height*0.80
    x_change = 0

    thing_startx=random.randrange(0,d_width)
    thing_starty=-600
    thing_speed=5
    thing_width=100
    thing_height=100

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        g_display.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,red)
        thing_starty+=thing_speed
        game(x, y)

        if x>d_width-car_width or x<0:
            crash()

        if thing_starty>d_height:
            thing_starty=0-300
            thing_startx=random.randrange(0,d_width)

        if y<thing_starty+thing_height:
            print('y-crossover')
            if thing_startx < x < thing_startx+thing_width or x+car_width>thing_startx and x<thing_startx+car_width:
                print('x-crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()