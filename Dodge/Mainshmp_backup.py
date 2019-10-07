import pygame
import random
import time
import pickle

WIDTH = 800
HEIGHT = 800
FPS =60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

pygame.init()
pygame.mixer.init()
pygame.joystick.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dodge")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#TopScore
pickle_in = open("topscore.dat", "rb")
topscore_save = pickle.load(pickle_in)
topscore = topscore_save

#sounds/music
pygame.mixer.music.load("random silly chip song.wav")
pygame.mixer.music.play(-1)
lasersound = pygame.mixer.Sound("laser.wav")
explosion = pygame.mixer.Sound("explosion.wav")
powerup_sound = pygame.mixer.Sound("Powerup.wav")
oneup_sound = pygame.mixer.Sound("1up.wav")
laserup_sound = pygame.mixer.Sound("laserup.wav")

#load images
alien_img = []
alien_list = ["shipBeige.png","shipYellow.png","shipPink.png","shipGreen.png","shipBlue.png"]
for img in alien_list:
    alien_img.append(pygame.image.load(img).convert_alpha())

kenny = pygame.image.load("kenny.png")
laser = pygame.image.load("beam.png")
star_field = pygame.image.load("back1.png")
powerUp_img = pygame.image.load("star1.png")
laserUp_img = pygame.image.load("laserstar.png")
oneUp_img = pygame.image.load("1up.png")

asteroid_img = []
asteroid_list = ["asteroid1.png", "asteroid2.png", "asteroid3.png", "asteroid4.png"]
for img in asteroid_list:
    asteroid_img.append(pygame.image.load(img).convert_alpha())

explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for i in range(11):
    filename = 'Explosion{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img,(75,75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img,(32,32))
    explosion_anim["sm"].append(img_sm)
    img_player = pygame.transform.scale(img,(200,200))
    explosion_anim["player"].append(img_player)

button1 = pygame.image.load("button1.png")
button2 = pygame.image.load("button2.png")
quit1 = pygame.image.load("quit1.png")
quit2 = pygame.image.load("quit2.png")

pygame.image.load("spaceShip.png").convert_alpha()
player_Img = pygame.image.load("spaceShip.png").convert_alpha()
player_mini_img = pygame.transform.scale(player_Img,(25,19)).convert_alpha()

player_mask = pygame.mask.from_surface(player_Img)
player_rect = player_Img.get_rect()

pause = False

#drawing surfaces
def draw_text(surf,text, size, x, y):
    font = pygame.font.Font('Gretoon.ttf', 20)
    text = font.render("Score: " +str(score), True, RED)
    surf.blit(text, (20,10))

def draw_topscore(surf,text, size, x, y):
    font = pygame.font.Font('Gretoon.ttf', 20)
    text = font.render("TopScore: " +str(topscore), True, RED)
    surf.blit(text, (550,10))

def draw_shield_bar(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100 * BAR_LENGTH)
    outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf,WHITE, outline_rect,3)

def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('SnackerComic.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


#CRASH
def crash():
    pause = True

    while pause:
        for event in pygame.event.get():
            print(event)
            
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
        
        screen.blit(kenny,(350, 350))
        largeText = pygame.font.Font('SnackerComic.ttf',150)
        TextSurf, TextRect = text_objects("You're Dead!", largeText)
        TextRect.center = (WIDTH/2),(HEIGHT/3)
        screen.blit(TextSurf, TextRect)

        button(200,500,100,39,button1,button2, "play")
        button(500,500,100,39,quit1,quit2, "quit")

        pygame.display.update()
        clock.tick(15)

#BUTTON
def button(x,y,w,h, b1, b2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    screen.blit(b2,(x,y))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            if action == "unpause":
                unpause()
            elif action == "quit":
                pygame.quit()

        screen.blit(b1,(x,y))

def unpause():
    global pause
    pause = False
def paused():
    pause = True
#PAUSE
    while pause:
        for event in pygame.event.get():
            print(event)
           
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
        
        screen.blit(kenny,(350, 350))
        largeText = pygame.font.Font('SnackerComic.ttf',115)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/3))
        screen.blit(TextSurf, TextRect)

        button(200,500,100,39,button1,button2, "play")
        button(500,500,100,39,quit1,quit2, "quit")
      
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pause = False
    
    

#BACKGROUND
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load("back.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
bg = Background('background_image.png', [0,0])

class star_field(pygame.sprite.Sprite):
    def __init__(self,image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("back1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        self.speedy = 2

bg1 = star_field("star_field_image.png",[0,0])

def new_asteroids():
    m = Asteroid()
    all_sprites.add(m)
    asteroids.add(m)

def new_aliens():
    a = Alien()
    all_sprites.add(a)
    aliens.add(a)

def new_powerUp():
    p = PowerUp()
    all_sprites.add(p)
    powerUp.add(p)

def new_laserUp():
    l = LaserUp()
    all_sprites.add(l)
    laserUp.add(l)

def new_oneUp():
    o = OneUp()
    all_sprites.add(o)
    oneUp.add(o)

#PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceShip.png")
        self.rect = self.image.get_rect()
        self.radius = 28
    #    pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100
    #    self.shoot_delay = 250
    #   self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
    
    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH /2
            self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_d]:
            self.speedx = 5
    #    if keystate[pygame.K_SPACE]:
    #        self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
    #    now = pygame.time.get_ticks()
    #    if now - self.last_shot > self.shoot_delay:
    #        self.last_shot = now
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        lasersound.play()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT + 200)

#ASTEROIDS
class Asteroid(pygame.sprite.Sprite):
    def  __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(asteroid_img)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .75 /2)
     #   pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)
            

#ALIEN
class Alien(pygame.sprite.Sprite):
    def  __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(alien_img)
        self.rect = self.image.get_rect()
        self.radius = 25
    #    pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-1,1)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)

#BULLET

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("beam.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect.center = center

#Bonus Ups
class PowerUp(pygame.sprite.Sprite):
    def  __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = powerUp_img
        self.rect = self.image.get_rect()
        self.radius = 15
    #    pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-2,2)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)

class LaserUp(pygame.sprite.Sprite):
    def  __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = laserUp_img
        self.rect = self.image.get_rect()
        self.radius = 15
    #    pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-2,2)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)

class OneUp(pygame.sprite.Sprite):
    def  __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = oneUp_img
        self.rect = self.image.get_rect()
        self.radius = 10
    #    pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-2,2)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)


all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerUp = pygame.sprite.Group() 
laserUp = pygame.sprite.Group() 
oneUp = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


for i in range(10):
    m = Asteroid()
    all_sprites.add(m)
    asteroids.add(m)
for i in range(5):
    a = Alien()
    all_sprites.add(a)
    aliens.add(a)
for i in range(1):
    p = PowerUp()
    all_sprites.add(p)
    powerUp.add(p)
for i in range(1):
    l = LaserUp()
    all_sprites.add(l)
    laserUp.add(l)
for i in range(1):
    o = OneUp()
    all_sprites.add(o)
    oneUp.add(o)

score = 0

#game loop
running = True
while running:
    
    clock.tick(FPS)

    pickle_in = open("topscore.dat", "rb")
    topscore_save = pickle.load(pickle_in)
    topscore = topscore_save
    
#process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
                paused()
                
#Update
    all_sprites.update()

#check if player hit
    hits = pygame.sprite.spritecollide(player, asteroids, True, pygame.sprite.collide_circle)
    for hit in hits:
        explosion.play()
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, "sm")
        all_sprites.add(expl)
        new_asteroids()
        if player.shield <= 0:
           # running = False
            death_expl = Explosion(player.rect.center, "player")
            all_sprites.add(death_expl)
            player.hide()
            player.lives -= 1
            player.shield = 100
    if player.lives == 0 and not death_expl.alive():
        crash()

    hits = pygame.sprite.spritecollide(player, aliens, True, pygame.sprite.collide_circle)
    for hit in hits:
        explosion.play()
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, "sm")
        all_sprites.add(expl)
        new_aliens()
        if player.shield <= 0:
            death_expl = Explosion(player.rect.center, "player")
            all_sprites.add(death_expl)
            player.hide()
            player.lives -= 1
            player.shield = 100
    if player.lives == 0 and not death_expl.alive():
        crash()

#PowerUp
    hits = pygame.sprite.spritecollide(player, powerUp, True, pygame.sprite.collide_circle)
    for hit in hits:
        powerup_sound.play()
        if player.shield < 100:
            player.shield += random.randrange(10,25)   
            if player.shield > 100:
                player.shield = 100
        else:
            score += random.randrange(5, 500)
        new_powerUp()

#laserup
    hits = pygame.sprite.spritecollide(player, laserUp, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += random.randrange(5, 500)
        laserup_sound.play()
        new_laserUp()

#OneUp
    hits = pygame.sprite.spritecollide(player, oneUp, True, pygame.sprite.collide_circle)
    for hit in hits:
        if player.lives < 2:
            player.lives += 1
        else:
            score += random.randrange(5, 500)
        oneup_sound.play()
        new_oneUp()




#check if bullets hit
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    for hit in hits:
        explosion.play()
        score += 50 - hit.radius
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
        new_asteroids()

    hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
    for hit in hits:
        explosion.play()
        score += 25
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
        new_aliens()


#score save
    if score > int(topscore):
        x = score
        topscore_save = int(x)
        pickle_out = open("topscore.dat","wb")
        pickle.dump(topscore_save, pickle_out)
        print(topscore_save)
        pickle_out.close()

#Draw/ render
    screen.fill(BLACK)
    screen.blit(bg.image, bg.rect)
    screen.blit(bg1.image, bg.rect)
    
    all_sprites.draw(screen)
    draw_text(screen, str(score), 20, WIDTH, HEIGHT)
    draw_topscore(screen, str(topscore_save),20, 550, 10)
    draw_shield_bar(screen,WIDTH/2 - 55,10,player.shield)
    draw_lives(screen, WIDTH/2 - 50, 30, player.lives, player_mini_img)

    pygame.display.flip()

game_loop()
pygame.quit()
quit()
