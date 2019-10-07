import pygame
import time
import random
#import Pause


pygame.init()

display_width = 800
display_height = 800

HW,HH = display_width / 2, display_height / 2
AREA = display_width * display_height

white = (255,255,255)
black = (0,0,0,)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

player_width = 50
player_heigth = 50

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge')
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.font.init()

pygame.mixer.music.load("random silly chip song.wav")
pygame.mixer.music.play(-1)
lasersound = pygame.mixer.Sound("laser.wav")


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("back.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
bg = Background('background_image.png', [0,0])

alien1_img = pygame.image.load("shipYellow.png").convert_alpha()
alien3_img = pygame.image.load("shipBeige.png").convert_alpha()
alien2_img = pygame.image.load("shipPink.png").convert_alpha()
alien4_img = pygame.image.load("shipGreen.png").convert_alpha()

kenny = pygame.image.load("kenny.png")
laser = pygame.image.load("beam.png")

ast_3 = pygame.image.load("asteroid3.png").convert_alpha()
ast_4 = pygame.image.load("asteroid4.png").convert_alpha()
ast_1 = pygame.image.load("asteroid1.png").convert_alpha()
ast_2 = pygame.image.load("asteroid2.png").convert_alpha()

button1 = pygame.image.load("button1.png")
button2 = pygame.image.load("button2.png")

alien4_mask = pygame.mask.from_surface(alien4_img)
alien3_mask = pygame.mask.from_surface(alien3_img)
alien2_mask = pygame.mask.from_surface(alien2_img)
alien1_mask = pygame.mask.from_surface(alien1_img)

asteroids = ['ast_1', 'ast_2', 'ast_3', 'ast_4']
 
def asteroid_field():
    asteroid = asteroids[random.randrange(len(asteroids))]
    print(asteroid)

def ast1(ast1x, ast1y):
    gameDisplay.blit(ast_1,(ast1x, ast1y))

def ast2(ast2x, ast2y):
    gameDisplay.blit(ast_2,(ast2x, ast2y))

def ast3(ast3x, ast3y):
    gameDisplay.blit(ast_3,(ast3x, ast3y))

def ast4(ast4x, ast4y):
    gameDisplay.blit(ast_4,(ast4x, ast4y))

class alien(pygame.sprite.Sprite):
    def __init__(self,image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("alien")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.alien_startx = random.randrange(0, 600)
        self.alien_starty = -900
        self.alien_speed = random.randint(2,6)
        self.alien_width = 50
        self.alien_heigth = 50
        self.alien(alien_startx, alien_starty)
        self.alien_starty += alien_speed
        self.alien_starty > display_height
        self.alien_starty = 0 -alien_heigth
        self.alien_startx = random.randrange(0, display_width)
        self.alien(alien_startx, alien_starty)
        self.alien_starty += alien_speed

def alien1(alien1x, alien1y):
    gameDisplay.blit(alien1_img,(alien1x, alien1y))
   
def alien2(alien2x, alien2y):
    gameDisplay.blit(alien2_img,(alien2x, alien2y))
    
def alien3(alien3x, alien3y):
    gameDisplay.blit(alien3_img,(alien3x, alien3y))
    
def alien4(alien4x, alien4y):
    gameDisplay.blit(alien4_img,(alien4x, alien4y))
    
player_Img = pygame.image.load('shipBlue.png').convert_alpha()
player_mask = pygame.mask.from_surface(player_Img)
player_rect = player_Img.get_rect()

def alien_dodged(count):
    font = pygame.font.Font('Gretoon.ttf', 20)
    text = font.render("Dodged: " +str(count), True, red)
    gameDisplay.blit(text, (0,0))

#player_x = 380
#player_y = 700

#laser_x = player_x + player_width//2
#laser_y = player_y - 20 + player_heigth//2

def player(x, y):
    gameDisplay.blit(player_Img,(x,y))

#LASER  
#laser_x_change = 0
#laser_y_change = laser_y+10
#laserstate = "ready"

#def fire_laser():
#    global laserstate
#    if laserstate == "ready":
#        gameDisplay.blit(laser,(laser_x, laser_y))
#        laserstate = "fire"
#        lasersound.play()    

pause = True

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('SnackerComic.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def crash():
    pause = True

    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_p:
                   pause = False
                   game_loop()
        
        gameDisplay.blit(kenny,(450, 450))
        largeText = pygame.font.Font('SnackerComic.ttf',150)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button(200,500,100,39,button1,button2, "play")
        
        pygame.display.update()
        clock.tick(15)

def button(x,y,w,h, b1, b2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    gameDisplay.blit(b2,(x,y))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "unpause":
                unpause()
            elif action == "quit":
                pygame.quit()

        gameDisplay.blit(b1,(x,y))
    
def unpause():
    global pause
    pause = False
def paused():
    pause = True

    while pause:
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_p:
                   pause = False

        
        gameDisplay.blit(kenny,(450, 450))
        largeText = pygame.font.Font('SnackerComic.ttf',115)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button(200,500,100,39,button1,button2, "play",)

        
      
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    global laserstate
   
    asteroid_field()

    x = (display_width * 0.45)
    y = (display_height * 0.85)

    x_change = 0
   # player_speed = 0
#asteroids
    ast1_startx = -(random.randrange(0, 60))
    ast1_starty = -(random.randint(200, 500))
    ast1_speed = random.randint(1, 4)
    ast1_width = 60
    ast1_heigth = 60

    ast2_startx = random.randrange(400, 600)
    ast2_starty = 0
    ast2_speed = random.randint(1, 4)
    ast2_width = 30
    ast2_heigth = 30

    ast3_startx = -(random.randrange(0, 60))
    ast3_starty = -(random.randint(2, 500))
    ast3_speed = random.randint(1, 4)
    ast3_width = 40
    ast3_heigth = 40

    ast4_startx = -(random.randrange(0, 60))
    ast4_starty = -(random.randint(2, 500))
    ast4_speed = random.randint(1, 4)
    ast4_width = 70
    ast4_heigth = 70
#aliens
    alien1_startx = random.randrange(0, 600)
    alien1_starty = -900
    alien1_speed = random.randint(5,10)
    alien1_width = 50
    alien1_heigth = 50

    alien2_startx = random.randrange(0, 600)
    alien2_starty = -900
    alien2_speed = random.randint(2,6)
    alien2_width = 50
    alien2_heigth = 50

    alien3_startx = random.randrange(0, 600)
    alien3_starty = -900
    alien3_speed = random.randint(7,15)
    alien3_width = 50
    alien3_heigth = 50

    alien4_startx = random.randrange(0, 600)
    alien4_starty = -900
    alien4_speed = random.randint(2,10)
    alien4_width = 50
    alien4_heigth = 50

    dodged = 0

    gameExit = False

    bullets = []
    for bullet in bullets:
        bullet.draw(win)
    
#    shootLoop = 0
#gameloop start
    while not gameExit:
#events
        for event in pygame.event.get():
         #   print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                if event.key == pygame.K_RIGHT:
                    x_change = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_SPACE:
#                   fire_laser()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()

        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(bg.image, bg.rect)
        player(x,y)
        x += x_change
        alien_dodged(dodged)
#asteroids
        ast1(ast1_startx, ast1_starty)
        ast1_starty += ast1_speed
        ast1_startx += ast1_speed

        ast2(ast2_startx, ast2_starty)
        ast2_starty += ast2_speed
        ast2_startx -= ast2_speed

        ast3(ast3_startx, ast3_starty)
        ast3_starty += ast3_speed
        ast3_startx += ast3_speed

        ast4(ast4_startx, ast4_starty)
        ast4_starty += ast4_speed
        ast4_startx -= ast4_speed
#aliens
        alien1(alien1_startx, alien1_starty)
        alien1_starty += alien1_speed

        alien2(alien2_startx, alien2_starty)
        alien2_starty += alien2_speed

        alien3(alien3_startx, alien3_starty)
        alien3_starty += alien3_speed

        alien4(alien4_startx, alien4_starty)
        alien4_starty += alien4_speed
#crash
        if x > display_width - player_width or x < 0:
            crash()
#asteroids          
        if ast1_starty > display_height:
            ast1_starty = 0 -ast1_heigth
            ast1_startx = random.randrange(0, display_width)
        if ast2_starty > display_height:
            ast2_starty = 0 -ast2_heigth
            ast2_startx = random.randrange(0, display_width)
        if ast3_starty > display_height:
            ast3_starty = 0 -ast3_heigth
            ast3_startx = random.randrange(0, display_width)
        if ast4_starty > display_height:
            ast4_starty = 0 -ast4_heigth
            ast4_startx = random.randrange(0, display_width)
#aliens
        if alien1_starty > display_height:
            alien1_starty = 0 -alien1_heigth
            alien1_startx = random.randrange(0, display_width)
            dodged += 1
        if alien2_starty > display_height:
            alien2_starty = 0 -alien2_heigth
            alien2_startx = random.randrange(0, display_width)
            dodged += 1
        if alien3_starty > display_height:
            alien3_starty = 0 -alien3_heigth
            alien3_startx = random.randrange(0, display_width)
            dodged += 1
        if alien4_starty > display_height:
            alien4_starty = 0 -alien4_heigth
            alien4_startx = random.randrange(0, display_width)
            dodged += 1
#asteroids            
        if y < ast1_starty + ast1_heigth:
            if x > ast1_startx and x < ast1_startx + ast1_width or x + player_width > ast1_startx and x + player_width < ast1_startx + ast1_width:
                crash()
        if y < ast2_starty + ast2_heigth:
            if x > ast2_startx and x < ast2_startx + ast2_width or x + player_width > ast2_startx and x + player_width < ast2_startx + ast2_width:
                crash()
        if y < ast3_starty + ast3_heigth:
            if x > ast3_startx and x < ast3_startx + ast3_width or x + player_width > ast3_startx and x + player_width < ast3_startx + ast3_width:
                crash()
        if y < ast4_starty + ast4_heigth:
            if x > ast4_startx and x < ast4_startx + ast4_width or x + player_width > ast4_startx and x + player_width < ast4_startx + ast4_width:
                crash()
#aliens
        if y < alien1_starty + alien1_heigth:
            if x > alien1_startx and x < alien1_startx + alien1_width or x + player_width > alien1_startx and x + player_width < alien1_startx + alien1_width:
                crash()
        if y < alien2_starty + alien2_heigth:
            if x > alien2_startx and x < alien2_startx + alien2_width or x + player_width > alien2_startx and x + player_width < alien2_startx + alien2_width:
                crash()
        if y < alien3_starty + alien3_heigth:
            if x > alien3_startx and x < alien3_startx + alien3_width or x + player_width > alien3_startx and x + player_width < alien3_startx + alien3_width:
                crash()
        if y < alien4_starty + alien4_heigth:  
            if x > alien4_startx and x < alien4_startx + alien4_width or x + player_width > alien4_startx and x + player_width < alien4_startx + alien4_width:
                crash()
         
 #       if laserstate is "fire":
 #           fire_laser()
 #           laser_y -= laser_y_change
 #           laserstate = "ready"

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()


