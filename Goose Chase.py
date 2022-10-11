import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((760, 500))

pygame.display.set_caption("Goose Chase")

class player(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 20

class enemy(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 10

class fastenemy(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 14

class point(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

score = 0

red = (255, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)

black = (0, 0, 0)

white = (255, 255, 255)

rustic_red = (137, 16, 16) 

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

font_bigger = pygame.font.SysFont(None, 50)

def draw_player(win, color, posx, posy, sizex, sizey):
    pygame.draw.rect(win, color, (posx, posy, sizex, sizey))
    pygame.display.update

def draw_enemy(win, color, posx, posy, sizex, sizey):
    pygame.draw.rect(win, color, (posx, posy, sizex, sizey))

def draw_fastenemy(win, color, posx, posy, sizex, sizey):
    pygame.draw.rect(win, color, (posx, posy, sizex, sizey))

def draw_score(win, color, posx, posy, sizex, sizey):
    pygame.draw.rect(win, color, (posx, posy, sizex, sizey))

def draw_borders(win, color, posx, posy, sizex, sizey):
    pygame.draw.rect(win, color, (posx, posy, sizex, sizey))

def score_counter(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [660, 460])

def score_display(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [725, 460])

def game_over_msg(msg, color):
    text = font_bigger.render(msg, True, color)
    screen.blit(text, [100, 225])

def final_score(msg, color):
    text = font_bigger.render(msg, True, color)
    screen.blit(text, [615, 225])

def help_msg(msg, color, x, y):
    text = font.render(msg,True, color)
    screen.blit(text, [x, y])

fast_spawned = False
help_menu = True
sqrroot = 0.5
fps = 20
score = 0
samepos_x = False
samepos_y = False
run = True
alive = False
char = player(50, 50, 20, 20, blue)
coin = point(random.randint(25, 645), random.randint(25, 460), 15, 15, green)
badguy = enemy(600, 400, 40, 40, red)
fastbadguy = fastenemy(600, 400, 30, 30, rustic_red)

while run:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if alive == False and help_menu == True:
        screen.fill(white)
        help_msg("This is your character", black, 50, 100)
        draw_player(screen, char.color, 300, 100, char.width, char.height)
        help_msg("Collect the green cubes to add score to your counter!", black, 50, 150)
        draw_score(screen, coin.color, 600, 150, coin.width, coin.height)
        help_msg("Avoid the enemys trying to hunt you down", black, 50, 200)
        draw_enemy(screen, badguy.color, 500, 200, badguy.width, badguy.height)
        help_msg("As your score increases, a faster enemy will spawn", black, 50, 250)
        draw_fastenemy(screen, fastbadguy.color, 580, 250, fastbadguy.width, fastbadguy.height)
        help_msg("Use W A S D keys to move your character around!", black, 50, 300)
        help_msg("Press Space To Begin.", blue, 50, 350)
        pygame.display.update()
        if keys[pygame.K_SPACE]:
            alive = True
            help_menu = False


        
    
    if alive == True and help_menu == False:
        if keys[pygame.K_a] and char.x > char.vel:
            char.x -= char.vel
    
        if keys[pygame.K_d] and char.x < 750 - char.width - 13:
            char.x += char.vel
    
        if keys[pygame.K_w] and char.y - 10 > 0:
            char.y -= char.vel
    
        if keys[pygame.K_s] and char.y < 500 - char.height - 13:
            char.y += char.vel

        if keys[pygame.K_q]:
            fps -= 2

        if keys[pygame.K_e]:
            fps += 2
        
        
        
    
        if char.x - (badguy.x) or badguy.x - (char.x) < char.y - (badguy.y) or badguy.y - (char.y) and char.x + char.width < badguy.x and char.x > badguy.x + badguy.width:
            if char.y - (badguy.y) < -10 and 10 > char.y - (badguy.y):
                badguy.y -= badguy.vel
            elif char.y - (badguy.y) > -10 and 10 < char.y - (badguy.y):
                badguy.y += badguy.vel
            elif ((char.y - (badguy.y))**2)**(sqrroot) < 0 and char.y - (badguy.y) <= 20:
                char.y = badguy.y
            elif char.x - (badguy.x) or badguy.x - (char.x) < char.y - (badguy.y) or badguy.y - (char.y) and char.y + char.height < badguy.y and char.y > badguy.y + badguy.height:
                pass
        
        if char.x - (badguy.x) or badguy.x - (char.x) > char.y - (badguy.y) or badguy.y - (char.y) and char.y + char.height < badguy.y and char.y > badguy.y + badguy.height:
            if char.x - (badguy.x) < -10 and 0 > char.x - (badguy.x):
                badguy.x -= badguy.vel
            elif char.x - (badguy.y) > -10 and 10 < char.x - (badguy.x):
                badguy.x += badguy.vel
            elif ((char.x - (badguy.x))**2)**(sqrroot) < 0 and char.x - (badguy.x) <= 20:
                badguy.x = char.x
            elif char.x - (badguy.x) or badguy.x - (char.x) < char.y - (badguy.y) or badguy.y - (char.y) and char.x + char.width < badguy.x and char.x > badguy.x + badguy.width:
                pass
        
        if fast_spawned == True:
            if char.x - (fastbadguy.x) or fastbadguy.x - (char.x) < char.y - (fastbadguy.y) or fastbadguy.y - (char.y) and char.x + char.width < fastbadguy.x and char.x > fastbadguy.x + fastbadguy.width:
                if char.y - (fastbadguy.y) < -10 and 10 > char.y - (fastbadguy.y):
                    fastbadguy.y -= fastbadguy.vel
                elif char.y - (fastbadguy.y) > -10 and 10 < char.y - (fastbadguy.y):
                    fastbadguy.y += fastbadguy.vel
                elif ((char.y - (fastbadguy.y))**2)**(sqrroot) < 0 and char.y - (fastbadguy.y) <= 20:
                    char.y = fastbadguy.y
                elif char.x - (fastbadguy.x) or fastbadguy.x - (char.x) < char.y - (fastbadguy.y) or fastbadguy.y - (char.y) and char.y + char.height < fastbadguy.y and char.y > fastbadguy.y + fastbadguy.height:
                    pass
        
            if char.x - (fastbadguy.x) or fastbadguy.x - (char.x) > char.y - (fastbadguy.y) or fastbadguy.y - (char.y) and char.y + char.height < fastbadguy.y and char.y > fastbadguy.y + fastbadguy.height:
                if char.x - (fastbadguy.x) < -10 and 0 > char.x - (fastbadguy.x):
                    fastbadguy.x -= fastbadguy.vel
                elif char.x - (fastbadguy.y) > -10 and 10 < char.x - (fastbadguy.x):
                    fastbadguy.x += fastbadguy.vel
                elif ((char.x - (fastbadguy.x))**2)**(sqrroot) < 0 and char.x - (fastbadguy.x) <= 20:
                    fastbadguy.x = char.x
                elif char.x - (fastbadguy.x) or fastbadguy.x - (char.x) < char.y - (fastbadguy.y) or fastbadguy.y - (char.y) and char.x + char.width < fastbadguy.x and char.x > fastbadguy.x + fastbadguy.width:
                    pass
            
            if fastbadguy.x < 10:
                fastbadguy.x = 10
            if fastbadguy.x > 725:
                fastbadguy.x = 705
            if fastbadguy.y < 10:
                fastbadguy.y = 10
            if fastbadguy.y > 455:
                fastbadguy.y = 455
            
            if fastbadguy.x + fastbadguy.width > char.x and fastbadguy.x < char.x + char.width:
                if fastbadguy.y + fastbadguy.height > char.y and fastbadguy.y < char.y + char.height:
                    alive = False
                    print("Game Over, your score is:", score)
        
            if fastbadguy.x + fastbadguy.width > char.x and fastbadguy.x < char.x + char.width:
                if fastbadguy.x < char.x + 20 and fastbadguy.x > char.x + 20:
                    alive = False
                    print("Game Over, your score is :", score)
        
        if badguy.x < 10:
            badguy.x = 10
        if badguy.x > 720:
            badguy.x = 700
        if badguy.y < 10:
            badguy.y = 10
        if badguy.y > 450:
            badguy.y = 450

        if badguy.x + badguy.width > char.x and badguy.x < char.x + char.width:
            if badguy.y + badguy.height > char.y and badguy.y < char.y + char.height:
                alive = False
                print("Game Over, your score is:", score)
        
        if badguy.x + badguy.width > char.x and badguy.x < char.x + char.width:
            if badguy.x < char.x + 20 and badguy.x > char.x + 20:
                alive = False
                print("Game Over, your score is :", score)
         
        
        if char.x + char.width > coin.x and char.x < coin.x + coin.width:
            if char.y + char.height > coin.y and char.y < coin.y + coin.height:
                score += 1
                coin.x = random.randint(10, 735)
                coin.y = random.randint(10, 475)
        
        if char.y + char.height > coin.y and char.y < coin.y + coin.height:
            if char.x + char.width > coin.x and char.x < coin.x + coin.width:
                score += 1
                coin.x = random.randint(10, 735)
                coin.y = random.randint(10, 475)

       
            
        
        
        
    if alive == True:
        screen.fill(white)
        
        score_counter("Score:", black)
    
        score_display(str(score), black)
         
        draw_player(screen, char.color, char.x, char.y, char.width, char.height)
        
        draw_enemy(screen, badguy.color, badguy.x, badguy.y, badguy.width, badguy.height)
        
        if score >= 5:
            draw_fastenemy(screen, fastbadguy.color, fastbadguy.x, fastbadguy.y, fastbadguy.width, fastbadguy.height)
            fast_spawned = True

        draw_score(screen, coin.color, coin.x, coin.y, coin.width, coin.height)
        
        draw_borders(screen, (51,153,255), 0, 0, 10, 500)
        
        draw_borders(screen, (51,153,255), 10, 0, 750, 10)
        
        draw_borders(screen, (51,153,255), 10, 490, 740, 10)
        
        draw_borders(screen, (51,153,255), 750, 10, 10, 490)    
        
        pygame.display.update()

    if alive == False and help_menu == False:
        screen.fill(white)
        game_over_msg("Game Over, your final score is:", black)
        final_score(str(score), black)
        pygame.display.update()
        time.sleep(3)
        run = False



pygame.quit()
