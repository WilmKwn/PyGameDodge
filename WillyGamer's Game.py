import pygame
import time
import random

pygame.init()

display_width = 800
display_height= 600

black = (0,0,0)
white = (255,255,255)

red = (150,0,0)
lime = (0,255,0)

blue = (0,0,255)
green = (0,100,0)

bright_red = (250,0,0)
bright_green = (0,255,255)

car_width = 80
car_height = 110

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Dodgey')
clock = pygame.time.Clock()

carImg = pygame.image.load('coolkid.png')
background = pygame.image.load('arenaBg.png')
intro_img = pygame.image.load('dodgypic.jpg')

def things_dodged(count):
    font = pygame.font.SysFont(None, 51)
    text = font.render("Dodged:"+str(count), True, blue)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def intro_pic(old_x,old_y):
    gameDisplay.blit(intro_img,(old_x,old_y))

def bg_img(new_x,new_y):
    gameDisplay.blit(background,(new_x,new_y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    game_loop()


def crash():
    gameDisplay.fill(red)
    message_display('YOU HAVE CRASHED!!')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    old_x = (display_width * 0.24)
    old_y = (display_height * 0.0001)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(lime)
        intro_pic(old_x,old_y)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("A bit dodgy", largeText)
        TextRect.center = ((display_width/2),(display_height/1.6))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY!",150,450,100,50,green,bright_green,"play")
        button("Quit :(",550,450,100,50,bright_red,red,"quit")

        
        mouse = pygame.mouse.get_pos()
             
        pygame.display.update()
        clock.tick(15)
       
        
def game_loop():
    
    x = (display_width * 0.48)
    y = (display_height * 0.55)

    new_x = (display_width * 0.003)
    new_y = (display_height * 0.003)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    dodged = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                elif event.key == pygame.K_UP:
                    y_change = -7
                elif event.key == pygame.K_DOWN:
                    y_change = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0



        x += x_change
        y += y_change
        
        gameDisplay.fill(lime)
        
        # thingx, thingy, thingw, thingh, color
        bg_img(new_x,new_y)
        things(thing_startx, thing_starty, thing_width, thing_height, red)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
        elif y > display_height - car_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.25
            thing_width += (dodged * 1)
            thing_height += (dodged * 0.01)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
            
